# aem-toc-generator

Generate Mimir-compatible TOC JSON files from AEM-page HTML files.

## Structure of AEM HTML files

AEM documentation HTML files use two structural patterns, sometimes combined
within the same document.

### Pattern 1: Nested articles

The primary structure in most AEM docs. Articles are nested using CSS classes
`nested0`, `nested1`, `nested2`, etc. Each article has an `id` attribute and
a heading with a `topictitle` class.

Example files:
- `red_hat_content/documentation/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_awx_manage_utility/aem-page/administer-assembly_controller_awx_manage_utility.html`
- `red_hat_content/documentation/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_ee_setup_reference/aem-page/administer-assembly_controller_ee_setup_reference.html`
- `red_hat_content/documentation/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_inventory_templates/aem-page/administer-assembly_controller_inventory_templates.html`

```html
<article role="article">
  <article class="nested0" id="controller-instance-groups">
    <h1 class="title topictitle1" id="ariaid-title1">Instance groups</h1>
    ...
    <article class="topic task nested1" id="controller-create-instance-group">
      <h2 class="title topictitle2" id="ariaid-title2">Create an instance group</h2>
      ...
    </article>
  </article>
</article>
```

### Pattern 2: Flat sections

Simpler documents omit nested articles and use `<section>` elements directly.
Headings use the `sectiontitle` class. The sections may or may not carry `id`
attributes.

Example files:
- `red_hat_content/documentation/red_hat_ansible_automation_platform/2.7/aap_26_2025_12_10/aem-page/aap_26_2025_12_10.html`
- `red_hat_content/documentation/red_hat_ansible_automation_platform/2.7/administer-assembly_automation_mesh_operator_aap/aem-page/administer-assembly_automation_mesh_operator_aap.html`
- `red_hat_content/documentation/red_hat_ansible_automation_platform/2.7/administer-background_task_processing_for_event_driven_ansible/aem-page/administer-background_task_processing_for_event_driven_ansible.html`

```html
<article role="article">
  <h1 class="title topictitle1" id="ariaid-title1">New features</h1>
  <div class="body refbody">
    <section class="section" id="doc-id___feature_one">
      <h2 class="title sectiontitle">Feature one</h2>
      ...
    </section>
    <section class="section" id="doc-id___feature_two">
      <h2 class="title sectiontitle">Feature two</h2>
      ...
    </section>
  </div>
</article>
```

### Mixed content

Some documents combine both patterns. A nested article may contain `<section>`
elements or `<div class="example">` elements with `sectiontitle` headings:

Example files:
- `red_hat_content/documentation/red_hat_ansible_automation_platform/2.7/administer-assembly_aap_backup/aem-page/administer-assembly_aap_backup.html`
- `red_hat_content/documentation/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_hosts/aem-page/administer-assembly_controller_hosts.html`
- `red_hat_content/documentation/red_hat_ansible_automation_platform/2.7/administer-assembly_ug_controller_instance_groups/aem-page/administer-assembly_ug_controller_instance_groups.html`

```html
<article class="nested1" id="controller-group-policies">
  <h2 class="title topictitle2" id="ariaid-title7">Define instance groups</h2>
  <div class="body refbody">
    <section class="section" id="controller-group-policies___criteria">
      <h3 class="title sectiontitle">Criteria</h3>
      ...
    </section>
    <div class="example">
      <h3 class="title sectiontitle">Example</h3>
      ...
    </div>
  </div>
</article>
```

### Key conventions

- The outermost `<article role="article">` is a wrapper with no nesting level.
- `<body id="...">` provides the document identifier when no `nested0` article
  exists.
- Only containers (`<article>`, `<section>`, `<div class="example">`) that carry
  an `id` attribute produce TOC entries. Containers without `id` are ignored.

## Structure of TOC JSON files

The generated TOC JSON is consumed by `mimir-parser.py` to split documents into
chunks. The top-level structure is:

```json
{
  "version": "1.1",
  "sections": [
    {
      "title": "Document title",
      "visible": true,
      "weight": 1,
      "urlFragment": "index",
      "anchor": null,
      "singlePageAnchor": null,
      "sections": [
        {
          "title": "Chapter title",
          "visible": true,
          "weight": 1,
          "urlFragment": "chapter-id",
          "anchor": null,
          "singlePageAnchor": "chapter-id",
          "sections": [...]
        }
      ]
    }
  ]
}
```

### Field descriptions

| Field | Description |
|---|---|
| `title` | Section heading text. |
| `visible` | Whether the section appears in navigation. `true` for levels 0--3, `false` for level 4+. |
| `weight` | 1-based position among siblings. |
| `urlFragment` | Page identifier for URL construction. For level 0--1 nodes, this is the node's own `id`. For deeper nodes, it is the nearest level-1 ancestor's `id`. |
| `anchor` | Fragment anchor within the page. `null` for level 0--1 nodes; the node's `id` for deeper nodes. |
| `singlePageAnchor` | The node's `id`, used by `mimir-parser.py` to match headings in the markdown file and to name output chunk files. |

### Root section

The root section always has `urlFragment: "index"` and `singlePageAnchor: null`.
It represents the document as a whole.

## How aem-toc-generator.py works

### Overview

The script is a two-phase pipeline:

1. **Parse**: `AEMHTMLParser` walks the HTML and builds a tree of
   `AEMArticleNode` objects.
2. **Generate**: `TOCGenerator` converts the node tree into Mimir-compatible
   TOC JSON.

### Parsing phase

`AEMHTMLParser` extends Python's `html.parser.HTMLParser` and processes tags
as they are encountered:

- **`<article class="nested{N}">`** -- Creates a node at the given nesting
  level. Level 0 becomes the root; deeper levels attach to their parent article
  or are deferred to `pending_articles` if no root exists yet.

- **`<section>` and `<div class="example">`** -- Creates a node one level
  below the enclosing article (or level 1 if at the top level). Tracked on
  `section_stack`. On the closing tag, nodes with a title are attached to the
  nearest enclosing article, the root, or deferred to `pending_sections`.

- **Heading tags (`<h1>`--`<h6>`)** -- If the heading class contains
  `topictitle` or `sectiontitle` and a node is pending, the heading text is
  collected. The title is assigned to the pending node only if the node has a
  non-empty `id`. This filters out anonymous structural headings (e.g.,
  "Procedure", "Before you begin") that lack identifiers.

- **Fallback root** -- When no `nested0` article exists, a root node is created
  from `<body id>` after parsing completes. Any pending sections and articles
  are then attached. The root title is extracted from the first `h1.topictitle`
  via regex fallback.

### Generation phase

`TOCGenerator.generate()` walks the node tree depth-first:

- The root node becomes the single top-level section with `urlFragment: "index"`.
- Each child is converted by `_build_section()`, which sets `urlFragment` and
  `anchor` based on nesting level and propagates the `chapter_id` (the nearest
  level-1 ancestor's `id`) to deeper nodes.
- `visible` is set to `true` for nodes at level 0--3 and `false` for level 4+.
- `weight` is assigned as the 1-based sibling index.

### Usage

```bash
# Single file
python scripts/aem-toc-generator.py -i path/to/file.html -o path/to/toc.json

# Batch: process all aem-page directories under a base directory
python scripts/aem-toc-generator.py --batch --base-dir red_hat_content/documentation/red_hat_ansible_automation_platform
```

In the Mimir pipeline (`mimir-parser.py`), the script is invoked automatically
for each AEM document directory found during archive extraction.

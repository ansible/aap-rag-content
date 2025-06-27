import json

import requests
from constants import UI_AWX_ROUTES, VLLM_API_KEY, VLLM_BASE_URL, VLLM_MODEL_NAME

# --- LLM Prompt Template ---
# (This remains the same as your latest version, which is very specific about output)
LLM_PROMPT_TEMPLATE = """
**LLM Prompt: Automated UI Element Linking in Documentation**

**Objective:**
Your primary task is to intelligently process a given "Document Section" by identifying phrases that describe user interface elements (such as page titles, button labels, navigational actions, or interactive tasks). For each such identified phrase, you must find the most semantically relevant UI route from a provided "List of UI Routes". Finally, you will replace the original phrase in the document with a markdown link, where the link text is the original phrase and the link URL is the ID of the matched UI route. The goal is to emulate a process of identifying the best match as if using cosine similarity between the textual phrase and the descriptive names of the UI routes.

**Inputs You Will Receive:**

1.  **`Document Section`**: This is the text content that requires processing. It may contain descriptions of steps, UI interactions, and references to system functionalities.
2.  **`List of UI Routes`**: This is a JSON-formatted list. Each item in the list is an object containing a single key-value pair.
    * The **key** is a descriptive name of a UI element, page, or action (e.g., "CreateUser," "OrganizationDetails," "Select the Organization to be assigned for this user").
    * The **value** is its corresponding unique UI route ID (e.g., "awx-create-user," "awx-organization-details," "awx-organization-add-users").
    * Example format: `[ {{"Descriptive Name 1": "route-id-1"}}, {{"Descriptive Name 2": "route-id-2"}}, ... ]`

**Step-by-Step Instructions for Transformation:**

1.  **Identify Target UI Phrases:**
    * Thoroughly read and analyze the `Document Section`.
    * Pinpoint and extract specific phrases that explicitly name or describe:
        * User interface elements (e.g., "Users page," "Edit button," "the User dialog").
        * Actions a user performs within the UI (e.g., "Click Create user," "Select the Organization to be assigned for this user," "review and modify the user's Teams").
        * References to specific sections/functionalities accessible through the UI.
    * Focus on phrases that represent a clear navigational target or an interactive element.

2.  **Semantic Matching with UI Route Descriptive Names:**
    * For each identified target phrase from the `Document Section`:
        * Your goal is to find the **best semantic match** for this phrase among the **descriptive names (keys)** provided in the `List of UI Routes`.
        * This involves understanding the meaning, intent, and context of the identified phrase and comparing it to the meanings of the descriptive names in the UI route list. Consider synonyms, related actions, and the overall purpose. Choose the descriptive name that most closely represents the function or UI element mentioned in the document phrase.
        * For example, the phrase "Select the Organization to be assigned for this user" should semantically match a route key like "OrganizationAddUsers" because the action implies adding a user to an organization. Similarly, "Click Create user" directly matches a key like "CreateUser".
        * Once you have identified the best matching descriptive name, retrieve its associated **UI route ID (value)**.

3.  **Construct and Replace with Markdown Link:**
    * In the `Document Section`, you will replace the *exact original identified phrase* with a markdown-formatted link.
    * The markdown link must strictly follow this format: `[original identified phrase](matched_ui_route_id)`
    * **Crucially**: Ensure that any punctuation (e.g., periods, commas) that was part of the original identified phrase is included *within* the square brackets `[]` of the markdown link text. For example, if the identified phrase is "Select the Organization to be assigned for this user.", the link text should be "Select the Organization to be assigned for this user.".

4.  **Preserve Unrelated Content:**
    * You must not alter any other parts of the `Document Section` that were not identified as target UI phrases for replacement.
    * Any existing markdown links (like the one to `docs.redhat.com` in the example), code blocks, or other formatting within the document that are not relevant to this task should be preserved in their original state.

5.  **Output:**
    * **CRITICAL INSTRUCTION: YOUR RESPONSE MUST BE *ONLY* THE MODIFIED `Document Section` TEXT. NOTHING ELSE. NO EXCEPTIONS.**
    * **ABSOLUTELY NO EXTRA TEXT: Do not include any introductory phrases, preambles, greetings, headings (like "Explanation:"), summaries, apologies, justifications, conversational filler, concluding remarks, end markers (like "END OF TRANSFORMED DOCUMENT SECTION"), or any other text whatsoever that was not part of the original `Document Section`.**
    * **The output MUST begin *exactly* with the first character of the (potentially modified) original `Document Section` and end *exactly* with its last character. Do not add any characters, including newlines, before the start or after the end of the processed document text.**
    * **The structural integrity, formatting, and overall length of the output should mirror the input `Document Section`, changed *only* by the specified markdown link replacements.**
    * **Failure to adhere to this strict output format will render the response unusable. Only the transformed document text is permitted. Re-read these output instructions carefully.**

**Illustrative Example (Based on User's Provided Scenario):**

* **Given `Document Section`:**
    ```
    To create a user in the Ansible AutomationTo create a user in the Ansible Automation Platform (AAP), follow these steps:

    1. Select the Organization to be assigned for this user. For information about creating a new organization, refer to [Creating an Organization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-create-organization)
    2. Click Create user

    Once the user is successfully created, the User dialog opens. Here, you can review and modify the user's Teams, Roles, Tokens, and other membership details.
    ```

* **Given `List of UI Routes` (excerpt relevant to the example):**
    ```json
    [
      {{"CreateUser": "awx-create-user"}},
      {{"OrganizationAddUsers": "awx-organization-add-users"}},
      {{"UserPage": "awx-user-page"}},
      {{"UserDetails": "awx-user-details"}},
      {{"Organizations": "awx-organizations"}},
      {{"CreateOrganization": "awx-create-organization"}}
    ]
    ```
    *(Note: The full list provided by the user would be used in a real scenario, this is just a snippet for the example's clarity).*

* **LLM's Internal Reasoning (Simplified):**
  1. **Identified Phrase 1:** "Select the Organization to be assigned for this user." (Note the period is part of the phrase as it's at the end of the sentence segment being considered for linking).
     * Semantic Analysis: This action describes assigning a user to an organization. It implies an interaction related to adding or associating users with organizations.
     * Matching: From the provided list, "OrganizationAddUsers" (key) is the strongest semantic match for the action of selecting an organization *for a user*.
     * Route ID: "awx-organization-add-users" (value).
     * Replacement: `[Select the Organization to be assigned for this user.](awx-organization-add-users)`
  2. **Identified Phrase 2:** "Create user"
     * Semantic Analysis: This is a direct and explicit action to create a new user.
     * Matching: "CreateUser" (key) is a direct and exact semantic match.
     * Route ID: "awx-create-user" (value).
     * Replacement: `[Create user](awx-create-user)`
  3. **Other content:**
     * The phrase "User dialog opens." is not transformed in the user's desired output. This implies it's either not considered an actionable link target in this context, or a sufficiently strong semantic match was not found/prioritized. The prompt should follow this example and not link phrases unless a clear, actionable UI element or navigation is described and a strong semantic match exists.
     * The existing link `[Creating an Organization](https://docs.redhat.com/...)` must be preserved.

* **Expected Output (as per user's desired outcome):**
    ```
    To create a user in the Ansible AutomationTo create a user in the Ansible Automation Platform (AAP), follow these steps:

    1. [Select the Organization to be assigned for this user.](awx-organization-add-users). For information about creating a new organization, refer to [Creating an Organization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-create-organization)
    2. Click [Create user](awx-create-user)

    Once the user is successfully created, the User dialog opens. Here, you can review and modify the user's Teams, Roles, Tokens, and other membership details.
    ```

---

**How to Use This Prompt with an LLM:**

When you provide this to an LLM, you will fill in the actual content for the `Document Section` and the `List of UI Routes`.

**`Document Section`:**
```
{PASTE_YOUR_DOCUMENT_SECTION_CONTENT_HERE}
```

**`List of UI Routes`:**
```json
{PASTE_YOUR_FULL_JSON_LIST_OF_UI_ROUTES_HERE}
```

**Expected Transformed `Document Section` (The LLM should output this):**
```
{{LLM_GENERATED_OUTPUT_WILL_APPEAR_HERE}}
```
**ULTRA-CRITICAL REMINDER: THE *ONLY* VALID OUTPUT IS THE MODIFIED `Document Section` TEXT. NO OTHER TEXT, MARKERS, OR EXPLANATIONS ARE PERMITTED. THE RESPONSE MUST BE *IDENTICAL* TO THE MODIFIED DOCUMENT SECTION.**
"""


TEST_PROMPT_TEMPLATE = """
You are a meticulous document transformation assistant specialized in updating Markdown (.md) documents.

Your task is to **only** update references to UI elements in the document using a list of UI route mappings. You must **not make any other changes** to the document. Follow the rules strictly:

---

## Inputs

1. **Document Text**: Provided in Markdown format.
2. **UI Route Mappings**: Provided as a JSON dictionary of key-value pairs, where:
   - The key is a UI concept (e.g., "Users", "ExecutionEnvironmentTemplates").
   - The value is the associated route slug (e.g., "awx-users", "awx-execution-environments-templates").

---

## Instructions

### 1. Link Replacement Only
- Parse the document line-by-line.
- Search for phrases that **semantically match** or **directly match** any of the UI route keys.
- Replace only those phrases with their corresponding markdown link using the exact key-to-link mapping.
- Only wrap a phrase with a **single, most contextually accurate** route match.
- **Do not embed multiple route slugs** into a single markdown link.
- Do **not reformat, bold, italicize, or rewrite** any part of the sentence.

### 2. Do Not Modify Existing Links
- If a line contains an existing markdown link (e.g., `[Authentication details](#gw-configure-auth-details)`), **do not update or replace** that link even if a UI route mapping matches it semantically.

### 3. Do Not Add Any New Content
- Absolutely do **not** add:
  - Notes, summaries, explanations, or footers (e.g., “Note: The response has been minimal...”).
  - Any mention or formatting block such as `markdown`, ` ```markdown`, or similar.
  - Lists, headers, keys, route explanations, or helper comments.
  - **Any text outside of the original document body**.

### 4. No Syntax Decorations
- Do not output any markdown fences like ``````markdown`, ` ```markdown`, or any code block wrapper.
- The returned output must be **plain Markdown** content, line-for-line.

### 5. Be Strict and Minimal
- Any part of the document that is not a link replacement **must remain byte-for-byte unchanged**.
- Do not change:
  - Capitalization
  - Spacing
  - Typography or style (e.g., converting to bold)
  - Grammar or punctuation

### 6. Output Format
- Return a single plain Markdown document.
- No code blocks, no YAML, no annotations, no tags.
- Just the minimally updated document in raw text.

---

## Examples

### Allowed Update:
- Input: `Create a new user or select an existing one.`
- With UI routes: `{ "Users": "awx-users", "UserPage": "awx-user-page" }`
- Output: `Create a new [user](awx-users) or select an [existing user](awx-user-page).`

### Forbidden Update:
- Input: `ClickFinishto continue.`
- Wrong: `Click [Finish](#) to continue.`
- Correct: Leave it unchanged.

### Forbidden Addition:
- `Note: The response has been minimal...`
- ` ```markdown` or `markdown:` or code fences
- List of route keys with generated examples

---
**How to Use This Prompt with an LLM:**

When you provide this to an LLM, you will fill in the actual content for the `Document Section` and the `List of UI Routes`.

**`Document Section`:**
```
{PASTE_YOUR_DOCUMENT_SECTION_CONTENT_HERE}
```

**`List of UI Routes`:**
```json
{PASTE_YOUR_FULL_JSON_LIST_OF_UI_ROUTES_HERE}
```

**Expected Transformed `Document Section` (The LLM should output this):**
```
{{LLM_GENERATED_OUTPUT_WILL_APPEAR_HERE}}
```
**ULTRA-CRITICAL REMINDER: THE *ONLY* VALID OUTPUT IS THE MODIFIED `Document Section` TEXT. NO OTHER TEXT, MARKERS, OR EXPLANATIONS ARE PERMITTED. THE RESPONSE MUST BE *IDENTICAL* TO THE MODIFIED DOCUMENT SECTION.

Return only the updated Markdown document as plain text. Do not include headers, footers, logs, or explanations.
"""


def read_markdown_file(filepath: str) -> str | None:
    """Reads content from a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return None

def write_markdown_file(filepath: str, content: str):
    """Writes content to a markdown file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully wrote processed content to {filepath}")
    except Exception as e:
        print(f"Error writing file {filepath}: {e}")

def chunk_markdown_content(markdown_text: str, max_chunk_size_chars: int = 3000) -> list[str]:
    """
    Chunks markdown text into manageable parts based on paragraphs.
    Tries to keep chunks under max_chunk_size_chars, but a single paragraph
    exceeding this size will become its own chunk.
    Args:
        markdown_text: The full markdown text.
        max_chunk_size_chars: The target maximum character size for a chunk.
    Returns:
        A list of markdown text chunks.
    """
    if not markdown_text:
        return []

    lines = markdown_text.splitlines(keepends=True)
    chunks = []
    current_chunk_lines = []
    current_chunk_size = 0
    in_code_block = False

    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
        # If adding this line exceeds max size AND we're not in a code block
        # AND current_chunk is not empty, then finalize current_chunk.
        if (current_chunk_size + len(line) > max_chunk_size_chars and
                not in_code_block and current_chunk_lines):
            chunks.append("".join(current_chunk_lines))
            current_chunk_lines = []
            current_chunk_size = 0
        current_chunk_lines.append(line)
        current_chunk_size += len(line)

    # Add any remaining lines as the last chunk
    if current_chunk_lines:
        chunks.append("".join(current_chunk_lines))

    # Filter out empty or whitespace-only chunks that might have been created
    return [chunk for chunk in chunks if chunk.strip()]


def format_llm_request_content(document_section_content: str, ui_routes_list_data: list) -> str:
    """
    Formats the LLM prompt by inserting the document section and UI routes list.
    (Identical to previous version)
    """
    ui_routes_json_string = json.dumps(ui_routes_list_data, indent=2)

    formatted_prompt = TEST_PROMPT_TEMPLATE.replace(
        "{PASTE_YOUR_DOCUMENT_SECTION_CONTENT_HERE}",
        document_section_content
    )
    formatted_prompt = formatted_prompt.replace(
        "{PASTE_YOUR_FULL_JSON_LIST_OF_UI_ROUTES_HERE}",
        ui_routes_json_string
    )
    formatted_prompt = formatted_prompt.replace("{{", "{").replace("}}", "}")
    return formatted_prompt

def query_vllm_model(
    prompt_content: str,
    base_url: str = VLLM_BASE_URL,
    model_name: str = VLLM_MODEL_NAME,
    api_key: str = VLLM_API_KEY,
    temperature: float = 0.0,
    max_tokens: int = 2048 # Increased default, will be adjusted per chunk
) -> str | None:
    """
    Sends a prompt to a vLLM model (via OpenAI-compatible API) and returns the response.
    (Identical to previous version, but max_tokens might be adjusted per call)
    """
    url = base_url
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json',
               'Authorization': f'Bearer {api_key}'}
    payload = {
        "model": model_name,
        "messages": [{
            "role": "system",
            "content": "You are Granite, developed by IBM. You are a helpful AI assistant."
        },
        {
            "role": "user",
            "content": prompt_content
        }
        ]
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print("--- Received response from vLLM ---", response)
    if response.status_code == 200:
        print("Success.")
        resp_value = response.json()
        return resp_value['choices'][0]['message']['content'].split('\n\nIn this example')[0]
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    """
    Main function to process a full markdown file.
    """
    print("Starting UI Element Linking Script for Markdown File...")

    # --- Configuration for File Processing ---
    input_markdown_filepath = "/Users/sjaiswal/Sumit/wisdom/chatbot/POC/test_chatbot_streaming/red_hat_content/documentation/red_hat_ansible_automation_platform/2.5/access_management_and_authentication/single-page/048256f59b95ce97da4376d3955b9b6c.md"
    output_markdown_filepath = "/Users/sjaiswal/Sumit/wisdom/chatbot/POC/test_chatbot_streaming/red_hat_content/documentation/red_hat_ansible_automation_platform/2.5/access_management_and_authentication/single-page/output_linked_048256f59b95ce97da4376d3955b9b6c.md"

    max_chars_per_chunk = 3000

    # --- Load UI Routes (example, replace with your actual list) ---
    ui_routes_list = UI_AWX_ROUTES

    # 1. Read the input markdown file
    print(f"\n--- Reading Markdown File: {input_markdown_filepath} ---")
    markdown_content = read_markdown_file(input_markdown_filepath)
    if markdown_content is None:
        print("Exiting due to file read error.")
        return

    # 2. Chunk the markdown content
    print(f"\n--- Chunking Markdown Content (Max Chars/Chunk: {max_chars_per_chunk}) ---")
    chunks = chunk_markdown_content(markdown_content, max_chars_per_chunk)
    if not chunks:
        print("No content to process after chunking.")
        return
    print(f"Content split into {len(chunks)} chunks.")

    processed_chunks = []
    total_chunks = len(chunks)

    # 3. Process each chunk
    print("\n--- Processing Chunks with LLM ---")
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{total_chunks} (length: {len(chunk)} chars)...")
        estimated_output_max_tokens = len(chunk) + int(len(chunk) * 0.5) + 500 # Buffer for links and prompt overhead
        # Cap at a reasonable max if needed, e.g., 4096, depending on model
        llm_max_tokens_for_chunk = min(estimated_output_max_tokens, 4096)


        formatted_prompt = format_llm_request_content(chunk, ui_routes_list)
        try:
            llm_output = query_vllm_model(
                formatted_prompt,
                max_tokens=llm_max_tokens_for_chunk, # Adjust max_tokens based on chunk
                temperature=0.0 # Keep deterministic
            )
            if llm_output:
                processed_output = llm_output.strip()
                # Fallback post-processing for unwanted markers (should ideally be prevented by prompt)
                unwanted_markers = ["END OF TRANSFORMED DOCUMENT SECTION"]
                for marker in unwanted_markers:
                    if processed_output.endswith(marker):
                        processed_output = processed_output[:-len(marker)].strip()
                processed_chunks.append(processed_output)
                print(f"Chunk {i+1}/{total_chunks} processed.")
            else:
                print(f"Warning: Failed to get LLM response for chunk {i+1}. Using original chunk.")
                processed_chunks.append(chunk) # Fallback to original chunk if LLM fails
        except ConnectionError as ce:
            print(f"Connection error while processing chunk {i+1}: {ce}")
            processed_chunks.append(chunk)
            continue
        except Exception as e:
            print(f"Error processing chunk {i+1}: {e}")
            processed_chunks.append(chunk)
            continue
    # 4. Reconstruct the document
    print("\n--- Reconstructing Document ---")
    final_markdown_content = "\n\n".join(processed_chunks) # Join 
    final_markdown_content = "".join(processed_chunks)


    # 5. Write the output file
    print(f"\n--- Writing Processed Markdown to: {output_markdown_filepath} ---")
    write_markdown_file(output_markdown_filepath, final_markdown_content)

    print("\nScript finished.")

if __name__ == "__main__":
    # Before running:
    # 2. Ensure your vLLM server is running and accessible.
    # 3. Update VLLM_BASE_URL and VLLM_MODEL_NAME at the top of the script.
    # 4. Create an 'input.md' file in the same directory or update 'input_markdown_filepath'.
    # 5. AWX 'ui_routes.json' or define 'ui_routes_list' directly.

    main()

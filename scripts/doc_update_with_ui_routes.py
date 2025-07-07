"""This module processes a markdown document.

To convert specific UI navigation-instructions into markdown links using provided AWX UI routes.
"""

import argparse
import difflib
import os
import re
from typing import List, Optional, Tuple

import requests
from constants import UI_AWX_ROUTES, UI_EDA_ROUTES, UI_HUB_ROUTES
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Constants
VLLM_BASE_URL = os.environ.get("VLLM_BASE_URL")
VLLM_MODEL_NAME = os.environ.get("VLLM_MODEL_NAME")
VLLM_API_KEY = os.environ.get("VLLM_API_KEY")

# Pre-compiled regex patterns for performance optimization
_COMPILED_PATTERNS = {
    'markdown_links': re.compile(r'\[(.*?)\]\(.*?\)'),
    'punctuation': re.compile(r'[,.()\[\]"]'),
    'whitespace': re.compile(r'\s+'),
    'route_links': re.compile(r'\[.*?\]\(((awx|eda|hub)-[^)]+)\)'),
    'nav_panel': re.compile(r'From the navigation panel,\s+select([A-Z][a-zA-Z\s&→]+(?:→[A-Z][a-zA-Z\s&]+)*)'),
    'select': re.compile(r'(?<!\S)select([A-Z][a-zA-Z\s&→]+(?:→[A-Z][a-zA-Z\s&]+)*)'),
    'click': re.compile(r'(?<!\S)Click\s*([A-Z][a-zA-Z\s&]+)'),
    'page': re.compile(r'the\s+([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*)\s+page'),
    'navigate': re.compile(r'[Nn]avigate to (?:the\s+)?([A-Z][a-zA-Z\s&]+)'),
    'goto': re.compile(r'[Gg]o to (?:the\s+)?([A-Z][a-zA-Z\s&]+)'),
    'access': re.compile(r'[Aa]ccess (?:the\s+)?([A-Z][a-zA-Z\s&]+)'),
    'open': re.compile(r'[Oo]pen (?:the\s+)?([A-Z][a-zA-Z\s&]+)'),
    'activate': re.compile(r'[Aa]ctivate (?:the\s+)?([A-Z][a-zA-Z\s&]+)'),
    'create_rulebook': re.compile(r'[Cc]reate (?:a\s+)?[Rr]ulebook\s+([A-Z][a-zA-Z\s&]+)'),
    'view': re.compile(r'[Vv]iew (?:the\s+)?([A-Z][a-zA-Z\s&]+)'),
    'upload': re.compile(r'[Uu]pload (?:the\s+)?([A-Z][a-zA-Z\s&]+)'),
    'import': re.compile(r'[Ii]mport (?:the\s+)?([A-Z][a-zA-Z\s&]+)'),
    'publish': re.compile(r'[Pp]ublish (?:the\s+)?([A-Z][a-zA-Z\s&]+)')
}

# Global TF-IDF vectorizer for performance
_tfidf_vectorizer = None

def get_tfidf_vectorizer():
    """Get or create a shared TF-IDF vectorizer for performance."""
    global _tfidf_vectorizer
    if _tfidf_vectorizer is None:
        _tfidf_vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    return _tfidf_vectorizer

# --- Helper Functions ---

def calculate_text_similarity(text1: str, text2: str) -> float:
    """Calculate text similarity between two strings using cosine similarity.

    Returns a float between 0 and 1, where 1 means identical.
    """
    # Remove markdown link syntax for comparison purposes
    def normalize_for_comparison(text):
        # Use pre-compiled patterns for better performance
        text = _COMPILED_PATTERNS['markdown_links'].sub(r'\1', text)
        text = _COMPILED_PATTERNS['punctuation'].sub(' ', text)
        text = _COMPILED_PATTERNS['whitespace'].sub(' ', text).strip().lower()
        return text

    text1_normalized = normalize_for_comparison(text1)
    text2_normalized = normalize_for_comparison(text2)

    # Handle empty strings to prevent vectorizer errors
    if not text1_normalized.strip() or not text2_normalized.strip():
        return 0.0

    # Use shared vectorizer for better performance
    try:
        vectorizer = get_tfidf_vectorizer()
        tfidf_matrix = vectorizer.fit_transform([text1_normalized, text2_normalized])
        cos_similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return cos_similarity_score
    except Exception as e:
        print(f"Error calculating cosine similarity: {e}")
        # Fall back to SequenceMatcher if TF-IDF fails
        differ = difflib.SequenceMatcher(None, text1_normalized, text2_normalized)
        return differ.ratio()

def read_markdown_file(filepath: str) -> str | None:
    """Content read from a markdown file."""
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
    """Content write to a markdown file.

    If the file does not exist, it will be created.
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully wrote processed content to {filepath}")
    except Exception as e:
        print(f"Error writing file {filepath}: {e}")

def validate_and_filter_routes(ui_routes_list: list) -> list:
    """Validate, filter, and prioritize UI routes.

    Works with AWX, EDA, and HUB routes.
    """
    all_routes = []

    for route in ui_routes_list:
        if isinstance(route, dict):
            # For routes format: {"RouteKey": "route-id"}
            for name, route_id in route.items():
                if isinstance(route_id, str) and len(route_id) > 4:
                    # Identify route type based on prefix
                    route_type = "unknown"
                    if route_id.startswith("awx-"):
                        route_type = "awx"
                    elif route_id.startswith("eda-"):
                        route_type = "eda"
                    elif route_id.startswith("hub-"):
                        route_type = "hub"
                    elif route_id.startswith("hub") or route_id == "hub":
                        # Special case for just "hub"
                        route_type = "hub"

                    # Only exclude obviously fake ones
                    fake_indicators = ["example", "test", "fake", "dummy"]

                    if not any(indicator in route_id.lower() for indicator in fake_indicators):
                        # Store the route with type information
                        all_routes.append({
                            "name": name,
                            "route_id": route_id,
                            "route_type": route_type
                        })
    # Create priority tiers based on route type
    priority_routes = categorize_routes_by_priority(all_routes)

    print(f"Filtered routes: {len(ui_routes_list)} -> {len(all_routes)} valid routes")
    tiers = count_routes_by_tier(priority_routes)
    print(f"Tier 1: {tiers[1]}, Tier 2: {tiers[2]}, Tier 3: {tiers[3]}, Tier 4: {tiers[4]}, Other: {tiers[0]}")

    # Debug: show first few routes
    if priority_routes:
        print(f"First 5 routes: {[r['name'] + ': ' + r['route_id'] for r in priority_routes[:5]]}")

    return priority_routes

def categorize_routes_by_priority(routes: list) -> list:
    """Categorize routes into priority tiers based on heuristics.

    Works with AWX, EDA, and HUB routes.
    """
    # Enhanced categorization patterns that work across all route types
    categorized_routes = []

    for route in routes:
        if not isinstance(route, dict) or "route_id" not in route:
            continue

        route_id = route["route_id"]

        # Initialize with lowest priority
        tier = 5

        # High priority routes (Tier 1) - Major navigation and creation pages
        if any(keyword in route_id.lower() for keyword in ["dashboard", "home", "create", "add", "new", "launch"]):
            tier = 1
        # Important functional routes (Tier 2) - Action pages and main sections
        elif any(keyword in route_id.lower() for keyword in ["edit", "detail", "view", "manage", "list", "job", "template"]):
            tier = 2
        # Secondary pages (Tier 3) - Support pages and secondary functions
        elif any(keyword in route_id.lower() for keyword in ["config", "setting", "access", "credential", "inventory"]):
            tier = 3
        # Low priority (Tier 4) - Misc and tertiary pages
        elif any(keyword in route_id.lower() for keyword in ["help", "about", "log", "report"]):
            tier = 4

        # Add tier to route metadata
        route["tier"] = tier
        categorized_routes.append(route)

    return categorized_routes

def sort_routes_by_priority(routes: list) -> list:
    """Sort routes by priority tier and alphabetically within each tier.

    Works for any route type (AWX, EDA, HUB).
    """
    # First ensure all routes have a tier assigned
    categorized_routes = []

    for route in routes:
        if not isinstance(route, dict):
            # Handle non-dict route formats
            continue

        # Ensure routes have tier information
        if "tier" not in route:
            # Add tier information using categorization logic
            categorized_routes = categorize_routes_by_priority(routes)
            break
        else:
            categorized_routes = routes

    # Sort by tier (ascending), then by name (alphabetically)
    if categorized_routes:
        sorted_routes = sorted(
            categorized_routes,
            key=lambda x: (
                x.get('tier', 5),  # Default to lowest priority if missing
                x.get('name', '').lower() if isinstance(x.get('name', ''), str) else ''
            )
        )
        return sorted_routes

    return routes

def format_llm_request_content(document_section_content: str, ui_routes_list_data: list) -> str:
    """Format the request content for LLM processing.

    This is the core prompt template.
    """
    # Reformat UI routes to ensure they're formatted for the task
    formatted_routes = []
    valid_routes = validate_and_filter_routes(ui_routes_list_data)

    # Order routes by priority tier, then alphabetically within each tier
    priority_routes = sort_routes_by_priority(valid_routes)

    # Determine the predominant route type in this set
    route_types = {"awx": 0, "eda": 0, "hub": 0, "unknown": 0}
    for route in priority_routes:
        if "route_type" in route:
            route_type = route["route_type"]
            route_types[route_type] = route_types.get(route_type, 0) + 1

    # Get the predominant route type for customized prompts
    predominant_route_type = max(route_types.items(), key=lambda x: x[1])[0]
    print(f"Detected predominant route type: {predominant_route_type} (counts: {route_types})")

    # Limit routes to first 100 to avoid overwhelming the model
    display_routes = priority_routes[:100]

    print(f"Filtered routes: {len(ui_routes_list_data)} -> {len(valid_routes)} valid routes")
    tiers = count_routes_by_tier(priority_routes)
    print(f"Tier 1: {tiers[1]}, Tier 2: {tiers[2]}, Tier 3: {tiers[3]}, Tier 4: {tiers[4]}, Other: {tiers[0]}")
    print(f"First 5 routes: {[(route['name'] + ': ' + route['route_id']) for route in priority_routes[:5]]}")
    print(f"Limited routes to first {len(display_routes)} for LLM processing (includes all priority routes)")

    # Format routes list for display - include prefix
    for route in display_routes:
        formatted_routes.append(f"{route['name']}: {route['route_id']}")

    formatted_routes_str = "\n".join(formatted_routes)

    # Debug: print chunk and routes
    print(f"=== DOCUMENT CHUNK ({len(document_section_content)} chars) ===")
    print(document_section_content[:300] + "..." if len(document_section_content) > 300 else document_section_content)
    print(f"=== ROUTES AVAILABLE ({len(display_routes)}) ===")

    # Create a clear, directive prompt with explicit instructions
    # Adjust example routes to match the predominant route type
    route_prefix = {
        "awx": "awx-",
        "eda": "eda-",
        "hub": "hub-",
        "unknown": "awx-"  # Default to AWX if unknown
    }.get(predominant_route_type, "awx-")

    # Extract a few actual route examples from the valid routes for better instruction
    route_examples = []
    for route in priority_routes[:3]:
        if "name" in route and "route_id" in route:
            route_examples.append(f"'{route['name']}' → '{route['route_id']}'")

    prompt = f"""# TASK
        Your task is to convert specific UI navigation instructions in the document to markdown-formatted links using the provided UI routes.

        # INPUT FORMAT
        You will receive:
        1. A DOCUMENT section containing text with UI navigation instructions
        2. An AVAILABLE ROUTES section with route names and IDs

        # LINKING RULES
        Only convert these exact patterns to links, preserving the surrounding text exactly:

        1. Navigation panel selections:
        "select X" → "select [X]({route_prefix}route-id)"
        "selectX" → "select[X]({route_prefix}route-id)"
        Example: "selectAccess Management→Teams" → "select[Access Management→Teams]({route_prefix}teams)"

        2. Click actions:
        "Click X" → "Click [X]({route_prefix}route-id)"
        "ClickX" → "Click[X]({route_prefix}route-id)"
        Example: "ClickCreate team" → "Click[Create team]({route_prefix}create-team)"

        3. UI page references:
        "the X page" → "the [X]({route_prefix}route-id) page"
        Example: "the Users page" → "the [Users]({route_prefix}users) page"

        # CRITICAL REQUIREMENTS
        - Return ONLY the processed document with the navigation patterns converted to links
        - ONLY USE ROUTE IDs FROM THE PROVIDED LIST - DO NOT INVENT NEW ROUTES
        - DO NOT use generic routes like "awx-next", "awx-finish", "awx-save", or "awx-confirm" unless they are in the provided list
        - If you cannot find an exact match for a UI element in the routes list, leave it as plain text without a link
        - DO NOT include the available routes list in your response
        - DO NOT include any route listings, route IDs, or route names at the end of your response
        - DO NOT add explanatory text or modify any content
        - DO NOT add ANY notes, comments or explanations to the output
        - DO NOT include phrases like "The document has been updated" or "Note: The route ID for"
        - DO NOT include phrases like "NOTE:" or explanations about routes
        - DO NOT include phrases like "No matching route provided, text unchanged"
        - DO NOT include any sentences that begin with "Note:" or "The route ID for"
        - DO NOT add any sentences explaining why a route wasn't found or provided
        - DO NOT add any text like "No organization creation route was explicitly provided"
        - DO NOT add any explanations about routes not being in the available routes list
        - DO NOT change formatting, spacing, line breaks, or document structure
        - DO NOT link regular words/phrases that aren't navigation instructions
        - VERIFY that any route ID you use exists in the provided routes list
        - DO NOT invent route IDs that aren't in the list
        - ALWAYS use the EXACT route IDs as provided in the routes list
        - NEVER add text that wasn't in the original document
        - NEVER remove text that was in the original document
        - PRESERVE all line breaks exactly as they appear in the original
        - PRESERVE all paragraph structure exactly as in the original
        - All numbered lists, bullet points, and blocks starting with ###/## must start with NEW lines
        - If you cannot find a matching route, simply leave the text as is WITHOUT adding any explanation
        - NEVER include the available routes in your output
        - NEVER include route listings in your output
        - DO NOT include "# AVAILABLE ROUTES" or similar sections in your output
        - DO NOT include "route_id:" or "name:" lines in your output

        # DOCUMENT
        {document_section_content}

        # AVAILABLE ROUTES
        {formatted_routes_str}

        Remember: Return ONLY the processed document with no additional content. Only use route IDs that appear in the AVAILABLE ROUTES list.
    """

    return prompt

def query_vllm_model(
    prompt_content: str,
    base_url: str = VLLM_BASE_URL,
    model_name: str = VLLM_MODEL_NAME,
    api_key: str = VLLM_API_KEY,
    temperature: float = 0.0,
    max_tokens: int = 2048 # Increased default, will be adjusted per chunk
) -> str | None:
    """Prompt to a vLLM model.

    Returns the response.
    """
    url = base_url
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json',
               'Authorization': f'Bearer {api_key}'}

    # Add temperature and max_tokens to the payload
    payload = {
        "model": model_name,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "messages": [{
            "role": "system",
            "content": "You are Granite, developed by IBM. You are a helpful AI assistant that specializes in converting UI navigation instructions to markdown links."
        }, {
            "role": "user",
            "content": prompt_content
        }]
    }
    try:
        # Print debug info
        print(f"Sending request to LLM API at {base_url}")

        # Send the request
        response = requests.post(url, headers=headers, json=payload, timeout=60)

        # Print response status
        print(f"Received response from LLM API: {response.status_code}")

        # Check if the response is successful
        if response.status_code == 200:
            response_json = response.json()
            # Extract the content from the response
            if "choices" in response_json and len(response_json["choices"]) > 0:
                content = response_json["choices"][0]["message"]["content"]
                print(f"Processing LLM response ({len(content)} chars)")
                return content
            else:
                print(f"Invalid response format: {response_json}")
                return None
        else:
            # Handle error responses
            print(f"Error response: {response.status_code}")
            print(f"Response text: {response.text[:100]}...")

            # For debugging - print the full request that was sent
            print(f"Request URL: {url}")
            print(f"Request headers: {headers}")
            # Don't print the full payload as it might contain sensitive info
            print(f"Request payload model: {payload['model']}")
            print(f"Request payload temperature: {payload['temperature']}")

            return None
    except Exception as e:
        print(f"Exception during API call: {str(e)}")
        return None

def clean_llm_output(raw_output: str) -> str:
    """Clean LLM output to remove any unwanted content before validation.

    More aggressively removes route listings and explanatory text.
    """
    # Remove any heading sections that might be included from the prompt
    cleaned_output = re.sub(r'^#.*?\n', '', raw_output)  # Remove markdown headings
    cleaned_output = re.sub(r'^.*?DOCUMENT\s*\n', '', cleaned_output)  # Remove everything before DOCUMENT heading
    cleaned_output = re.sub(r'^.*?OUTPUT\s*\n', '', cleaned_output)  # Remove everything before OUTPUT heading

    # Remove route listings and debugging information - more aggressively
    cleaned_output = re.sub(r'# AVAILABLE ROUTES[\s\S]*?$', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'Available routes:[\s\S]*?$', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'name:.*?route_id:.*?$', '', cleaned_output, flags=re.MULTILINE)
    cleaned_output = re.sub(r'route_id:.*?$', '', cleaned_output, flags=re.MULTILINE)
    cleaned_output = re.sub(r'# ROUTE ID MAPPING.*?$', '', cleaned_output, flags=re.DOTALL)

    # Remove any section that starts with "name:" and contains multiple lines of route information
    cleaned_output = re.sub(r'name:[\s\S]*?route_id:[\s\S]*?$', '', cleaned_output, flags=re.MULTILINE)

    # Remove explanatory text and notes about routes - be more aggressive
    cleaned_output = re.sub(r'# CRITICAL:.*?\.', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'NOTE:.*?\.', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'Note:.*?\.', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'The document has been updated.*?\.', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'The provided routes.*?\.', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'No matching route.*?\.', '', cleaned_output, flags=re.DOTALL)

    # Remove any sections that look like route listings
    cleaned_output = re.sub(r'name: .*?\nname: .*?\n', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'route_id: .*?\nroute_id: .*?\n', '', cleaned_output, flags=re.DOTALL)

    # More aggressive removal of explanatory text about routes
    cleaned_output = re.sub(r'I could not find a route for.*?\.', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'Since there is no route for.*?\.', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'There is no route provided for.*?\.', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'No route was found for.*?\.', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'I did not find a matching route for.*?\.', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'I\'ve left this as plain text.*?\.', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'I couldn\'t find a route for.*?\.', '', cleaned_output, flags=re.DOTALL)
    cleaned_output = re.sub(r'I have not linked.*?\.', '', cleaned_output, flags=re.DOTALL)

    # Remove lines that contain route explanations
    lines = cleaned_output.split('\n')
    filtered_lines = []
    for line in lines:
        # Skip lines that are just route IDs or route names
        if re.match(r'^route_id: .*$', line.strip()) or re.match(r'^name: .*$', line.strip()):
            continue
        # Skip lines that are just route listings
        if re.match(r'^.*: awx-.*$', line.strip()) or re.match(r'^.*: eda-.*$', line.strip()) or re.match(r'^.*: hub-.*$', line.strip()):
            continue
        # Skip lines that explain route issues
        if any(phrase in line.lower() for phrase in [
            "no matching route",
            "could not find a route",
            "there is no route",
            "didn't find a route",
            "didn't find an exact match",
            "route id for",
            "route not found",
            "no route available",
            "left as plain text",
            "no specific route"
        ]):
            continue
        filtered_lines.append(line)

    cleaned_output = '\n'.join(filtered_lines)
    # Fix any double newlines that might have been created
    cleaned_output = re.sub(r'\n{3,}', '\n\n', cleaned_output)

    return cleaned_output

def validate_output_for_prompt_leakage(output: str) -> tuple[bool, str]:
    """Validate that the output doesn't contain prompt instructions or unwanted content.

    Returns (is_valid, reason) tuple.
    """
    # Critical patterns that should never appear in the output
    forbidden_phrases = [
        # Prompt section headers (be very precise)
        "# TASK",
        "# INPUT FORMAT",
        "# LINKING RULES",
        "# CRITICAL REQUIREMENTS",
        "# AVAILABLE ROUTES",

        # Instructions that might leak (be very precise)
        "Your task is to convert",
        "Return the EXACT document",
        "DO NOT add explanatory",
        "VERIFY that any route",
        "DO NOT invent route",
        "The provided document has been converted",

        # JSON artifacts
        "{\"",
        "\"}",
        "[{",
        "}]",
    ]

    # Check for forbidden phrases - be precise to avoid false positives
    for phrase in forbidden_phrases:
        if phrase in output:
            return False, f"Contains forbidden phrase: {phrase}"

    return True, "Valid"

def validate_changes_only_expected(original: str, processed: str, expected_patterns: list) -> tuple[bool, str]:
    """Validate that the processed text only has expected changes and no fabrication.

    More flexible validation that only checks for drastic content changes.
    """
    # If no patterns were found, the processed and original should be identical
    if not expected_patterns and processed != original:
        # Calculate similarity to be more lenient
        similarity = calculate_text_similarity(original, processed)
        if similarity > 0.95:  # If texts are at least 95% similar
            return True, "No patterns found but texts are very similar"
        return False, "Changes made when no UI patterns were detected"

    # If the processed text is identical to the original, but we found UI patterns
    if expected_patterns and processed == original:
        # Check if the original already contains markdown links - if so, it's valid
        if re.search(r'\[.*?\]\([^)]+\)', original):
            return True, "Original already contains markdown links"
        return False, "No changes made despite UI patterns detected"

    # Calculate text similarity for more lenient validation
    similarity = calculate_text_similarity(original, processed)

    # If the texts are very different, reject
    if similarity < 0.80:  # If texts are less than 80% similar
        return False, f"Processed text differs too much from original (similarity: {similarity:.1%})"

    # Check for markdown links in the processed text
    if expected_patterns and not re.search(r'\[.*?\]\([^)]+\)', processed):
        # No markdown links found - this is suspicious but not necessarily invalid
        # Some patterns might not have matching routes
        # Be lenient and accept if the text is otherwise very similar
        if similarity > 0.95:  # If texts are at least 95% similar
            return True, "No markdown links found but texts are very similar"
        return False, "No markdown links found in processed text"

    # All checks passed
    return True, "Changes appear to be valid"

def identify_ui_navigation_patterns(text: str) -> list:
    """Use regex to identify specific UI navigation patterns that should be converted.

    Returns list of (pattern_type, start_pos, end_pos, matched_text) tuples.
    Works with AWX, EDA, and HUB UI patterns.
    """
    patterns = []

    # Use pre-compiled patterns for better performance
    # Pattern 1: "From the navigation panel, selectMenuPath→SubMenu" (full context)
    for match in _COMPILED_PATTERNS['nav_panel'].finditer(text):
        patterns.append(('nav_panel', match.start(), match.end(), match.group(1).strip()))

    # Pattern 2: "selectMenuPath→SubMenu" (standalone)
    for match in _COMPILED_PATTERNS['select'].finditer(text):
        # Avoid duplicating patterns from navigation panel instructions
        if not any(p[0] == 'nav_panel' and p[2] >= match.start() for p in patterns):
            patterns.append(('select', match.start(), match.end(), match.group(1).strip()))

    # Pattern 3: "ClickButtonName" or "Click ButtonName"
    for match in _COMPILED_PATTERNS['click'].finditer(text):
        patterns.append(('click', match.start(), match.end(), match.group(1).strip()))

    # Pattern 4: "the PageName page" - detects UI page references
    for match in _COMPILED_PATTERNS['page'].finditer(text):
        patterns.append(('go_to', match.start(), match.end(), match.group(1).strip()))

    # Pattern 5: "Navigate to PageName" - detect navigation instructions
    for match in _COMPILED_PATTERNS['navigate'].finditer(text):
        patterns.append(('navigate', match.start(), match.end(), match.group(1).strip()))

    # Pattern 6: "Go to PageName" - detect navigation instructions
    for match in _COMPILED_PATTERNS['goto'].finditer(text):
        patterns.append(('goto', match.start(), match.end(), match.group(1).strip()))

    # Pattern 7: "Access PageName" - detect access instructions
    for match in _COMPILED_PATTERNS['access'].finditer(text):
        patterns.append(('access', match.start(), match.end(), match.group(1).strip()))

    # Pattern 8: "Open PageName" - detect open instructions
    for match in _COMPILED_PATTERNS['open'].finditer(text):
        patterns.append(('open', match.start(), match.end(), match.group(1).strip()))

    # EDA-specific patterns
    for match in _COMPILED_PATTERNS['activate'].finditer(text):
        patterns.append(('activate', match.start(), match.end(), match.group(1).strip()))

    for match in _COMPILED_PATTERNS['create_rulebook'].finditer(text):
        patterns.append(('create_rulebook', match.start(), match.end(), match.group(1).strip()))

    for match in _COMPILED_PATTERNS['view'].finditer(text):
        patterns.append(('view', match.start(), match.end(), match.group(1).strip()))

    # HUB-specific patterns
    for match in _COMPILED_PATTERNS['upload'].finditer(text):
        patterns.append(('upload', match.start(), match.end(), match.group(1).strip()))

    for match in _COMPILED_PATTERNS['import'].finditer(text):
        patterns.append(('import', match.start(), match.end(), match.group(1).strip()))

    for match in _COMPILED_PATTERNS['publish'].finditer(text):
        patterns.append(('publish', match.start(), match.end(), match.group(1).strip()))

    return patterns

def needs_llm_processing(chunk: str) -> bool:
    """Check if a chunk contains UI navigation patterns that need LLM processing.

    Returns True if patterns are found, False otherwise.
    """
    patterns = identify_ui_navigation_patterns(chunk)
    return len(patterns) > 0

def validate_awx_routes_exist(output: str, valid_routes: list) -> tuple[bool, str]:
    """Validate that all UI routes used in the output actually exist in the provided routes list.

    Works with AWX, EDA, and HUB routes.
    """
    # Extract all route links from the output using pre-compiled pattern
    ui_links = _COMPILED_PATTERNS['route_links'].findall(output)

    if not ui_links:
        return True, "No UI links found"
    # Extract just the route IDs
    ui_route_ids = [link[0] for link in ui_links]

    # Get list of valid route IDs
    valid_route_ids = set()
    for route in valid_routes:
        if isinstance(route, dict) and "route_id" in route:
            # Store the route_id as is
            route_id = route["route_id"]
            valid_route_ids.add(route_id)

            # For robustness, also add variants without prefix
            if route_id.startswith(("awx-", "eda-", "hub-")):
                # Extract the prefix
                prefix = route_id.split('-', 1)[0]
                # Add version without prefix
                valid_route_ids.add(route_id[len(prefix)+1:])
                # Handle the doubled prefix case
                valid_route_ids.add(f"{prefix}-{prefix}-{route_id[len(prefix)+1:]}")
        elif isinstance(route, str):
            parts = route.split(": ", 1)
            if len(parts) == 2:
                route_id = parts[1]
                valid_route_ids.add(route_id)

    # Check if all UI routes in the output exist in the valid routes
    invalid_routes = []
    for route in ui_route_ids:
        # Handle doubled prefix case (awx-awx-*, eda-eda-*, hub-hub-*)
        for prefix in ["awx", "eda", "hub"]:
            double_prefix = f"{prefix}-{prefix}-"
            if route.startswith(double_prefix):
                corrected_route = f"{prefix}-{route[len(double_prefix):]}"
                if corrected_route in valid_route_ids:
                    break
        else:  # This else belongs to the for loop - executes if no break occurred
            if route not in valid_route_ids:
                invalid_routes.append(route)

    if invalid_routes:
        # Find similar valid routes for better error messages
        error_msg = f"Contains invalid route IDs not in provided list: {', '.join(invalid_routes)}"
        similar_routes = []
        for invalid_route in invalid_routes:
            similar = find_similar_routes(invalid_route, list(valid_route_ids))
            if similar:
                similar_routes.append(f"For '{invalid_route}', did you mean: {', '.join(similar)}")

        if similar_routes:
            error_msg += f"\n   Similar valid routes: {'; '.join(similar_routes)}"

        # Find the text associated with each invalid route for better debugging
        route_texts = []
        for invalid_route in invalid_routes:
            match = re.search(r'\[(.*?)\]\(' + re.escape(invalid_route) + r'\)', output)
            if match:
                route_texts.append(
                    f"Found invalid route '{invalid_route}' with text: '{match.group(1)}'")

        if route_texts:
            error_msg += f"\n   {'; '.join(route_texts)}"

        return False, error_msg

    return True, "All UI routes are valid"

def validate_line_by_line(original_chunk: str, processed_chunk: str, valid_routes: list) -> str:
    """Validate UI routes on a line-by-line basis, preserving only lines with valid routes.

    Returns a cleaned version of the processed chunk with invalid routes replaced by original lines.
    """
    # Generate a comprehensive set of valid route IDs from all route types
    valid_route_ids = set()
    for route in valid_routes:
        if isinstance(route, dict) and "route_id" in route:
            # Store the route_id both with and without prefix
            route_id = route["route_id"]
            valid_route_ids.add(route_id)

            # Handle route prefixes (awx-, eda-, hub-)
            if route_id.startswith(("awx-", "eda-", "hub-")):
                # Extract the prefix
                prefix = route_id.split('-', 1)[0]
                # Add without prefix for flexibility
                valid_route_ids.add(route_id[len(prefix)+1:])
                # Also add with doubled prefix for detection of common errors
                valid_route_ids.add(f"{prefix}-{prefix}-{route_id[len(prefix)+1:]}")
        elif isinstance(route, str):
            parts = route.split(": ", 1)
            if len(parts) == 2:
                route_id = parts[1]
                valid_route_ids.add(route_id)
                # Handle prefixes in string format as well
                for prefix in ["awx", "eda", "hub"]:
                    if route_id.startswith(f"{prefix}-"):
                        valid_route_ids.add(route_id[len(prefix)+1:])
                        valid_route_ids.add(f"{prefix}-{route_id}")

    # Split both chunks into lines
    original_lines = original_chunk.split('\n')
    processed_lines = processed_chunk.split('\n')

    # Make sure we have enough lines in both chunks
    max_lines = max(len(original_lines), len(processed_lines))
    if len(original_lines) < max_lines:
        original_lines.extend([''] * (max_lines - len(original_lines)))
    if len(processed_lines) < max_lines:
        processed_lines.extend([''] * (max_lines - len(processed_lines)))

    # Process each line
    result_lines = []
    invalid_lines_count = 0

    for i in range(max_lines):
        original_line = original_lines[i] if i < len(original_lines) else ""
        processed_line = processed_lines[i] if i < len(processed_lines) else ""

        # Extract links with route IDs - check for all prefixes (awx-, eda-, hub-)
        route_pattern = r'\[.*?\]\(((awx|eda|hub)-[^)]+)\)'
        ui_links = re.findall(route_pattern, processed_line)

        if not ui_links:
            # No UI links, keep the processed line
            result_lines.append(processed_line)
            continue

        # Extract just the route IDs
        link_route_ids = [link[0] for link in ui_links]

        # Check if all UI links in this line are valid
        invalid_links = [link for link in link_route_ids if link not in valid_route_ids]

        if invalid_links:
            # Line contains invalid UI links, use the original line
            result_lines.append(original_line)
            invalid_lines_count += 1
        else:
            # All UI links are valid, keep the processed line
            result_lines.append(processed_line)

    if invalid_lines_count > 0:
        print(f"Found and replaced {invalid_lines_count} lines with invalid routes")

    # Join the lines back together
    return '\n'.join(result_lines)

def enhanced_validation_gate(original_chunk: str, processed_chunk: str,
                           expected_patterns: Optional[List] = None,
                           valid_routes: Optional[List] = None) -> Tuple[bool, str]:
    """Enhanced validation to ensure the LLM output is acceptable.

    Returns (is_valid, reason) tuple.
    """
    # First clean the LLM output to remove any unwanted content
    cleaned_output = clean_llm_output(processed_chunk)

    # Apply line-by-line validation to filter out lines with invalid routes
    if valid_routes:
        cleaned_output = validate_line_by_line(original_chunk, cleaned_output, valid_routes)

    # Check for prompt leakage
    is_valid_prompt, prompt_reason = validate_output_for_prompt_leakage(cleaned_output)
    if not is_valid_prompt:
        return False, prompt_reason

    # Check that changes are only where expected
    if expected_patterns is not None:
        is_valid_changes, changes_reason = validate_changes_only_expected(
            original_chunk, cleaned_output, expected_patterns
        )
        # Be more strict - only accept if changes are valid or very similar
        if not is_valid_changes:
            # Calculate text similarity
            similarity = calculate_text_similarity(original_chunk, cleaned_output)
            if similarity > 0.95:  # Increase threshold to 95% for stricter validation
                print(f"Changes validation failed but texts are {similarity:.1%} similar - accepting")
                return True, "Changes accepted based on high text similarity"
            return False, changes_reason

    # Check for valid routes - this is now stricter
    if valid_routes:
        is_valid_routes, routes_reason = validate_awx_routes_exist(cleaned_output, valid_routes)
        if not is_valid_routes:
            # Only accept if there are no markdown links at all
            if not re.search(r'\[.*?\]\(.*?\)', cleaned_output):
                print("  No markdown links found - accepting as no routes matched")
                return True, "No markdown links found - accepting"

            # If there are links but they're invalid, reject
            return False, routes_reason

    # All validations passed
    return True, "All validations passed"

def find_similar_routes(invalid_route: str, valid_routes: list) -> list:
    """Find valid routes that are similar to an invalid route.

    Works with any route type (AWX, EDA, HUB).
    """
    similar_routes = []

    # Extract the route type prefix (awx-, eda-, hub-)
    prefix = ""
    if invalid_route.startswith("awx-"):
        prefix = "awx-"
    elif invalid_route.startswith("eda-"):
        prefix = "eda-"
    elif invalid_route.startswith("hub-"):
        prefix = "hub-"

    # Extract the route ID without the prefix
    route_id = invalid_route
    if prefix:
        route_id = invalid_route[len(prefix):]

    # Look for valid routes with similar IDs
    for valid_route in valid_routes:
        # Handle both string and dict route formats
        if isinstance(valid_route, dict) and "route_id" in valid_route:
            valid_id = valid_route["route_id"]
            valid_name = valid_route.get("name", "")

            # Check similarity with and without prefix
            if (route_id.lower() in valid_id.lower() or 
                valid_id.lower() in route_id.lower() or
                route_id.lower() in valid_name.lower() or
                valid_name.lower() in route_id.lower()):
                similar_routes.append(valid_id)
        elif isinstance(valid_route, str):
            if route_id.lower() in valid_route.lower() or valid_route.lower() in route_id.lower():
                similar_routes.append(valid_route)

    # Return at most 3 similar routes
    return similar_routes[:3]

def count_routes_by_tier(routes: list) -> dict:
    """Count how many routes are in each tier.

    Returns a dictionary with tier numbers as keys and counts as values.
    """
    tier_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    for route in routes:
        if not isinstance(route, dict):
            tier_counts[0] += 1
            continue

        tier = route.get('tier', 5)  # Default to tier 5 if not set
        tier_counts[tier] += 1

    return tier_counts

def process_document(input_file_path: str, output_file_path: str, ui_routes_list_data: list) -> None:
    """Process a markdown document to add UI element links.

    returns None.
    This function reads a markdown file, splits it into chunks, identifies UI navigation patterns,
    queries a vLLM model to convert those patterns into markdown links, and writes the processed
    content to an output file. It also performs various validations to ensure the output is correct.
    """
    print(f"Processing document: {input_file_path}")
    print(f"Output will be written to: {output_file_path}")

    # Read the input markdown file
    input_content = read_markdown_file(input_file_path)
    if not input_content:
        print("Failed to read input file or file is empty.")
        return

    # Split the document into manageable chunks
    chunks = split_markdown_into_chunks(input_content, 1000)
    total_chunks = len(chunks)
    print(f"Split document into {total_chunks} chunks")

    # Track processing statistics
    chunks_with_patterns = 0
    successful_llm_chunks = 0
    skipped_chunks = 0
    rejected_chunks = 0
    failed_llm_calls = 0

    # Process each chunk
    processed_chunks = []

    for i, chunk in enumerate(chunks):
        print(f"--- Processing chunk {i+1}/{total_chunks} ---")

        # Identify UI navigation patterns
        patterns = identify_ui_navigation_patterns(chunk)

        if patterns:
            chunks_with_patterns += 1
            print(f"Found {len(patterns)} UI patterns: {', '.join([p[0] for p in patterns])}")

            # Get valid routes for this chunk (optimize by caching if needed)
            valid_routes = validate_and_filter_routes(ui_routes_list_data)

            # Format the prompt for the LLM
            prompt = format_llm_request_content(chunk, valid_routes)

            # Query the LLM
            print(f"🤖 Querying LLM for chunk {i+1}...")
            llm_response = query_vllm_model(prompt)

            if llm_response:
                # Clean the LLM response to remove any unwanted content
                cleaned_response = clean_llm_output(llm_response)

                # Calculate similarity between original and processed text - early exit if too low
                similarity = calculate_text_similarity(chunk, cleaned_response)
                if similarity < 0.8:
                    print(f"Similarity below threshold (80%): {similarity:.2%} - using original chunk")
                    processed_chunks.append(chunk)
                    rejected_chunks += 1
                    continue

                # Validate the LLM response
                is_valid, reason = enhanced_validation_gate(
                    chunk,
                    cleaned_response,
                    expected_patterns=patterns,
                    valid_routes=valid_routes
                )
                if is_valid:
                    # Additional validation to catch any remaining invalid routes
                    final_response = validate_line_by_line(chunk, cleaned_response, valid_routes)
                    processed_chunks.append(final_response)
                    successful_llm_chunks += 1
                else:
                    print(f"Chunk {i+1} failed validation: {reason}")
                    processed_chunks.append(chunk)  # Use original chunk
                    rejected_chunks += 1
            else:
                # LLM call failed, use original chunk
                print(f"Failed to get LLM response for chunk {i+1}. Using original chunk.")
                processed_chunks.append(chunk)
                failed_llm_calls += 1
        else:
            # No patterns found, use original chunk
            processed_chunks.append(chunk)
            skipped_chunks += 1

    # Reconstruct the document
    print("\n--- Reconstructing Document ---")
    output_content = "".join(processed_chunks)

    # Final cleanup to remove any remaining route listings or debugging information
    print("\n--- Performing Final Cleanup ---")
    output_content = clean_llm_output(output_content)

    # Write the output file
    print(f"\n--- Writing Processed Markdown to: {output_file_path} ---")
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(output_content)

    # Print statistics
    print("\n--- Processing Statistics ---")
    print(f"Total chunks: {total_chunks}")
    print(f"Chunks with UI patterns: {chunks_with_patterns}")
    print(f"Chunks successfully processed by LLM: {successful_llm_chunks}")
    print(f"Chunks skipped (no patterns): {skipped_chunks}")
    print(f"Chunks rejected by validation: {rejected_chunks}")
    print(f"Chunks with failed LLM calls: {failed_llm_calls}")

    print("\nScript finished successfully!!")

def split_markdown_into_chunks(content: str, chunk_size: int) -> List[str]:
    """Split markdown content into chunks of approximately the given size.

    This function attempts to split the content into chunks of approximately
    `chunk_size` characters trying to preserve markdown structure by splitting
    at paragraph boundaries. Improved to better handle chunk boundaries.

    Returns a list of content chunks.
    """
    # Try to split at paragraph boundaries
    paragraphs = re.split(r'\n\n+', content)

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        # If adding this paragraph would exceed chunk size and we already have content,
        # start a new chunk
        if len(current_chunk) + len(paragraph) > chunk_size and current_chunk:
            # Ensure we end with a newline to preserve structure
            if not current_chunk.endswith('\n\n'):
                current_chunk += '\n\n'
            chunks.append(current_chunk)
            current_chunk = paragraph + "\n\n"
        else:
            current_chunk += paragraph + "\n\n"

    # Add the last chunk if there's anything left
    if current_chunk:
        chunks.append(current_chunk)

    # Handle very large paragraphs that exceed chunk size by themselves
    final_chunks = []
    for chunk in chunks:
        if len(chunk) > chunk_size * 2:  # If chunk is more than double the target size
            # Split into smaller pieces, trying to keep sentences together
            sentences = re.split(r'(?<=[.!?])\s+', chunk)
            sub_chunk = ""
            for sentence in sentences:
                if len(sub_chunk) + len(sentence) > chunk_size and sub_chunk:
                    # Ensure we end with a newline to preserve structure
                    if not sub_chunk.endswith('\n\n'):
                        sub_chunk += '\n\n'
                    final_chunks.append(sub_chunk)
                    sub_chunk = sentence + " "
                else:
                    sub_chunk += sentence + " "
            if sub_chunk:
                final_chunks.append(sub_chunk)
        else:
            final_chunks.append(chunk)

    print(f"Split content into {len(final_chunks)} chunks (target size {chunk_size} chars)")
    return final_chunks

def main():
    """Main function to run the UI Element Linking Script for Markdown Files."""
    print("Starting UI Element Linking Script for Markdown File...")

    # --- Parse command line arguments ---
    parser = argparse.ArgumentParser(description='Process markdown files to add UI element links')
    parser.add_argument('--input', '-i', required=True, help='Input markdown file path')
    parser.add_argument('--output', '-o', help='Output markdown file path')
    parser.add_argument('--similarity-threshold', type=float, default=0.8,
                       help='Similarity threshold for accepting LLM output (0.0-1.0)')
    args = parser.parse_args()

    if VLLM_API_KEY is None:
        print("No API key provided, please set VLLM_API_KEY environment variable")
        return
    if VLLM_BASE_URL is None:
        print("No VLLM base URL provided, please set VLLM_BASE_URL environment variable")
        return
    if VLLM_MODEL_NAME is None:
        print("No VLLM model name provided, please set VLLM_MODEL_NAME environment variable")
        return
    # Choose which file to process
    input_file = args.input
    if input_file is None:
        print("No input file provided")
        return

    # Determine output file path
    if args.output:
        output_file = args.output
    else:
        # Auto-generate output path by adding "_llm_output_" before the extension
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}_llm_output_{ext}"

    # --- Determine which UI routes to use based on file path ---
    # Default to AWX routes
    ui_routes_to_use = UI_AWX_ROUTES

    # Check file path to determine appropriate routes
    if "eda" in input_file.lower() or "automation_decisions" in input_file.lower():
        print("Detected EDA document - using EDA routes")
        ui_routes_to_use = UI_EDA_ROUTES
    elif "hub" in input_file.lower() or "automation_content" in input_file.lower():
        print("Detected HUB document - using HUB routes")
        ui_routes_to_use = UI_HUB_ROUTES
    else:
        print("Using default AWX routes")

    # --- Process the document ---
    process_document(input_file, output_file, ui_routes_to_use)

if __name__ == "__main__":
    main()

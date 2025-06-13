import re

def ultra_clean_fleetstack_text(input_file='fleetstack_docs.txt', output_file='fleetstack_docs_ultra_cleaned.txt'):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned = []
    seen = set()
    
    skip_patterns = [
        r'^\s*$',                         # Empty lines
        r'^--- TEXT FROM:',              # Section separators
        r'^https?://',                   # Links
        r'^edit page$',                  # GitHub edit links
        r'^last updated.*$',             # Update timestamps
        r'^navigation$',                 # Navigation label
        r'^powered by.*$',               # Site footer
        r'^©.*$',                        # Copyright
        r'^fleetstack.*$',               # Brand name noise
        r'^next$', r'^previous$',        # Pagination
        r'^home$', r'^get started$',     # Sidebar menu
        r'^search$',                     # Search box
        r'^docs$', r'^community$',       # Top nav
        r'^\[\]$',                       # Stray UI elements
        r'^\|.*\|$',                     # Markdown table bars
        r'^[-=~_]{3,}$',                 # Decorative dividers
    ]

    for line in lines:
        line = line.strip()

        if any(re.match(pattern, line, re.IGNORECASE) for pattern in skip_patterns):
            continue

        # Filter out very short junk (single words or less than 5 characters, unless it's a heading)
        if len(line) < 5 and not re.match(r'^[A-Z][a-z]+(\s[A-Z][a-z]+)*$', line):
            continue

        # Remove duplicates while preserving order
        if line not in seen:
            seen.add(line)
            cleaned.append(line)

    # Write to final output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(cleaned))

    print(f"✅ Ultra-cleaned content saved to: {output_file}")

# Run the cleaner
ultra_clean_fleetstack_text()

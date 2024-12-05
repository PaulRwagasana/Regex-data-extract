#!/usr/bin/env python3
import re


text = """
contact Paul at paul@alu.com for any inquires, call +1-800-555-1234. Follow us on social media with #IceCodes  or #IceTech.
"""

patterns = {
    "emails": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    "phone_numbers": r'\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}',
    "hashtags": r'#\w+'
}

# Extract and display each type of information
for key, pattern in patterns.items():
    matches = re.findall(pattern, text)
    unique_matches = sorted(set(matches))
    print(f"Extracted {key.capitalize()}:")
    for match in unique_matches:
        print(match)
    print()


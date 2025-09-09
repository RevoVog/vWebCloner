#!/usr/bin/env python3
import requests
import sys
import os

if len(sys.argv) != 3:
    print("Usage: python3 download_html.py <URL> <output_file.html>")
    sys.exit(1)

url = sys.argv[1]
output_file = sys.argv[2]

try:
    # Fetch the HTML content
    response = requests.get(url)
    response.raise_for_status()  # Raise error if request failed

    # Save HTML to file
    with open(output_file, "w", encoding=response.encoding or "utf-8") as f:
        f.write(response.text)

    print(f"[✔] HTML source saved to {output_file}")

except requests.exceptions.RequestException as e:
    print(f"[✘] Error fetching the URL: {e}")
    sys.exit(1)

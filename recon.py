#!/usr/bin/env python3
"""
Simple recon: read URLs from a file and print HTTP status codes.
Usage: python3 scripts/recon.py urls.txt
"""

import sys
import requests

def check(url):
    try:
        r = requests.get(url, timeout=6, allow_redirects=True)
        print(f"{r.status_code}  {url}")
    except Exception as e:
        print(f"ERR      {url} -> {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/recon.py urls.txt")
        sys.exit(1)
    infile = sys.argv[1]
    try:
        with open(infile, "r") as f:
            for line in f:
                u = line.strip()
                if u:
                    check(u)
    except FileNotFoundError:
        print(f"File not found: {infile}")
        sys.exit(1)

if __name__ == "__main__":
    main()

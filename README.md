# bugbounty-notes

Personal bug bounty notes, payloads and simple recon scripts.

## Code of Conduct
Only test in-scope, follow VDP.

## Contents
- `notes.md` — learning notes, lab summaries, report templates
- `payloads.txt` — categorized payload snippets (XSS, SQLi, LFI, ...)
- `scripts/` — small helper scripts (recon, status checks)

## Run recon script (locally)
1. Create `urls.txt` with one URL per line.
2. Install requests: `pip install requests`
3. Run: `python3 scripts/recon.py urls.txt`

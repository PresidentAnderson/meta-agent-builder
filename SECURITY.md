## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

> **Note:** We recommend always running the latest **patch** release in each supported minor series.  
> If you’re on 5.0.x or anything older than 4.0, please plan an upgrade to avoid unpatched vulnerabilities.

---

## Reporting a Vulnerability

We take security seriously—and we want to hear from you if you find a flaw. Here’s how to engage:

1. **Send us an email**  
   - **Address:** `security@yourproject.org`  
   - **PGP key fingerprint (optional):**  
     ```
     3F2A 5B1C 9D8E 17F4 2A3B  9C0D 8E4F 1A2B 3C4D 5E6F
     ```
   - **Please include:**  
     - A clear description of the issue  
     - A minimal reproduction case or proof-of-concept  
     - Exact versions and environment details  
   - **Do not** file public issues or mention on Twitter until a fix is available.

2. **What to expect**  
   - **Acknowledgment** within **48 hours**.  
   - **Status updates** every **7 days** or upon major milestones (e.g. patch ready).  
   - We aim to ship a **fix within 30 days** of triage; high-severity issues may be faster.

3. **After disclosure**  
   - We’ll coordinate a public CVE assignment if applicable.  
   - A release announcement will include CVE details and upgrade instructions.

---

## Security Updates & Patch Release

- **Patch cadence:** Monthly for non-critical issues; out-of-band for high-severity fixes.  
- **How to upgrade:**  
  ```bash
  # npm example
  npm install yourproject@latest
  # or
  pip install --upgrade yourproject

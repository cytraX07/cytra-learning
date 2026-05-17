# 🛡️ Ethical Hacking Day 04: Vulnerability Scanning & Full Stack Recon

**Investigator:** Mr. Rupesh Kumar  
**Topics Covered:** Subdomain Discovery, Asset Validation, Tech Profiling & Automated Vulnerability Scanning  
**Status:** [x] Lab Tested

---

## 🔍 1. Subfinder (The Subdomain Hunter)

Agar target website ek bada ped (tree) hai, toh subdomains uski tehniyan (branches) hain.

- **Kyun:** Ye ek passive discovery tool hai. Ye target website ko scan karne ke bajaye public records (Search engines, APIs) se data nikalta hai, isliye aap detect nahi hote.
- **Hacker Logic:** 20+ sources se data fetch karta hai.
- **Basic Usage:**
  ```bash
  subfinder -d example.com -o subdomains.txt
  ```

---

## ⚡ 2. Naabu (Port Enumeration)

Port scanning ke liye Nmap toh hai hi, par jab hazaron subdomains ho, tab Naabu kaam aata hai.

- **Kyun:** Ye Go language mein likha gaya hai, jo isse extremely fast banata hai.
- **Function:** Ye check karta hai ki kaunse ports (80, 443, 8080, etc.) open hain.
- **Usage:**
  ```bash
  naabu -list subdomains.txt -o open_ports.txt
  ```

---

## 🛠️ 3. httpx-toolkit (Web Probing)

> **Note:** Aksar log `httpx` (Python library) aur `httpx-toolkit` (ProjectDiscovery tool) mein confuse hote hain. Hacking ke liye toolkit version best hai.

- **Problem Solver:** Sabhi subdomains "live" nahi hote. Ye tool verify karta hai ki kaunsa URL browser mein khulega aur uska status code (200 OK, 403 Forbidden) kya hai.
- **Pro Tip:** Isse hum "dead targets" ko filter kar dete hain.
- **Usage:**
  ```bash
  cat subdomains.txt | httpx-toolkit -sc -title -td
  ```

---

## 🏷️ 4. WhatWeb (Technological Fingerprinting)

Vulnerability dhoondne se pehle ye janna zaroori hai ki website kis technology par bani hai.

- **Concept:** Ye CMS (WordPress, Joomla), Web Servers (Nginx, Apache), aur Plugins ka pata lagata hai.
- **Kyun:** Agar WhatWeb bataye ki site "WordPress 4.7" use kar rahi hai, toh aapko turant pata chal jayega ki ye vulnerable hai.
- **Usage:**
  ```bash
  whatweb -i subdomains.txt
  ```

---

## 🎯 5. Nuclei (The Template King)

Nuclei aaj ke time ka sabse powerful automated scanner hai jo "Templates" par kaam karta hai.

- **Kyun:** Har roz naye exploits aate hain. Nuclei ki community unka `.yaml` template bana deti hai. Aapko bas wo template run karna hai.
- **Advanced Logic (Custom Templates):** Aap khud ke templates likh sakte ho specific bugs dhoondne ke liye.
- **Usage:**

  ```bash
  # Sabhi default templates run karne ke liye
  nuclei -l live_subs.txt

  # Specific category scan (e.g., Critical bugs)
  nuclei -l live_subs.txt -severity critical,high
  ```

---

## 🕵️ 6. Nikto (Web Server Auditor)

Nikto ek classic tool hai jo server-side vulnerabilities aur "dangerous" files ko dhoondta hai.

- **Primary Use:** Outdated server software aur default files (like `readme.html` ya `config.php.bak`) ko scan karna.
- **Warning:** Ye tool bohot noise create karta hai. Blue Teams/WAF ise turant pakad lete hain.
- **Usage:**
  ```bash
  nikto -h https://example.com -Tuning 4,5
  ```

---

## 📑 Tool Summary Table

| Tool              | Category   | Key Strengths                                       |
| :---------------- | :--------- | :-------------------------------------------------- |
| **Subfinder**     | Recon      | Sabse zyada subdomains nikalna (Passive).           |
| **Naabu**         | Scanning   | Super fast port scanning.                           |
| **httpx-toolkit** | Validation | Live web servers aur title filter karna.            |
| **WhatWeb**       | Analysis   | Website ka infrastructure (stack) pehchanna.        |
| **Nuclei**        | Pwnage     | Automated exploitation using YAML templates.        |
| **Nikto**         | Audit      | Server misconfigurations aur hidden files dhoondna. |

---

## 🧠 Investigator's Conclusion

> "Information Gathering sirf data jama karna nahi hai, balki sahi jagah (Dorks) aur sahi resource (OSINT.rocks) ka use karke 'Hidden Gems' dhoondna hai."

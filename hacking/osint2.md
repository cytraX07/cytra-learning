# 🛡️ Ethical Hacking Day 02: The Master Guide to Reconnaissance & OSINT

**Investigator:** Mr. Rupesh Kumar  
**Project:** Learning Cyber Security & Digital Footprinting  
**Date:** April 27, 2026

---

## 🌐 1. Fundamental Logic: Reconnaissance Kyun Zaruri Hai?

Hacking ki duniya mein "Information is Power" hoti hai. Reconnaissance (Recon) ka matlab hai apne target ke baare mein har wo choti jankari nikalna jo attack ke waqt kaam aa sake.

* **Kyun:** Bina recon ke attack karna andhere mein teer chalane jaisa hai.
* **Kya Nikalta Hai:** IP addresses, hidden subdomains, employee emails, server technologies, aur leaked documents.
* **Fayda:** Isse hacker ko target ki "Weak Link" (sabse kamzor kadi) ka pata chalta hai.

---

## 🛠️ 2. Professional Toolset (Deep Dive)

### 🦅 A. theHarvester
**Kyun use karein:** Ye tool "Open Source Intelligence" (OSINT) ke liye king hai. Iska kaam internet ke kone-kone se target ki details nikalna hai.

* **Kya Data Nikalta Hai:** Emails, Names, Subdomains, aur IP Addresses.
* **Installation:** Kali Linux mein pehle se hota hai. Agar na ho toh: `sudo apt install theharvester`.
* **Kaise Chalayein:**
  - `theHarvester -d target.com -l 500 -b all`
  - `-d`: Target domain.
  - `-l`: Kitne results dhoondne hain.
  - `-b`: Kahan se dhoondna hai (Google, Bing, LinkedIn, etc.).
* **Possible Problems:** Google ka IP block hona ya "Unrecognized arguments" error.
* **Fix:** Hamesha `-b` flag ke saath source specify karein aur limit (`-l`) set karein.

### 🕸️ B. SpiderFoot
**Kyun use karein:** Ye ek automatic framework hai jo 100 se zyada data sources ko ek saath scan karta hai.

* **Kya Data Nikalta Hai:** Phone numbers, Bitcoin addresses, DNS records, aur leaked API keys.
* **Installation:**
  1. `git clone https://github.com/smicallef/spiderfoot.git`
  2. `cd spiderfoot`
  3. `pip3 install -r requirements.txt`
* **Kaise Chalayein:**
  - `python3 sf.py -l 127.0.0.1:5001`
  - Phir browser mein `http://127.0.0.1:5001` kholo.
* **Possible Problems:** `lxml` installation fail hona.
* **Fix:** System libraries install karein: `sudo apt install libxml2-dev libxslt1-dev`.

### 🕷️ C. ParamSpider
**Kyun use karein:** Web application hacking mein parameters (`?id=`, `?page=`) dhoondna sabse zaruri hai. ParamSpider yahi kaam karta hai.

* **Kya Data Nikalta Hai:** Aise URLs jinme vulnerabilities (SQLi, XSS) hone ke chance hote hain.
* **Installation:**
  1. `git clone https://github.com/devanshbatham/ParamSpider`
  2. `pip install .`
* **Kaise Chalayein:** `python3 paramspider.py -d target.com`
* **Possible Problems:** "Results folder not found" error.
* **Fix:** Ye tool hamesha apne main folder ke andar `/results` folder banata hai, wahan check karein.

### 📁 d. Metagoofil (The Document Spy)
* **Kyun Use Karein:** Kisi company ki website par publicly available documents (PDF, Word, Excel) dhoond kar unka **Metadata** nikalne ke liye.
* **Kya Data Milega:** * **Usernames:** Files banane wale employees ke naam.
    * **Software Versions:** Kaunsa Office ya Adobe version use ho raha hai (Vulnerability dhoondne ke liye).
    * **Internal Paths:** Company ke servers aur folders ka internal rasta.
* **Kaise Install Karein:**
    ```bash
    sudo apt install metagoofil
    ```
* **Kaise Chalayein (Master Command):**
    ```bash
    metagoofil -d target.com -t pdf,doc,docx -l 50 -n 10 -o ./metagoofil_docs
    ```
    * `-d`: Target Domain.
    * `-t`: File extensions (pdf, doc, etc.).
    * `-l`: Kitne results search karne hain.
    * `-n`: Kitni files download karni hain.
    * `-o`: Output folder jahan files save hongi.
* **Possible Dikkat:** Google ki taraf se IP block hona agar zyada request bheinji jayein.
* **Solution:** Scan ke beech mein thoda delay rakhein ya VPN ka use karein.
---

## ⚠️ 3. Common Installation & Setup Errors

| Error Message                    | Kyun aata hai?                                                     | Sahi Solution (The Fix)                                                 |
| :-------------------------------:| :---------------------------------------------------------------:  | :---------------------------------------------------------------------: |
| **Failed to build lxml / wheel** | Python ko build karne ke liye C-compiler aur libraries nahi milti. | `sudo apt install build-essential libxml2-dev libxslt1-dev`             |
| **Command Not Found**            | Tool install toh hai par system path mein nahi hai.                | Folder ke andar jaakar (`cd`) usey `python3 tool_name.py` se chalayein. |
| **Permission Denied**            | Aapke paas file likhne ya execute karne ki power nahi hai.         | Command ke shuru mein `sudo` lagayein.                                  |

---

## 🏗️ 4. Advanced Concepts & Next Steps

### 🔍 Google Dorking
Google ko filter laga kar secret data nikalna.
* **Example:** `site:target.com filetype:env "DB_PASSWORD"` (Database passwords dhoondne ke liye).

### 🗡️ Katana (Waiting for Practice)
Ye ek fast crawler hai jo website ke har ek link ko scan karta hai.
* **Cammand:** `katana -u https://target.com`

---

## 🏠 Homework & Checklist
1. [ ] **DorksEye Setup:** GitHub se clone karke requirements finish karna.
2. [ ] **theHarvester Report:** Ek domain ka result `.html` format mein nikalna.
3. [ ] **SpiderFoot Scan:** Ek passive scan run karke interface ko samajhna.

---

> **Final Note:** Reconnaissance sirf tools chalana nahi hai, balki milne wale data ko samajhna hai. Troubleshoot karte waqt ghabrao mat, wahi asli hacking hai! 🛡️🚀


metagoofil
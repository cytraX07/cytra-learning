# 🛡️ Ethical Hacking: Password Cracking (Class 01) - Master Guide

**Investigator:** Mr. Rupesh Kumar  
**Project:** Learning Cyber Security & Password Auditing  
**Date:** May 9, 2026

---

## 🔐 1. Fundamental Logic: Password Cracking Kyun Zaruri Hai?

Security audit mein password cracking sirf password todne ke liye nahi, balki system ki mazbooti check karne ke liye hoti hai.

*   **Kyun:** Agar koi user `"123456"` ya `"admin"` jaisa password rakhta hai, toh system vulnerable hai.
*   **Kya Hota Hai:** Hum **hashes** (encrypted passwords) ko crack karke original plaintext nikalte hain.
*   **Fayda:** Isse pata chalta hai ki company ko kitni strong **"Password Policy"** ki zaroorat hai.

---

## 🛠️ 2. Professional Toolset: Crunch (The Pattern King)

### ⌨️ A. Crunch
**Kyun use karein:** Jab humein pata ho ki target ka password kisi specific pattern mein hai (jaise: Name + Year), toh Crunch custom wordlist banane ke liye best tool hai.  
**Installation:** `sudo apt install crunch` (Kali Linux mein pre-installed hota hai).


| Symbol    | Description                           |
| :-----:   | :---                                  |
| `@`       | Lowercase letters (a-z)               |
| `,`       | Uppercase letters (A-Z)               |
| `%`       | Numbers (0-9)                         |
| `^`       | Special Characters (!, @, #, etc.)    |

**Master Commands:**
*   **Simple List:** `crunch 4 8 0123456789 -o pwd.txt` (4 se 8 digit ke saare numbers).
*   **Pattern Based:** `crunch 10 10 -t admin%%%%% -o admin_list.txt` (Word 'admin' ke peeche 5 random numbers).
*   **Mixed Charset:** `crunch 8 8 -f /usr/share/crunch/charset.lst mixalpha-numeric -o mix.txt`.

### 👤 B. Personalized Tools (CUPP & BOPSCRK)
*   **CUPP (Common User Passwords Profiler):** Ye tool target se details leta hai (Name, DOB, Pet name) aur uske base par intelligent wordlist banata hai.
*   **BOPSCRK:** Advanced tool jo social media info ko use karke passwords predict karta hai.

---

## 📁 3. Important Wordlist Locations in Kali

Hacking ke liye hamesha khud ki list nahi banani padti; Kali mein industry-standard lists available hain:


| List Name | Path Location | Best For |
| :--- | :--- | :--- |
| **Rockyou** | `/usr/share/wordlists/rockyou.txt` | Common leaked passwords (Universal best). |
| **Nmap List** | `/usr/share/wordlists/nmap.lst` | Default software passwords. |
| **Dirb/Dirbuster** | `/usr/share/wordlists/dirb/` | Hidden website directories dhoondne ke liye. |

---

## ⚠️ 4. Common Setup & Execution Errors


| Error Message | Kyun aata hai? | Sahi Solution (The Fix) |
| :--- | :--- | :--- |
| `zsh: corrupt history file` | System galat shut down hone se history file kharab ho jati hai. | `rm ~/.zsh_history` aur naya terminal kholo. |
| `Permission Denied` | File generate karne ke liye root privileges nahi hain. | Command ke shuru mein `sudo` lagayein. |
| `Package wordlist is virtual` | `apt install wordlist` command galat hai. | Wordlists unzip karein: `gunzip /usr/share/wordlists/rockyou.txt.gz`. |

---
*Note: Use these techniques only on systems you have explicit permission to test.*

# 🛡️ ETHICAL HACKING: PASSWORD CRACKING (CLASS 02)

## 📑 Advanced Hash Decryption & Audit Guide

**👤 Investigator:** `Mr. Rupesh Kumar`  
**🎯 Project:** Cyber Security & Password Auditing  
**📅 Date:** May 10, 2026  
**🔐 Status:** [ SESSION 02 - ACTIVE ]

---

### 📂 TABLE OF CONTENTS

1. [Hash Identification](#-1-hash-identification)
2. [John The Ripper (JTR)](#-2-john-the-ripper)
3. [Hashcat (The GPU Beast)](#-3-hashcat-the-gpu-beast)
4. [Practical Training (THM)](#-4-tryhackme-practice)

---

### 🔍 1. HASH IDENTIFICATION (Pehchaan Kaun?)

_Password crack karne se pehle ye pata lagana zaruri hai ki wo kis algorithm (MD5, SHA-1, SHA-256, etc.) se encrypt hua hai._

- **🛠️ Primary Tool:** `hashid`
- **💡 Logic:** Bina algorithm jane hum tool ko sahi command nahi de sakte.

**🚀 Execution:**

```bash
# Basic Syntax
$ hashid <your_hash_here>

# Example Case
$ hashid 5d41402abc4b2a76b9719d911017c592
# Result: [MD5] or [SHA1]
```

---

### 🗡️ 2. JOHN THE RIPPER (JTR)

_John offline password cracking ka sabse famous aur reliable CPU-based tool hai._

- **✅ Pro:** Automatically hashes pehchaan leta hai.
- **📜 Syntax:** `john --wordlist=<path> --format=<type> <file>`

**🛠️ How to Use:**

1. Pehle apna hash ek text file mein save karo: `nano hash.txt`
2. Run the cracking command:

```bash
$ john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-md5 hash.txt
```

**🔓 Cracked Password Dekhne Ke Liye:**
_(Use this if the tool has already cracked the hash but isn't showing it again)_

```bash
$ john --show hash.txt
```

---

### 🏎️ 3. HASHCAT (The GPU Beast)

_Hashcat duniya ka sabse fast password cracker hai kyunki ye **GPU** ki power use karta hai._

- **🚀 Speed:** Iski speed John se kai guna zyada hoti hai.
- **⚙️ Syntax:** `hashcat -m <type_number> -a <mode> <hash_file> <wordlist>`

**🔑 Key Flags:**

| Flag | Name        | Details                                  |
| :--- | :---------- | :--------------------------------------- |
| `-m` | Module      | `0`=MD5, `100`=SHA1, `1400`=SHA256       |
| `-a` | Attack Mode | `0`=Straight (Wordlist), `3`=Brute Force |

**🚀 Example (MD5 Crack):**

```bash
$ hashcat -m 0 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```

---

### 🎯 4. TRYHACKME PRACTICE (The Battleground)

_Time to test these tools in a real environment._

- **📍 Platform:** [TryHackMe (THM)](https://tryhackme.com)
- **🏠 Recommended Room:** `"Crack the Hash"`

**⚔️ Your Mission Approach:**

1. **Join:** Room join karo aur task ka hash copy karo.
2. **Setup:** Kali mein file banao (`nano hash.txt`) aur paste karo.
3. **Identify:** `hashid` se algorithm check karo.
4. **Execute:** `rockyou.txt` ka use karke John ya Hashcat se usko tod do!

---

> [!TIP]
> **Final Note:** Hashcat bohot fast hai par commands complex hain. John slow hai par user-friendly hai. Apne machine ki power ke hisaab se choose karein. 🛡️🚀

---

**Prepared by:** _Mr. Rupesh Kumar (Professional Investigator)_

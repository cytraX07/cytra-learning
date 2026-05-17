# 🛡️ ETHICAL HACKING: SOCIAL MEDIA PHISHING

## 📑 Advanced Social Engineering & Credential Harvesting

**👤 Investigator:** `Mr. Rupesh Kumar`  
**🎯 Project:** Cyber Security & Phishing Awareness  
**📅 Date:** May 10, 2026  
**🔐 Status:** [ SESSION 03 - ACTIVE ]

---

### 📂 TABLE OF CONTENTS

1. [What is Social Media Phishing?](#-1-what-is-social-media-phishing)
2. [Zphisher & Cloudflare Error Fix](#-2-zphisher--tunneling-errors)
3. [Hider (Masking Links)](#-3-url-hider-link-masking)
4. [GoPhish Framework](#-4-gophish-the-enterprise-tool)

---

### 🎣 1. WHAT IS SOCIAL MEDIA PHISHING?

_Phishing ek Social Engineering attack hai jahan attacker kisi legitimate website ka ekdum real dikhne wala fake login page banata hai._

- **💡 Core Logic:** Isme hum kisi system ko hack nahi karte, balki insaan ke dimaag (**Psychology**) ko hack karte hain.
- **🎯 Goal:** Victim jaise hi us fake page par credentials dalta hai, wo attacker ke terminal par **Plain-text** mein save ho jata hai.

---

### 🛠️ 2. ZPHISHER & TUNNELING ERRORS

_Zphisher ek automated bash script hai jisme 30+ website templates hote hain._

**⚠️ The Problem (Cloudflare Error):** Link generate karte waqt Cloudflare aksar error deta hai ya tunnel turant ban ho jata hai.
**🔍 Reason:** Cloudflare security phishing patterns ko detect karke temporary links block kar deti hai.

**✅ How to Fix (Alternative Solutions):**

- **LocalXpose (Option 2/3):** Zphisher mein Cloudflare ki jagah LocalXpose select karein.
- **Ngrok (Manual):** Apna Ngrok token setup karein; ye sabse stable tunnel provide karta hai.
- **Localhost Testing:** Same WiFi par hone par Kali Linux ka IP use karke test karein.

---

### 🎭 3. URL HIDER (Link Masking)

_Phishing links (e.g., trycloudflare.com) suspicious lagte hain. Masking inhein disguise karti hai._

- **🛠️ Tools:** `Maskphish`, `Bit.ly`, `TinyURL`.
- **💡 Technique:** Trusted domains ko original link ke aage "overlay" ki tarah use karna.

**🚀 Masking Example:**

- **Original:** `https://xyz123.ngrok.io`
- **Masked:** `https://instagram.com-login-secure@xyz123.ngrok.io`
- _(Victim ko sirf 'instagram.com' dikhta hai aur wo trust kar leta hai.)_

---

### 🏢 4. GOPHISH (The Enterprise Tool)

_Jab poori company ko target karna ho, tab GoPhish Framework ka use hota hai. Ye ek professional Red-Teaming tool hai._

- **🌐 Interface:** Full Web-based GUI (Graphical User Interface).
- **🎯 Key Features:**
  - **Email Campaigns:** Hazaron logo ko ek saath target karna.
  - **Real-time Tracking:** Kisne email khola, click kiya ya password submit kiya—sab live dikhta hai.
  - **Reporting:** Client audit ke liye professional PDF reports generate karna.

---

> [!WARNING]  
> **AUDITOR'S NOTE:** Phishing links kisi bhi anjaan vyakti ko bhejna **ILLEGAL** hai. In tools ka istemaal sirf education, self-testing, ya written permission ke saath VAPT testing mein karein. 🛡️🚀

---

**Prepared by:** _Mr. Rupesh Kumar (Professional Investigator)_

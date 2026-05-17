# 🛡️ ETHICAL HACKING: CAMERA & LOCATION RECONNAISSANCE

## 📑 Advanced Device Hacking & Tunneling Fixes

**👤 Investigator:** `Mr. Rupesh Kumar`  
**🎯 Project:** Cyber Security & Phishing Awareness  
**📅 Date:** May 12, 2026  
**🔐 Status:** [ SESSION 04 - ACTIVE ]

---

### 📂 TABLE OF CONTENTS

1. [CamPhishing (Camera Hacking)](#-1-camphishing-camera-hacking)
2. [Storm-Breaker Installation & Fix](#-2-storm-breaker-installation--fix)
3. [Ngrok Setup & Error Fix](#-3-ngrok-setup--error-fix)
4. [Seeker (Location Phishing)](#-4-seeker-location-phishing)

---

### 📸 1. CAMPHISHING (Camera Hacking)

_Target ke device se bina uski jankari ke front camera se photo capture karna._

- **💡 Core Logic:** Fake templates (Festival wishes/YouTube links) ka use karna. Jaise hi victim camera permission **'Allow'** karta hai, background JavaScript photo capture kar leti hai.
- **🛠️ Popular Tools:** `CamPhish`, `SayCheese`.
- **⚠️ Requirement:** Ek local port (PHP server) aur internet hosting ke liye **Ngrok** ya **Cloudflare** tunnel.

---

### 🌩️ 2. STORM-BREAKER INSTALLATION & FIX

_Advanced OSINT tool jo camera, microphone, location aur device info nikalta hai._

**⚠️ The Problem:** Naye Kali Linux mein `pip` libraries install karte waqt "Externally managed environment" error aata hai.

**✅ How to Fix (Master Commands):**

```bash
# 1. Download & Enter Folder
git clone https://github.com/ultrasecurity/Storm-Breaker
cd Storm-Breaker

# 2. Base Tools Installation
sudo apt update && sudo apt install python3-pip php -y

# 3. Bypass Pip Environment Error
sudo pip3 install -r requirements.txt --break-system-packages

# 4. Launch Tool
sudo python3 st.py
```

---

### 🚇 3. NGROK SETUP & ERROR FIX

_Local Kali server ko global internet link (Tunneling) dena._

**📥 Perfect Installation:**

```bash
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar -xvzf ngrok-v3-stable-linux-amd64.tgz
sudo mv ngrok /usr/local/bin/
```

**🔍 Common Issues & Fixes:**

- **Auth Token Missing:** Dashboard se token copy karein:  
  `ngrok config add-authtoken <YOUR_TOKEN>`
- **Waiting for Connection:** Check karein ki background mein local server (e.g., PHP) chal raha hai ya nahi:  
  `php -S 127.0.0.1:8080`

---

### 📍 4. SEEKER (Location Phishing)

_High-accuracy GPS coordinates nikalna HTML5 Geolocation API ke zariye._

- **💡 Core Logic:** Ye IP-based location (jo aksar galat hoti hai) ki jagah device ke **GPS hardware** se exact coordinates leta hai.

**🚀 Installation & Run:**

```bash
# 1. Clone & Enter
git clone https://github.com/thewhiteh4t/seeker.git
cd seeker/

# 2. Automated Setup
sudo bash install.sh

# 3. Start Command
python3 seeker.py -t manual
```

---

> [!WARNING]  
> **AUDITOR'S NOTE:** Phishing links kisi bhi anjaan vyakti ko bhejna **ILLEGAL** hai. In tools ka istemaal sirf education, self-testing, ya written permission ke saath VAPT testing mein karein. 🛡️🚀

---

**Prepared by:** _Mr. Rupesh Kumar (Professional Investigator)_

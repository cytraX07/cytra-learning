# 🛡️ Ethical Hacking - Day 01: Environment Setup & Network Basics

**Investigator:** Mr. Rupesh Kumar  
**Date:** April 22, 2026  
**Status:** [x] Lab Ready | [x] Fundamentals Understood

---

## 🛠️ 1. The Hacker's Nest: Lab Environment Setup

Hacking shuru karne se pehle ek "Safe Zone" banana zaruri hai taaki hamari asli machine ko koi nuksan na ho.

### **Virtualization (The Safety Shield)**
* **VirtualBox:** Ye ek aisa software hai jo humein Windows ke andar ek aur computer (Virtual Machine) chalane ki permission deta hai.
* **Kyun:** Agar hum koi malware test karein ya koi galti ho jaye, toh virus hamari asli Windows (Host) tak nahi pahunch sakta.
* **Pro-Tip (Snapshots):** Kaam shuru karne se pehle "Snapshot" le lo. Agar system crash ho jaye, toh 1 click mein wapas pehle jaisa ho jayega.

### **The Operating Systems**
* **Kali Linux:** Hackers ka hathiyar. Isme 600+ tools pehle se aate hain.
* **Python 3:** Automation aur custom scripts likhne ke liye primary language.

---

## 🌐 2. Networking Fundamentals (Kyun aur Kab?)

Bina networking samjhe aap data ko intercept nahi kar sakte.

### **IP Address (The Logical ID)**
* **Kyun:** Ye network par aapke computer ka "Post Address" hai.
* **Hacker Logic:** IP milte hi hacker ko target ka network aur location ka andaza ho jata hai.
* **Command:** Linux mein `ip a` aur Windows mein `ipconfig`.

### **MAC Address (The Hardware Identity)**
* **Concept:** Ye har network card ka permanent "Fingerprint" hota hai.
* **Hacker Logic (MAC Spoofing):** `macchanger` tool se apni identity badalna taaki security filters ko dhoka diya ja sake.

[Image of OSI model layers explaining data flow between hardware and software]

---

## 🚀 3. Basic Kali Commands (The Entry Point)

Linux terminal hacker ka sabse bada dost hai. In commands par mastery zaruri hai:

| Command | Purpose | Hacker Logic |
| :--- | :--- | :--- |
| `whoami` | Identity Check | Ye check karna ki kya humein 'root' (Superuser) ki power mili hai ya nahi. |
| `ls -la` | Deep Visibility | Hidden files dhoondna (jaise `.bash_history` ya `.env`) jisme passwords ho sakte hain. |
| `pwd` | Navigation | File system mein "Lost" hone se bachne ke liye aur path set karne ke liye. |
| `sudo apt update` | Maintenance | Apne saare hacking tools ko latest version par rakhne ke liye. |

---

## 🧠 4. Summary & Safety Logic

* **Isolation:** Hamesha VM use karein.
* **Identity:** Apne IP aur MAC ko manage karna sikhein.
* **Persistence:** Linux commands ki practice karte rahein.

> **Investigator's Note:** "Setup sahi ho toh aadhi jung wahi jeeti jati hai. Lab ready hai, ab hunt shuru hoga." 🛡️🔥
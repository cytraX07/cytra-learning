# 🛡️ Ethical Hacking Day 03: Advance & Dark OSINT

**Investigator:** Mr. Rupesh Kumar  
**Topics Covered:** Automated Dorking, GHDB, & OSINT Frameworks  
**Status:** [x] Lab Tested

---

## 🔍 1. Google Dorking & GHDB (The Brain of OSINT)

Sirf Google par search karna kafi nahi hai, Google ko "hacker mode" mein use karna hi asli skill hai.

### **Google Hacking Database (GHDB)**

- **Kyun:** Ye ek aisi library hai jahan hackers ne pehle se bane-banaye "Dorks" (search queries) share kiye hain.
- **Logic:** Agar aapko kisi website ke admin panels ya leaked passwords dhoondne hain, toh aap seedha [Exploit-DB GHDB](https://www.exploit-db.com/google-hacking-database) par jaakar query copy kar sakte ho.

### **Automated Tool: Dorkseye**

- **Kyun:** Manual dorks likhne mein time lagta hai, Dorkseye ise automate kar deta hai.
- **Kya Nikalta Hai:** \* Sensitive Files (PDF, log, config)
  - Login Pages
  - Hidden Directories
- **Usage:** ```bash
  cd ~/tools/dorkseye
  python3 dorkseye.py
  ```

  ```

---

## 🕸️ 2. OSINT.rocks (The Missing Manual)

Video mein iska zikr tha par details kam thi, ye raha iska poora nichod:

- **Concept:** [OSINT.rocks](https://osint.rocks/) ek curated list hai un saare tools aur websites ki jo internet par "Digital Investigation" ke liye use hoti hain.
- **Kyun Use Karein:**
  - **Username Tracking:** Sherlock jaisa kaam online karta hai.
  - **Image OSINT:** Kisi photo se location nikalna.
  - **Domain Research:** Website ke purane records dekhna.
- **Hacker Logic:** Jab hamare Kali Linux ke tools block ho jate hain, tab hum in web-based frameworks ka use karte hain taaki hamara IP safe rahe.

---

## 🌑 3. Dark OSINT (Hidden Web)

Deep aur Dark web se data nikalna normal browsing se alag hai.

- **Tor Browser:** Dark web (.onion sites) ko access karne ka gateway.
- **Logic:** Dark web par aksar leaked databases aur hacking forums hote hain. OSINT ka matlab yahan ye hai ki bina apni identity reveal kiye (Anonymity) wahan se info nikalna.

---

## 🛠️ Updated Tool Table

| Tool / Resource | Category   | Primary Use Case                              |
| :-------------- | :--------- | :-------------------------------------------- |
| **Dorkseye**    | Automation | Google Dorks ko fast execute karna.           |
| **GHDB**        | Database   | Expert-level search queries (Dorks) dhoondna. |
| **OSINT.rocks** | Framework  | Har tarah ke OSINT tools ka collection.       |

---

## 🧠 Investigator's Conclusion

> **"Information Gathering sirf data jama karna nahi hai, balki sahi jagah (Dorks) aur sahi resource (OSINT.rocks) ka use karke 'Hidden Gems' dhoondna hai."**

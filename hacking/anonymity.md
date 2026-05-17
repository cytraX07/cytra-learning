# 🛡️ Master Notes: Digital Anonymity & Stress Testing

**Prepared by:** Mr. Rupesh Kumar (Professional Investigator)  
**Topics Covered:** Anonymity, SMS/Call Stress Testing, Messaging & Email  
**Subject:** Cybersecurity Lab - Anonymity Phase

---

## 1. Networking & Privacy (Core Concepts)

- **Anonymity:** Internet par apni pehchaan (Identity) aur location ko mask karna.
- **Tor (The Onion Router):** Ye aapke data ko multiple "layers" (nodes) se guzarta hai taaki koi ye na jaan sake ki data kahan se aa raha hai.

---

## 2. Primary Anonymity Tools

|    Tool Name    |        Feature        |                                                        How it Works (Serial-wise)                                                         |
| :-------------: | :-------------------: | :---------------------------------------------------------------------------------------------------------------------------------------: |
|  **Anonsurf**   |    System-wide Tor    | Ye aapke poore Operating System (Kali/Parrot) ke traffic ko Tor network par redirect kar deta hai. IP leak hone ka chance 0% ho jata hai. |
|   **Autotor**   | Automatic IP Switcher |              Ye har 30-60 seconds mein aapka Exit Node (IP address) badalta rehta hai. Isse tracking impossible ho jati hai.              |
| **Blacktel.io** |   Virtual Identity    |               Bina apni real SIM use kiye, ye aapko fake numbers aur virtual SMS service provide karta hai for OTP bypass.                |

---

## 3. SMS/Call Stress Testing (The "Bomb" Tools)

_In tools ka use ethical hacking mein server ki response capacity check karne ke liye hota hai._

1.  **T-Bomb:** Sabse popular tool jo API exploitation ka use karke bulk SMS aur calls bhejta hai.
2.  **Pandora Bomb:** _(Status: Installing)_ Ye T-Bomb ka advanced version hai. Isme multi-thread support hota hai jo faster attack simulation karta hai.
3.  **Devil S-Call:** Ye specific call bombing ke liye use hota hai jisme caller ID mask ho jati hai.

---

## 4. Communication Anonymity (Messaging & Email)

- **Anon SMS:** Bina apna personal number disclose kiye anonymous SMS bhejna. Iska use investigative work mein communication ko private aur untraceable rakhne ke liye hota hai.
- **Fake Mailer:** Iska use phishing simulations ke liye kiya jata hai. Aap kisi bhi dummy address se email bhej sakte ho.
- **Temp Mail:** 10-minute mail services jo testing ke waqt aapke real inbox ko spam se bachati hain.

---

_Generated for Professional Investigation Purposes._

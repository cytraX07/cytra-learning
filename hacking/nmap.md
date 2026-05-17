# 🛡️ Ethical Hacking Day 04: Nmap (Network Mapper) Master Class

**Investigator:** Mr. Rupesh Kumar  
**Topics:** Network Scanning, Port Discovery, & OS Detection  
**Practice Labs:** [TryHackMe](https://tryhackme.com) | [TryHackMe Access](https://tryhackme.com/access)

---

## 🔍 1. Basic & Discovery Scanning

Saamne wale network mein kaun zinda hai aur kaun nahi, ye check karne ke liye.

- **`nmap -help`**: Nmap ke saare commands aur usage ki list dekhne ke liye.
- **`nmap -sn 142.250.182.238/24`**: **Ping Scan**. Ye ports scan nahi karta, sirf ye batata hai ki network mein kitne hosts "Up" (zinda) hain.
- **`nmap 142.250.182.238`**: **Default Scan**. Sabse common 1000 ports ko scan karta hai.
- **`nmap -Pn 142.250.182.238`**: **No Ping Scan**. Agar target firewall ping block kar raha ho, toh ye command use karke direct scan kiya jata hai.

---

## ⚡ 2. TCP & UDP Scanning Techniques

Inse pata chalta hai ki connection kaise ban raha hai.

- **`nmap -sT 142.250.182.238`**: **TCP Connect Scan**. Full 3-way handshake karta hai. Reliable hai par target ke logs mein pakda ja sakta hai.
- **`nmap -sS 142.250.182.238`**: **Stealth Scan (SYN Scan)**. Half-open scan hai. Ye connection poora nahi karta, isliye "Stealthy" (chupa hua) mana jata hai.
- **`nmap -sU 142.250.182.238`**: **UDP Scan**. UDP ports (jaise DNS, DHCP) dhoondne ke liye use hota hai. Ye thoda slow hota hai.
- **`nmap -sA 142.250.182.238`**: **ACK Scan**. Ye check karta hai ki port firewall ke peeche hai ya nahi (Filtered vs Unfiltered).
- **`nmap -sW 142.250.182.238`**: **Window Scan**. TCP window field check karke open ports dhoondta hai (kuch specific systems par).

---

## 🛠️ 3. Service & OS Intelligence

System ke andar ki deep jankari nikalne ke liye.

- **`nmap -sV 142.250.182.238`**: **Version Detection**. Ye batata hai ki port par kaunsa software aur uska version (jaise Apache 2.4.1) chal raha hai.
- **`nmap -sV --version-intensity 5 142.250.182.238`**: Intensity badhane par Nmap zyada probes bhejta hai taaki sahi version ka pata chale (Scale 0-9).
- **`nmap -O 142.250.182.238`**: **OS Detection**. Target machine ka Operating System (Windows, Linux, etc.) dhoondne ke liye.
- **`nmap -A 142.250.182.238`**: **Aggressive Scan**. Is ek command mein OS detection, Version detection, Script scanning aur Traceroute—sab kuch ho jata hai.

---

## 🕵️ 4. Advanced & Stealth Options

Firewall bypass aur vulnerability detection ke liye.

- **`nmap -p 1-5000 142.250.182.238`**: **Port Range**. Sirf 1 se lekar 5000 tak ke ports scan karega.
- **`nmap -vv`**: **Very Verbose**. Scan ke waqt screen par zyada details dikhayega ki background mein kya chal raha hai.
- **`nmap --script vuln 142.250.182.238`**: **Vulnerability Script**. NSE (Nmap Scripting Engine) ka use karke target mein purani kamzoriyan dhoondta hai.
- **`nmap --spoof-mac 0 142.250.182.238`**: **MAC Spoofing**. Apne system ka MAC address badal kar scan karne ke liye taaki asli identity chupi rahe.

---

## 🚀 5. Missing & Professional Pro Commands

Ye wo commands hain jo ek expert hacker ki productivity 10x badha dete hain.

### **Timing & Performance (Scan Tez Karne ke Liye)**

- **`nmap -T4 142.250.182.238`**: **Timing Template**. T0 (slowest) se T5 (fastest) tak hota hai. `T4` professional scans ke liye best hai—fast aur reliable.
- **`nmap --top-ports 100 142.250.182.238`**: Sirf un **top 100 ports** ko scan karega jo internet par sabse zyada use hote hain. Full scan se bahut fast hai.

### **Output Management (Report Banane ke Liye)**

- **`nmap -oN scan_report.txt 142.250.182.238`**: Scan ke result ko ek normal **Text file** mein save karne ke liye.
- **`nmap -oX scan_report.xml 142.250.182.238`**: Result ko **XML** mein save karta hai. Ye tab kaam aata hai jab aapko data kisi doosre tool (jaise Metasploit) mein import karna ho.

### **Firewall Evasion (Darwaza Khatkhataye Bina Andar Dekhna)**

- **`nmap -f 142.250.182.238`**: **Fragment Packets**. Packets ko chhote tukdon mein tod deta hai taaki purane Firewalls aur IDS inhe pehchan na sakein.
- **`nmap -D RND:10 142.250.182.238`**: **Decoy Scan**. Target ko lagega ki 10 alag-alag IPs se scan aa raha hai. Aapka asli IP un 10 ke beech mein kahin chhupa rahega.
- **`nmap --source-port 53 142.250.182.238`**: Scan ko **Port 53 (DNS)** se bhejta hai. Bahut saare Firewalls DNS traffic ko bina check kiye aane dete hain.

### **Specific Information Gathering**

- **`nmap --iflist`**: Ye dekhne ke liye ki aapke Kali Linux mein kaunse network interfaces (eth0, wlan0) aur routes available hain.
- **`nmap -R 142.250.182.238`**: **Reverse DNS lookup**. IP se domain name nikalne ki koshish karta hai (agar available ho).
- **`nmap --traceroute 142.250.182.238`**: **Traceroute**. Target ke path se kaha se jaa rahega.

---

## 💡 Quick Reference Table

| Command | Purpose                      | Speed      |
| :------ | :--------------------------- | :--------- |
| `-sS`   | Stealthy & Fast              | High       |
| `-sV`   | Identifies Software Versions | Medium     |
| `-A`    | All-in-one Deep Scan         | Low (Slow) |
| `-Pn`   | Bypass Ping Blocks           | Medium     |

---

**Notes Ending:** Nmap ke baad agla step **Vulnerability Scanning** hota hai jahan hum in ports ki kamzoriyon ka faida uthate hain.

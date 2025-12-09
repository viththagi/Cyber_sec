# 🔐 Local Security Monitor
A beginner-friendly cybersecurity tool built in Python to monitor suspicious processes, 
network connections, and weak passwords. Designed as a practical cybersecurity learning project.

---

## 🧠 Features
✔ Detects suspicious processes  
✔ Flags suspicious external network connections  
✔ Checks password strength  
✔ Logs events to a security log file  
✔ Lightweight, cross-platform, and easy to extend  

---

## 🏗 Project Architecture
local-security-monitor/
│── monitor.py           → Main controller  
│── process_checker.py   → Process scanning module  
│── network_scanner.py   → Network monitoring module  
│── password_audit.py    → Password strength checker  
│── utils/logger.py      → Event logging utility  

---

## ⚙ Installation
Install dependencies:
pip install psutil

## 🚀 Future Improvements
- Email/Discord alerting  
- Monitoring CPU spikes for malware  
- Parsing Windows event logs  
- GUI dashboard  
- Hash comparison for file integrity  

---

## 📚 Learning Outcomes
This project demonstrates:
- Basic threat detection  
- Python system monitoring  
- Log-based security event tracking  
- Cybersecurity fundamentals  

---

## 👤 Author
Built as a practical cybersecurity mini-project after completing  
**"Practical Cybersecurity for IT Professionals" – LinkedIn Learning**.

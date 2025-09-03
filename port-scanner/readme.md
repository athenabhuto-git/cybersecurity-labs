# 🔐 Port Scanner

A simple Python-based port scanner that checks a target IP or hostname for open ports.  
This project is part of the **Cybersecurity Labs** collection.

---

## 🚀 Features
- Scan a range of ports on any IP/hostname.
- Detect open ports using TCP connection.
- Lightweight and easy to run.

---

## 🛠️ How It Works
1. The program tries to connect to each port in the specified range.
2. If the connection succeeds → the port is **OPEN**.
3. If it fails → the port is assumed **CLOSED**.

---

## 📌 Usage
Run the script in your terminal:

```bash
python port_scanner.py

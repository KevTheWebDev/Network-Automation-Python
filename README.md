# 🔧 Network Automation with Python

This project automates configuration backups for Cisco network devices using Python and the Netmiko library.

---

## 🚀 What It Does

- Connects to Cisco devices over SSH
- Logs in using credentials from a YAML file
- Retrieves the running configuration
- Saves the config locally with timestamped filenames

---

## 📂 File Structure

- `backup_configs.py` – Python script to run the backup
- `config.yaml` – Device list and SSH credentials
- `requirements.txt` – Python package dependencies
- `.gitignore` – Prevents secrets and backups from being committed
- `backups/` – Directory that stores all backup files

---

## 🔧 Setup Instructions

Follow these steps to get the project running:

---

### ✅ Step 1: Clone this Repository

Open your terminal and run:

```bash
git clone https://github.com/yourusername/network-automation.git
cd network-automation
```

---

### ✅ Step 2: Install Required Python Packages

Make sure Python 3.7 or higher is installed.

Then install the required dependencies:

```bash
pip install -r requirements.txt
```

---

### ✅ Step 3: Configure Your Devices

Open the `config.yaml` file in a text editor and add your Cisco devices like this:

```yaml
devices:
  - ip: "192.168.1.1"
    username: "admin"
    password: "yourpassword"
    device_type: "cisco_ios"

  - ip: "192.168.1.2"
    username: "admin"
    password: "yourpassword"
    device_type: "cisco_ios"
```

You can add as many devices as you want.

---

### ✅ Step 4: Run the Script

Execute the Python script:

```bash
python backup_configs.py
```

This will connect to each device, download the running config, and save it in the `backups/` folder.

---

### ✅ Step 5: Verify the Backups

Open the `backups/` folder. You should see files named like:

```
192.168.1.1_2025-07-03_1510.txt
```

Each file contains the running configuration for that specific device.

---

## 📸 Example Output

Here’s what you’ll see in your terminal:

```text
[+] Connecting to 192.168.1.1...
[+] Successfully backed up 192.168.1.1 to backups/192.168.1.1_2025-07-03_1510.txt

[+] Connecting to 192.168.1.2...
[+] Successfully backed up 192.168.1.2 to backups/192.168.1.2_2025-07-03_1511.txt
```

---

**Made with ❤️ by [Kevin Orta]**


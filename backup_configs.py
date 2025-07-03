import os
import yaml
from datetime import datetime
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

# Load device config from YAML
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

devices = config.get("devices", [])

# Create backups directory if not exists
if not os.path.exists("backups"):
    os.makedirs("backups")

# Backup each device
for device in devices:
    ip = device["ip"]
    print(f"[+] Connecting to {ip}...")

    try:
        connection = ConnectHandler(**device)
        output = connection.send_command("show running-config")
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
        filename = f"backups/{ip}_{timestamp}.txt"
        
        with open(filename, "w") as f:
            f.write(output)
        
        print(f"[+] Successfully backed up {ip} to {filename}")
        connection.disconnect()

    except NetmikoTimeoutException:
        print(f"[!] Timeout connecting to {ip}")
    except NetmikoAuthenticationException:
        print(f"[!] Authentication failed for {ip}")
    except Exception as e:
        print(f"[!] Error connecting to {ip}: {e}")

#!/usr/bin/env bash

echo "[*] AREBAZ BLACKBOX - One Click Installer"
echo "[*] Detecting environment..."

# Detect Termux
if [ -d "/data/data/com.termux/files/home" ]; then
    echo "[+] Termux detected"

    pkg update && pkg upgrade -y
    pkg install python git nmap clang libjpeg-turbo zlib freetype -y

    pip install --upgrade pip
    pip install -r requirements.txt

# Detect Debian / Kali / Ubuntu
elif [ -f "/etc/debian_version" ]; then
    echo "[+] Debian/Kali/Ubuntu detected"

    sudo apt update
    sudo apt install -y python3 python3-pip nmap

    pip3 install --upgrade pip
    pip3 install -r requirements.txt

else
    echo "[!] Unsupported system"
    exit 1
fi

echo "[✓] Installation completed successfully"
echo "[*] Run the tool using:"
echo "    python main.py"

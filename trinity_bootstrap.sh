#!/data/data/com.termux/files/usr/bin/bash

# Trinity Bootstrap Script for Termux + Proot (Debian)
echo "[+] Bootstrapping Trinity: EmberNode..."

# Install Termux base packages
pkg update && pkg upgrade -y
pkg install -y proot-distro git curl python tmux

# Install Proot Debian
echo "[+] Installing Debian in Proot..."
proot-distro install debian

# Launch into Debian and set up environment
proot-distro login debian -- bash -c '
  apt update && apt install -y python3 python3-pip sqlite3 git curl redis nmap net-tools inotify-tools
  pip3 install fastapi uvicorn watchdog rich nats-py flask

  mkdir -p ~/trinity-core ~/.trinity_core/{logs,db,cache}
  cd ~/trinity-core

  echo "[+] Done. Run API: uvicorn core:app --host 0.0.0.0 --port 8000"
  echo "[+] Run watcher: python3 watcher.py"
  echo "[+] Run Avalanche: python3 avalanche_node.py"
  echo "[+] Dashboard UI: python3 dashboard.py"
'

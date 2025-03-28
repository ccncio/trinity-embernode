import os
import sys
import requests

API_BASE = "http://localhost:8000"

def get_status():
    r = requests.get(f"{API_BASE}/")
    print(r.json())

def get_logs():
    r = requests.get(f"{API_BASE}/logs")
    print(r.json().get("logs", "No logs available."))

def list_processes():
    print(requests.get(f"{API_BASE}/processes").text)

def list_net():
    print(requests.get(f"{API_BASE}/netstat").text)

def help():
    print("""
Trinity CLI Commands:
  status       Show Trinity Core status
  logs         Display last 1000 filesystem log lines
  procs        Show running processes
  net          Show current network connections
    """)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
    else:
        cmd = sys.argv[1]
        if cmd == "status": get_status()
        elif cmd == "logs": get_logs()
        elif cmd == "procs": list_processes()
        elif cmd == "net": list_net()
        else: help()

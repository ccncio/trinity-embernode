import os
from fastapi import FastAPI
import sqlite3

app = FastAPI()
DB_PATH = os.path.expanduser("~/.trinity_core/db/trinity.db")
LOG_PATH = os.path.expanduser("~/.trinity_core/logs/fs_events.log")

@app.get("/")
def root():
    return {"status": "Trinity Core Active"}

@app.get("/logs")
def get_logs():
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH) as f:
            return {"logs": f.read()[-1000:]}
    return {"error": "No logs found"}

@app.get("/processes")
def list_procs():
    return os.popen("ps aux").read()

@app.get("/netstat")
def net_info():
    return os.popen("netstat -tunapl").read()

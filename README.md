# Trinity: EmberNode

**Trinity: EmberNode** is a lightweight AI sentinel node that runs entirely inside Termux + Proot on unrooted Android. It includes:

- Filesystem monitoring
- FastAPI core with process/net/log API
- Avalanche mesh node integration
- Flask-based local dashboard

## Install

```bash
curl -s https://raw.githubusercontent.com/YOUR_USERNAME/trinity-embernode/main/trinity_bootstrap.sh | bash
```

## Usage (inside Proot Debian)

```bash
uvicorn core:app --host 0.0.0.0 --port 8000
python3 watcher.py
python3 avalanche_node.py
python3 dashboard.py
```

MIT License or custom quantumFreedom license

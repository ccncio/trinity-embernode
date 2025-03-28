import time, os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

log_path = os.path.expanduser("~/.trinity_core/logs/fs_events.log")
os.makedirs(os.path.dirname(log_path), exist_ok=True)

class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        with open(log_path, "a") as f:
            f.write(f"[{event.event_type.upper()}] {event.src_path}\n")

observer = Observer()
observer.schedule(Handler(), path=os.path.expanduser("~/storage"), recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

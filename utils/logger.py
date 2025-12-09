from datetime import datetime

# Log events to a file
def log_event(message):
    with open("security_log.txt", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

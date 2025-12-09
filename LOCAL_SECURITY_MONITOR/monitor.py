from process_checker import check_suspicious_processes
from network_scanner import scan_network_connections
from password_audit import check_password_strength
from utils.logger import log_event

# Entry point script
print("🔐 Local Security Monitor Started...\n")

# 1. Scan suspicious processes
processes = check_suspicious_processes()
if processes:
    print("[!] Suspicious processes found:")
    for p in processes:
        print(f"   ➤ PID: {p['pid']} | Process: {p['name']}")
        log_event(f"Suspicious process detected: {p['name']} (PID {p['pid']})")
else:
    print("[✓] No suspicious processes found.")

# 2. Scan suspicious network connections
connections = scan_network_connections()
if connections:
    print("\n[!] Suspicious network connections found:")
    for c in connections:
        print(f"   ➤ Local: {c.laddr} | Remote: {c.raddr} | Status: {c.status}")
        log_event(f"Suspicious connection: {c.laddr} → {c.raddr}")
else:
    print("[✓] No suspicious network connections found.")

# 3. Password check (example)
password = "admin"
if not check_password_strength(password):
    print("\n[!] Weak password detected.")
    log_event("Weak password detected in system check.")
else:
    print("\n[✓] Password strength OK.")

print("\n✔ Scan Completed.")

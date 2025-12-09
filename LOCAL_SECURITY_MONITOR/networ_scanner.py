import psutil

def scan_network_connections():
    flagged = []

    for conn in psutil.net_connections():
        if conn.status == "ESTABLISHED" and conn.raddr:
            ip = conn.raddr.ip

            # Example: suspicious if IP is outside known private ranges
            if not (ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.16.")):
                flagged.append(conn)

    return flagged

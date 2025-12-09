import psutil

def check_suspicious_processes():
    # List of commonly used malicious tool names
    suspicious_list = ["nc", "ncat", "telnet", "meterpreter", "msfconsole"]

    detected = []

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Check if name matches suspicious tools
            if proc.info['name'] in suspicious_list:
                detected.append(proc.info)
        except:
            continue

    return detected

import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

MAX_THREADS = 100

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                return port
    except:
        pass
    return None


#  Ask user for target
target_input = input("Enter IP address or domain name: ")

try:
    target_ip = socket.gethostbyname(target_input)
except socket.gaierror:
    print(" Invalid hostname or IP")
    exit()

#  Ask for port range
port_range = input("Enter port range (default 1-1000): ")
if port_range.strip() == "":
    start_port, end_port = 1, 1000
else:
    try:
        start_port, end_port = map(int, port_range.split("-"))
    except:
        print(" Invalid port range format (use example: 1-1000)")
        exit()

print("*" * 50)
print(f"Scanning target: {target_input} ({target_ip})")
print(f"Ports: {start_port}-{end_port}")
print(f"Start time: {datetime.now()}")
print("*" * 50)

open_ports = []

try:
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        ports = range(start_port, end_port + 1)
        results = executor.map(lambda p: scan_port(target_ip, p), ports)

        for port in results:
            if port:
                open_ports.append(port)
                print(f" Port {port} is open")

except KeyboardInterrupt:
    print("\n Scan interrupted")
    exit()

print("*" * 50)
print("Scan complete!")
print(f"Open ports: {open_ports}")
print(f"End time: {datetime.now()}")
print("*" * 50)
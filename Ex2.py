import nmap
from datetime import datetime

def main():
    scanner = nmap.PortScanner()

    target = input("Enter IP address or domain: ")
    ports = input("Enter port : ")

    if ports.strip() == "":
        ports = " "

    print("*" * 50)
    print(f"Scanning target: {target}")
    print(f"Ports: {ports}")
    print(f"Start time: {datetime.now()}")
    print("*" * 50)

    try:
        scanner.scan(target, ports)

        for host in scanner.all_hosts():
            print(f"\nHost: {host}")
            print(f"State: {scanner[host].state()}")

            for proto in scanner[host].all_protocols():
                print(f"\nProtocol: {proto}")

                ports_list = scanner[host][proto].keys()
                for port in ports_list:
                    state = scanner[host][proto][port]['state']
                    print(f"Port {port}: {state}")

    except Exception as e:
        print(f"Error: {e}")

    print("*" * 50)
    print(f"End time: {datetime.now()}")
    print("*" * 50)


if __name__ == "__main__":
    main()

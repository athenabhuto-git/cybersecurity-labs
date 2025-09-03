import socket

def scan_port(ip, port):
    """Try to connect to a specific port on the target IP"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # wait max 1 second for reply
    try:
        sock.connect((ip, port))
        print(f"[+] Port {port} is OPEN")
    except:
        pass  # ignore closed ports
    finally:
        sock.close()

def main():
    target = input("Enter target IP or hostname: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\n🔍 Scanning {target} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        scan_port(target, port)

if __name__ == "__main__":
    main()

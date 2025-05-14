#please use this for ethical purpose only :)

import socket
import subprocess
import sys
import threading
from queue import Queue
import platform
import argparse
from datetime import datetime

def ping_host(host):
    """
    Ping the target host and return True if it responds, False otherwise.
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        if 'TTL=' in output or 'ttl=' in output:
            return True
        return False
    except subprocess.CalledProcessError:
        return False

def scan_port(target, port, queue):
    """
    Scan a single port on the target host.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            queue.put(f"Port {port} is open - Service: {service}")
        sock.close()
    except:
        pass

def scan_ports(target, start_port=1, end_port=1024):
    """
    Scan a range of ports on the target host using threading.
    """
    print(f"\nStarting port scan on {target}")
    print("=" * 50)
    
    queue = Queue()
    threads = []
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port, queue))
        threads.append(thread)
        thread.start()
    

    for thread in threads:
        thread.join()

    while not queue.empty():
        print(queue.get())

def main():
    parser = argparse.ArgumentParser(description='Network Scanner - Ping and Port Scanner')
    parser.add_argument('target', help='Target host to scan')
    parser.add_argument('-p', '--ports', help='Port range to scan (e.g., 1-100)', default='1-1024')
    args = parser.parse_args()

    target = args.target
    
    try:
    
        target_ip = socket.gethostbyname(target)
        print(f"\nScanning Target: {target} ({target_ip})")
        print(f"Time Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 50)

    
        print(f"\nPinging {target}...")
        if ping_host(target):
            print(f"Host {target} is up!")
            
            start_port, end_port = map(int, args.ports.split('-'))
            
         
            scan_ports(target_ip, start_port, end_port)
        else:
            print(f"Host {target} is down or not responding to ping")

    except socket.gaierror:
        print("\nHostname could not be resolved")
    except ValueError:
        print("\nInvalid port range format. Use start-end (e.g., 1-100)")
    except KeyboardInterrupt:
        print("\nScan interrupted by user")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main() 

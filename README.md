# Network Scanner Tool



## Example Output

Here's an example of scanning a website for common web ports:

![Network Scanner Output](screenshots/scan_output.png)
*Example output showing the results of scanning a website's ports*


- Python 3.x installed on your system
- Basic understanding of networking concepts
- Administrative/root privileges (for some features on Unix-based systems)

## Installation

1. **Clone or Download**
   ```bash
   git clone <your-repository-url>
   # or download the network_scanner.py file directly
   ```

2. **Set Up Python**
   - Windows:
     ```bash
     # Check Python installation
     python --version
     ```
   - Linux/macOS:
     ```bash
     # Make the script executable
     chmod +x network_scanner.py
     ```

3. **Verify Installation**
   ```bash
   python network_scanner.py --help
   ```

## Usage Guide

### Basic Commands

1. **Scan a Single Host**
   ```bash
   python network_scanner.py example.com
   ```

2. **Specify Port Range**
   ```bash
   python network_scanner.py target_host -p 1-100
   ```

3. **Scan Common Web Ports**
   ```bash
   python network_scanner.py target_host -p 80,443
   ```

### Advanced Usage Examples

1. **Scan Local Network Device**
   ```bash
   python network_scanner.py 192.168.1.1
   ```

2. **Comprehensive Web Server Scan**
   ```bash
   python network_scanner.py target_host -p 80-443,8080,8443
   ```

3. **Quick Service Discovery**
   ```bash
   python network_scanner.py target_host -p 21,22,23,25,80,443,3306,5432
   ```



## Common Ports and Their Significance

| Port | Service | Security Implications |
|------|---------|---------------------|
| 21   | FTP     | File transfer, potential anonymous access |
| 22   | SSH     | Secure shell, brute force target |
| 23   | Telnet  | Unencrypted remote access |
| 25   | SMTP    | Email server, spam relay potential |
| 80   | HTTP    | Web server, common entry point |
| 443  | HTTPS   | Secure web server |
| 3306 | MySQL   | Database access |
| 3389 | RDP     | Remote desktop, Windows access |
| 8080 | HTTP Alt| Alternative web server, proxies |


## Example Outputs

### 1. Basic Port Scan Output
```bash
$ python network_scanner.py example.com -p 80-443

Scanning Target: example.com (93.184.216.34)
Time Started: 2024-03-20 10:30:15
==================================================

Pinging example.com...
Host example.com is up!

Starting port scan on 93.184.216.34
==================================================
Port 80 is open - Service: http
Port 443 is open - Service: https
```

### 2. Comprehensive Service Discovery
```bash
$ python network_scanner.py localhost -p 1-100

Scanning Target: localhost (127.0.0.1)
Time Started: 2024-03-20 10:35:22
==================================================

Pinging localhost...
Host localhost is up!

Starting port scan on 127.0.0.1
==================================================
Port 21 is open - Service: ftp
Port 22 is open - Service: ssh
Port 80 is open - Service: http
Port 3306 is open - Service: mysql
```

### 3. Failed Scan Example
```bash
$ python network_scanner.py nonexistent.domain

Hostname could not be resolved
```








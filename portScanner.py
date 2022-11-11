import socket
import termColor

def scan(target, port):
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        print("[-] Port Closed " + str(port))
        
targets = input("[*] Enter Targets To Scan(split the by ,): ")
ports = input("[*] Enter How Manu Ports You Want To Scan: ")

if ',' in targets:
    print("[*] Scannong multiple Targets")
    for ip_addr in targets.split(','): 
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)
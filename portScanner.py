import socket
import termColor

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        print("[-] Port Closed " + str(port))
        
target = input("[*] Enter Target To Scan: ")
ports = input("[*] Enter How Manu Ports You Want To Scan: ")
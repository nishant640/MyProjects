print("This code was written by Nishant Chinnasami")
print()
print("Port scanning is a method of determining which ports on a network are open and could be receiving or sending data. It is also a process for sending packets to specific ports on a host and analyzing responses to identify vulnerabilities.")
print()
print("A port scan is a common technique hackers use to discover open doors or weak points in a network. A port scan attack helps cyber criminals find open ports and figure out whether they are receiving or sending data. It can also reveal whether active security devices like firewalls are being used by an organization.")
print()

import socket

def port_scanner(target, start_port, end_port):
    print(f"Scanning target: {target}")
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  
        result = sock.connect_ex((target, port))  # Returns 0 if the port is open
        
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        sock.close()

# Example usage
try:
    target_ip = input("Enter target IP or domain: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    port_scanner(target_ip, start_port, end_port)
except ValueError:
    print("Please enter valid integer values for ports.")
except Exception as e:
    print(f"An error occurred: {e}")

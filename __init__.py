import os
import socket
import subprocess

def getwifi():
    result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()
    for line in output.split('\n'):
        if 'SSID' in line:
            wifi_name = line.split(':')[1].strip()
            return wifi_name

def getinfo():
    # Use the command line tool 'arp' to get the list of connected devices
    result = subprocess.run(['arp', '-a'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()
    # Extract the IP addresses from the output
    devices = []
    for line in output.split('\n'):
        if 'dynamic' in line:
            device = line.split()[0]
            devices.append(device)
    return devices

import subprocess

def showinfo():
    # Use the 'arp' command to get a list of all devices on the network
    result = subprocess.run(['arp', '-a'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()
    # Extract the IP addresses and MAC addresses from the output
    devices = []
    for line in output.split('\n'):
        if 'dynamic' in line:
            device = {}
            device['ip'] = line.split()[0]
            device['mac'] = line.split()[2]
            devices.append(device)
    # Use the 'getent' command to get the hostnames for each device
    for device in devices:
        result = subprocess.run(['getent', 'hosts', device['ip']], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8').strip()
        device['name'] = output.split()[1]
    return devices

def ping(target, num_bytes):
    # Resolve the IP address of the target if it is a domain name
    try:
        ip_address = socket.gethostbyname(target)
    except socket.gaierror:
        return False

    # Use the 'ping' command to send num_bytes of data to the specified IP address
    result = os.system(f"ping -c 1 -s {num_bytes} {ip_address}")
    if result == 0:
        return True
    else:
        return False

def trc(target):
    # Resolve the IP address of the target if it is a domain name
    try:
        ip_address = socket.gethostbyname(target)
    except socket.gaierror:
        return []

    # Use the 'traceroute' command to trace the route to the specified IP address
    result = subprocess.run(['traceroute', ip_address], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()
    # Extract the IP addresses of the intermediate hops from the output
    hops = []
    for line in output.split('\n')[1:]:
        if '* * *' not in line:
            hop_info = line.split()
            hop_ip = hop_info[1]
            hops.append(hop_ip)
    return hops

def netscan():
    result = subprocess.run(['netsh', 'wlan', 'show', 'networks'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()
    networks = []
    for line in output.split('\n'):
        if 'SSID' in line:
            ssid = line.split(':')[1].strip()
            networks.append(ssid)
    return networks

def prtscan(ip_address):
    open_ports = []
    # Try to connect to each port on the specified IP address using the 'powershell' command
    for port in range(1, 65535):
        result = subprocess.run(['powershell', '-c', f"Test-NetConnection -ComputerName {ip_address} -Port {port}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # If the 'powershell' command was successful, the port is open
        if 'True' in result.stdout.decode('utf-8'):
            open_ports.append(port)
    return open_ports
import os
import socket
import subprocess

def get_wifi_name():
    # Use the command line tool 'iwgetid' to get the WiFi name
    result = subprocess.run(['iwgetid', '-r'], stdout=subprocess.PIPE)
    wifi_name = result.stdout.decode('utf-8').strip()
    return wifi_name

def get_connected_devices():
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

def get_device_ip(device_name):
    # Use the command line tool 'arp' to get the IP address of a specific device
    result = subprocess.run(['arp', '-a', device_name], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()
    # Extract the IP address from the output
    device_ip = output.split()[1][1:-1]
    return device_ip

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

def trace(target):
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
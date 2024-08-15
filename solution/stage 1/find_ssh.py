import os
from scapy.all import rdpcap, TCP

def is_ssh_packet(packet):
    """
    Check if a packet is an SSH packet.
    SSH typically runs on port 22.
    """
    if packet.haslayer(TCP):
        tcp_layer = packet.getlayer(TCP)
        if tcp_layer.dport == 22 or tcp_layer.sport == 22:
            return True
    return False

def scan_pcap_for_ssh(pcap_file):
    """
    Scan a pcap file for SSH communication.
    """
    packets = rdpcap(pcap_file)
    for packet in packets:
        if is_ssh_packet(packet):
            return True
    return False

def scan_folder_for_ssh(folder_path):
    """
    Scan all pcap files in a folder for SSH communication.
    """
    ssh_pcap_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pcap') or filename.endswith('pcapng') or filename.endswith('.cap'):
            pcap_file = os.path.join(folder_path, filename)
            if scan_pcap_for_ssh(pcap_file):
                ssh_pcap_files.append(filename)
    return ssh_pcap_files

# Replace 'path/to/pcap/folder' with the path to the folder containing your pcap files
folder_path = '.'
ssh_pcap_files = scan_folder_for_ssh(folder_path)

if ssh_pcap_files:
    print("The following pcap files contain SSH communication:")
    for pcap_file in ssh_pcap_files:
        print(pcap_file)
else:
    print("No pcap files with SSH communication found.")

# Imports near the top
import os
import datetime


def arp_table_extract():
    os.system("arp -a > arp_table.txt")
    lines = []
    filtered_data = {}
    with open("arp_table.txt", "r") as arp_table_data:
        for line in arp_table_data:
            if "dynamic" in line:
                lines.append(line)
                line_split = line.split()
                filtered_data[line_split[0]] = line_split[1]
    return filtered_data

def find_duplicates(dictionay_ip_mac):
    duplicate_list = []
    all_mac_addresses = []
    return_dictionary_duplicate = {}
    for key in dictionay_ip_mac:
        mac = dictionay_ip_mac[key]
        if mac in all_mac_addresses:
            print(f"Duplicate found: {mac}")
            duplicate_list.append(mac)
        all_mac_addresses.append(dictionay_ip_mac[key])
    for ip in dictionay_ip_mac:
        mac = dictionay_ip_mac[ip]
        if mac in duplicate_list:
            return_dictionary_duplicate[ip] = mac

    return return_dictionary_duplicate

def log_results(duplicates):
    with open("Log.txt", "a") as file:
        for ip, mac in duplicates.items():
            file.write(f"Duplicate found - {ip} with mac {mac} found @ {datetime.datetime.now()}\n")

if __name__ == "__main__":
    filtered = arp_table_extract()
    duplicates = find_duplicates(filtered)
    log_results(duplicates)
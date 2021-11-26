# Imports near the top
import os
import datetime

# Defining the arp table command and saving the output to a file
def arp_table_extract():
    os.system("arp -a > arp_table.txt")
    lines = []
    parsed_output = {}
    with open("arp_table.txt", "r") as arp_table_data:
        for line in arp_table_data:
            if "dynamic" in line:
                lines.append(line)
                line_split = line.split()
                parsed_output[line_split[0]] = line_split[1]
    return parsed_output

# Defining the function to print duplicate mac addresses in our arp table.

def find_duplicates(dictionary_ip_mac):
    duplicate_list = []
    all_mac_addresses = []
    return_dictionary_duplicate = {}
    for key in dictionary_ip_mac:
        mac = dictionary_ip_mac[key]
        if mac in all_mac_addresses:
            print("Duplicate found: {}".format(mac))
            duplicate_list.append(mac)
        all_mac_addresses.append(dictionary_ip_mac[key])
    for ip in dictionay_ip_mac:
        mac = dictionay_ip_mac[ip]
        if mac in duplicate_list:
            return_dictionary_duplicate[ip] = mac

    return return_dictionary_duplicate
# Logging the duplicate output into a file for deeper analyses
def log_results(duplicates):
    with open("Log.txt", "a") as file:
        for ip, mac in duplicates.items():
            file.write(f"Duplicate found - {ip} with mac {mac} found @ {datetime.datetime.now()}\n")

if __name__ == "__main__":
    parsed_output = arp_table_extract()
    duplicates = find_duplicates(parsed_output)
    log_results(duplicates)

"""
imports a CSV system log from the TACACS server and finds unique IP addresses
that have connected to the server. Returns the number of unique IPs and
a list of unique IPs into the terminal
"""

import csv

def open_log(file):
    """
    Use built-in csv library to open and parse system log file
    Returns a list of all the items in the NAS_IP column of the log
    """
    ip_list = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            if len(line[4]) > 0:
                ip_list.append(line[4])
        ip_list = ip_list[1:]
    return ip_list

def main():
    """
    Prints the number and a list of unique IP addresses in the system log
    into the terminal. Parses the output of open_log function to find
    unique entries.
    """
    file = input("Please enter your system log file name / path: ")
    csv_log = open_log(file)
    unique_ip_list = []
    unique_ip_count = 0
    unique_ip_string = ""
    for ip_address in csv_log:
        if ip_address not in unique_ip_list:
            unique_ip_count += 1
            unique_ip_string = unique_ip_string + ip_address + "\n"
            unique_ip_list.append(ip_address)
    unique_ip_string = unique_ip_string[:-1]
    output = str(unique_ip_count) + " Unique IP addresses found in log " + file +\
         "\n" + "Unique IP addresses:\n" + unique_ip_string
    return output

#print(main("System_2019-11-04_3.csv"))
print(main())

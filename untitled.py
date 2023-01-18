from termcolor import colored

file_name = input("Enter the name of the file: ")
with open(file_name, 'r') as file:
    ips = file.readlines()

# Open a new file in write mode to save the results
with open('reachable_linux_servers.txt', 'w') as output_file_linux, open('reachable_windows_servers.txt', 'w') as output_file_windows:
    for ip in ips:
        ip = ip.strip()
        # Windows
        if platform.system() == "Windows":
            response = os.system("ping -n 1 " + ip)
            if response == 0:
                os.system("systeminfo /s " + ip)
                output_file_windows.write(ip + '\n')
                print(colored(ip + " is reachable Windows server.", 'green'))
            else:
                print(colored(ip + " is not reachable", 'red'))
        # Linux/Unix
        else:
            response = os.system("ping -c 1 " + ip)
            if response == 0:
                os.system("ssh " + ip + " 'uname -a'")
                output_file_linux.write(ip + '\n')
                print(colored(ip + " is reachable Linux server.", 'green'))
            else:
                print(colored(ip + " is not reachable", 'red'))
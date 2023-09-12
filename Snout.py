import nmap

nm = nmap.PortScanner()

print("   ▄████████ ███▄▄▄▄    ▄██████▄  ███    █▄      ███                       |\ ")
print("  ███    ███ ███▀▀▀██▄ ███    ███ ███    ███ ▀█████████▄          \`-. _.._| \ ")
print("  ███    █▀  ███   ███ ███    ███ ███    ███    ▀███▀▀██           |_,'  __`. \ ")
print("  ███        ███   ███ ███    ███ ███    ███     ███   ▀           ████████████")
print("▀███████████ ███   ███ ███    ███ ███    ███     ███              ,'      __ \ |")
print("         ███ ███   ███ ███    ███ ███    ███     ███            ,'     __/||\  |")
print("   ▄█    ███ ███   ███ ███    ███ ███    ███     ███           (Y8P  ,/|||||/  |")
print(" ▄████████▀   ▀█   █▀   ▀██████▀  ████████▀     ▄████▀             `-'_----    /")
print("\n~ By @jpmamededs with the help of DIO")
print("\n<---------------------------------------------------------------------------->")

ip = input("\nInsert the ip address to be scanned: ")
print("\nThe ip to be mapped will be", ip)
type(ip)

menu = int(input(""" Choose the type of scan you want to be made and type it below
            
            1) SYN Scan
            2) UDP Scan
            3) Intense Scan
            
            Type it here: """))

print("\nThe chosen option was", menu)

if menu == 1:
    print("nMap Version:", nm.nmap_version())
    nm.scan(ip, '1-1024' '-v -sS')
    print(nm.scaninfo())
    print("IP Status:", nm[ip].state())
    print(nm[ip].all_protocols())
    print("")
    print("Open ports:", nm[ip]['tcp'].keys())
elif menu == 2:
    print("nMap Version:", nm.nmap_version())
    nm.scan(ip, '1-1024', '-v -sU')
    print(nm.scaninfo())
    print("IP Status:", nm[ip].state())
    print(nm[ip].all_protocols())
    print("")
    print("Open ports:", nm[ip]['udp'].keys())
elif menu == 3:
    print("nMap Version:", nm.nmap_version())
    nm.scan(ip, '1-1024', '-v -sC')
    print(nm.scaninfo())
    print("IP Status:", nm[ip].state())
    print(nm[ip].all_protocols())
    print("")
    print("Open ports:", nm[ip]['tcp'].keys())
else:
    print("Choose a valid option.")

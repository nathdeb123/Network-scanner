import pyfiglet
i=pyfiglet.figlet_format("Network Scanner")
print(i)
ip = input(str("Enter the IP :"))
Ex = input("Enter Extension :")
import subprocess
subprocess.call( "nmap " + ip + " " + Ex ,shell=True)
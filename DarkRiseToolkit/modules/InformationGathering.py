from core.DarkRiseSettings import DarkRiseSettings
from DarkRise import DarkRise
from termcolor import colored
import scrapy
import subprocess
import nmap
import socket

class IG(DarkRiseSettings):
    def __init__(self):
        super().__init__()
        self.Options = """
    {1}--Nmap - Network Mapper
    {2}--Setoolkit
    {3}--Host To Ip
    {4}--ARP Scan
    {99}-Back To Main Menu
        """

    def Start(self):
        subprocess.call("clear")
        self.logo()
        print(colored(self.Options, "green", attrs=["bold"]))

        choice = input(colored("DarkRise:IG~# ", "cyan", attrs=["bold"]))

        while not choice in ["1", "2", "3", "4", "99"]:
            choice = input(colored("DarkRise:IG~# ", "cyan", attrs=["bold"]))
        else:
            if choice == "1":
                self.NmapScreen()
            elif choice == "2":
                subprocess.call("setoolkit")
            elif choice == "3":
                self.HostToIpScreen()
            elif choice == "4":
                self.ARPScan()
            elif choice == "99":
                MainMenu = DarkRise()
                MainMenu.Start()

    def NmapScreen(self):
        subprocess.call("clear")
        self.logo()

        nmoptions = {
            "ipAddr": "..."
        }

        cmd = ""

        while True:
            # Variables For F Strings
            ipaddr = nmoptions["ipAddr"]
            # Main Variables
            cmd = input(colored("DarkRise:NmapScan~# ", "cyan", attrs=["bold"])).lower()
            argsCommands = cmd.split(" ")

            if cmd == "help" or cmd == "?":
                print("\n\nDarkRise Nmap Help :")
                print("""
                
            {show options}         -------> Shows The Module Options
            {help OR ?}            -------> Shows This Help Menu
            {set (option) (value)} -------> Set Option's Value
            {scan, run}            -------> Run The Module
            {back, exit}           -------> Back To Main Topic Menu
                """)
            elif cmd == "show options" or cmd == "options":
                print(f"""
            IPADDR      {ipaddr}      OPTIONAL
                """)
            elif argsCommands[0] == "set" and argsCommands[1] == "ipaddr" and len(argsCommands) == 3:
                nmoptions["ipAddr"] = argsCommands[2]
            elif cmd == "scan" or cmd == "run" or cmd == "start":
                self.NmapScan(nmoptions["ipAddr"])
            elif cmd == "back" or cmd == "exit":
                self.Start()
                break
            else:
                print("Command Not Exist!, Use help To Show Available Commands.")

    def NmapScan(self, target):
        nm = nmap.PortScanner()
        try:
            scan = nm.scan(hosts=str(target), arguments="-sV")
            for port in scan["scan"][str(target)]['tcp']:
                state = scan["scan"][str(target)]["tcp"][port]["state"]
                print(colored(f"""  port {port} {state} """, "blue", "on_white", attrs=["bold"]))
        except KeyError:
            print("There Is An Error In Inserted Ip Address!")

    def HostToIpScreen(self):
        subprocess.call("clear")
        self.logo()

        Host2IpOptions = {
            "hostname": "..."
        }

        cmd = ""

        while True:
            # Variables For F Strings
            hostname = Host2IpOptions["hostname"]
            # Main Variables
            cmd = input(colored("DarkRise:Host2IP~# ", "cyan", attrs=["bold"])).lower()
            argsCommands = cmd.split(" ")

            if cmd == "help" or cmd == "?":
                print("\n\nDarkRise Host2IP Help :")
                print("""
                
            {show options}         -------> Shows The Module Options
            {help OR ?}            -------> Shows This Help Menu
            {set (option) (value)} -------> Set Option's Value
            {scan, run}            -------> Run The Module
            {back, exit}           -------> Back To Main Topic Menu
                """)
            elif cmd == "show options" or cmd == "options":
                print(f"""
            HOSTNAME      {hostname}      REQUIRED
                """)
            elif argsCommands[0] == "set" and argsCommands[1] == "hostname" and len(argsCommands) == 3:
                Host2IpOptions["hostname"] = argsCommands[2]
            elif cmd == "scan" or cmd == "run" or cmd == "start":
                print(socket.gethostbyname(hostname))
            elif cmd == "back" or cmd == "exit":
                self.Start()
                break
            else:
                print("Command Not Exist!, Use help To Show Available Commands.")

    def ARPScan(self):
        subprocess.call(["netdiscover", "-r", "192.168.1.0/16"])
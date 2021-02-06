from core.DarkRiseSettings import DarkRiseSettings
from thirdparty.sshbreaker import SSH_Breaker
from thirdparty.telnetbreaker import Telnet_Breaker
from thirdparty.ftpbreaker import FTP_Breaker
import DarkRise
from termcolor import colored
import subprocess
import itertools
import sys

class PA(DarkRiseSettings):
    def __init__(self):
        super().__init__()
        self.Options = """
    {1}--Password Cracking Attack
    {2}--Create A Wordlist
    {99}-Back To Main Menu
        """
        self.PassCrackingOptions = """
    {1}--SSH Cracking
    {2}--Telnet Cracking
    {3}--FTP Cracking
    {99}-Back To Main Topic Menu
        """

    def Start(self):
        subprocess.call("clear")
        self.logo()
        print(colored(self.Options, "green", attrs=["bold"]))

        choice = input(colored("DarkRise:PasswordAttacks~# ", "cyan", attrs=["bold"]))

        while not choice in ["1", "2", "99"]:
            choice = input(colored("DarkRise:PasswordAttacks~# ", "cyan", attrs=["bold"]))
        else:
            if choice == "1":
                self.PasswordCrackingScreen()
            elif choice == "2":
                self.WLCreatorScreen()
            elif choice == "99":
                MainMenu = DarkRise.DarkRise()
                MainMenu.Start()

    def WLCreatorScreen(self):
        subprocess.call("clear")
        self.logo()

        WLOptions = {
            "path": "wordlist.txt",
            "min": "3",
            "max": "5",
        }

        cmd = ""

        while True:
            # Variables For F Strings
            path = WLOptions["path"]
            minvalue = WLOptions["min"]
            maxvalue = WLOptions["max"]
            # Main Variables
            cmd = input(colored("DarkRise:PasswordAttacks~# ", "cyan", attrs=["bold"])).lower()
            argsCommands = cmd.split(" ")

            if cmd == "help" or cmd == "?":
                print("\n\nDarkRise Wordlist Wordlist Help :")
                print("""
                
            {show options}         -------> Shows The Module Options
            {help OR ?}            -------> Shows This Help Menu
            {set (option) (value)} -------> Set Option's Value
            {generate, run}        -------> Run The Module
            {back, exit}           -------> Back To Main Topic Menu
                """)
            elif cmd == "show options" or cmd == "options":
                print(f"""
            PATH        {path}        REQUIRED
            MIN         {minvalue}    REQUIRED
            MAX         {maxvalue}    REQUIRED
                """)
            elif argsCommands[0] == "set" and argsCommands[1] == "path" and len(argsCommands) == 3:
                WLOptions["path"] = argsCommands[2]
            elif argsCommands[0] == "set" and argsCommands[1] == "min" and len(argsCommands) == 3:
                WLOptions["min"] = argsCommands[2]
            elif argsCommands[0] == "set" and argsCommands[1] == "max" and len(argsCommands) == 3:
                WLOptions["max"] = argsCommands[2]
            elif cmd == "generate" or cmd == "run" or cmd == "start":
                self.WLGenerate(WLOptions["path"], WLOptions["min"], WLOptions["max"])
            elif cmd == "back" or cmd == "exit":
                self.Start()
                break
            else:
                print("Command Not Exist!, Use help To Show Available Commands.")

    def WLGenerate(self, path, minvalue, maxvalue):
        count = 0
        print("Writing Wordlist! Please Wait It May Take A While.")
        for num in range(int(minvalue), int(maxvalue) + 1):
            res = itertools.product('abcdefghijklmnopqrstuvwxyz1234567890*&$#@', repeat=num) 
            for i in res:
                f = open(path, "a")
                f.write("\n" + "".join(i))
                sys.stdout.write(f'\rWritten {count} Words In Your Wordlist!')
                count += 1

        f.close()

    def PasswordCrackingScreen(self):
        subprocess.call("clear")
        self.logo()
        print(colored(self.PassCrackingOptions, "green", attrs=["bold"]))

        choice = input(colored("DarkRise:PasswordAttacks~# ", "cyan", attrs=["bold"]))

        while not choice in ["1", "2", "3", "4", "99"]:
            choice = input(colored("DarkRise:PasswordAttacks~# ", "cyan", attrs=["bold"]))
        else:
            if choice == "1":
                self.SSH_Cracking_Screen()
            elif choice == "2":
                self.Telnet_Cracking_Screen()
            elif choice == "3":
                self.FTP_Cracking_Screen()
            elif choice == "99":
                MainMenu = DarkRise.DarkRise()
                MainMenu.Start()

    def SSH_Cracking_Screen(self):
        subprocess.call("clear")
        self.logo()

        SSH_Options = {
            "username": "root",
            "server": "localhost",
            "port": "22",
            "wordlist": "wordlist.txt",
        }

        cmd = ""

        while True:
            # Variables For F Strings
            username = SSH_Options["username"]
            server = SSH_Options["server"]
            port = SSH_Options["port"]
            wordlist = SSH_Options["wordlist"]
            # Main Variables
            cmd = input(colored("DarkRise:PasswordAttacks~# ", "cyan", attrs=["bold"])).lower()
            argsCommands = cmd.split(" ")

            if cmd == "help" or cmd == "?":
                print("\n\nDarkRise SSH Cracking Help :")
                print("""
                
            {show options}         -------> Shows The Module Options
            {help OR ?}            -------> Shows This Help Menu
            {set (option) (value)} -------> Set Option's Value
            {generate, run}        -------> Run The Module
            {back, exit}           -------> Back To Main Topic Menu
                """)
            elif cmd == "show options" or cmd == "options":
                print(f"""
            USERNAME    {username}  REQUIRED
            SERVER      {server}    REQUIRED
            PORT        {port}      REQUIRED
            WORDLIST    {wordlist}  REQUIRED
                """)
            elif argsCommands[0] == "set" and argsCommands[1] == "username" and len(argsCommands) == 3:
                SSH_Options["username"] = argsCommands[2]
            elif argsCommands[0] == "set" and argsCommands[1] == "server" and len(argsCommands) == 3:
                SSH_Options["server"] = argsCommands[2]
            elif argsCommands[0] == "set" and argsCommands[1] == "port" and len(argsCommands) == 3:
                SSH_Options["port"] = argsCommands[2]
            elif argsCommands[0] == "set" and argsCommands[1] == "wordlist" and len(argsCommands) == 3:
                SSH_Options["wordlist"] = argsCommands[2]
            elif cmd == "generate" or cmd == "run" or cmd == "start":
                try:
                    sshbreaker = SSH_Breaker(username=SSH_Options["username"], ipaddr=SSH_Options["server"], port=SSH_Options["port"], wordlist=SSH_Options["wordlist"])
                    sshbreaker.Break()
                except:
                    print(colored("[-] AN ERROR HAPPEND CHECK YOUR OPTIONS!", "red", attrs=["bold"]))
            elif cmd == "back" or cmd == "exit":
                self.PasswordCrackingScreen()
                break
            else:
                print("Command Not Exist!, Use help To Show Available Commands.")

    def Telnet_Cracking_Screen(self):
        subprocess.call("clear")
        self.logo()

        Telnet_Options = {
            "username": "root",
            "server": "localhost",
            "port": "23",
            "wordlist": "wordlist.txt",
        }

        cmd = ""

        while True:
            # Variables For F Strings
            username = Telnet_Options["username"]
            server = Telnet_Options["server"]
            port = Telnet_Options["port"]
            wordlist = Telnet_Options["wordlist"]
            # Main Variables
            cmd = input(colored("DarkRise:PasswordAttacks~# ", "cyan", attrs=["bold"])).lower()
            argsCommands = cmd.split(" ")

            if cmd == "help" or cmd == "?":
                print("\n\nDarkRise Telnet Cracking Help :")
                print("""
                
            {show options}         -------> Shows The Module Options
            {help OR ?}            -------> Shows This Help Menu
            {set (option) (value)} -------> Set Option's Value
            {generate, run}        -------> Run The Module
            {back, exit}           -------> Back To Main Topic Menu
                """)
            elif cmd == "show options" or cmd == "options":
                print(f"""
            USERNAME    {username}  REQUIRED
            SERVER      {server}    REQUIRED
            PORT        {port}      REQUIRED
            WORDLIST    {wordlist}  REQUIRED
                """)
            elif argsCommands[0] == "set" and argsCommands[1] == "username" and len(argsCommands) == 3:
                Telnet_Options["username"] = argsCommands[2]
            elif argsCommands[0] == "set" and argsCommands[1] == "server" and len(argsCommands) == 3:
                Telnet_Options["server"] = argsCommands[2]
            elif argsCommands[0] == "set" and argsCommands[1] == "port" and len(argsCommands) == 3:
                Telnet_Options["port"] = argsCommands[2]
            elif argsCommands[0] == "set" and argsCommands[1] == "wordlist" and len(argsCommands) == 3:
                Telnet_Options["wordlist"] = argsCommands[2]
            elif cmd == "generate" or cmd == "run" or cmd == "start":
                try:
                    telnetcracker = Telnet_Breaker(username=Telnet_Options["username"], ipaddr=Telnet_Options["server"], port=Telnet_Options["port"], wordlist=Telnet_Options["wordlist"])
                    telnetcracker.Break()
                except:
                    print(colored("[-] AN ERROR HAPPEND CHECK YOUR OPTIONS!", "red", attrs=["bold"]))
            elif cmd == "back" or cmd == "exit":
                self.PasswordCrackingScreen()
                break
            else:
                print("Command Not Exist!, Use help To Show Available Commands.")

    def FTP_Cracking_Screen(self):
        subprocess.call("clear")
        self.logo()

        FTP_Options = {
            "username": "root",
            "server": "localhost",
            "port": "23",
            "wordlist": "wordlist.txt",
        }

        cmd = ""

        while True:
            # Variables For F Strings
            username = FTP_Options["username"]
            server = FTP_Options["server"]
            port = FTP_Options["port"]
            wordlist = FTP_Options["wordlist"]
            # Main Variables
            cmd = input(colored("DarkRise:PasswordAttacks~# ", "cyan", attrs=["bold"])).lower()
            argsCommands = cmd.split(" ")

            if cmd == "help" or cmd == "?":
                print("\n\nDarkRise FTP Cracking Help :")
                print("""
                
            {show options}         -------> Shows The Module Options
            {help OR ?}            -------> Shows This Help Menu
            {set (option) (value)} -------> Set Option's Value
            {generate, run}        -------> Run The Module
            {back, exit}           -------> Back To Main Topic Menu
                """)
            elif cmd == "show options" or cmd == "options":
                print(f"""
            USERNAME    {username}  REQUIRED
            SERVER      {server}    REQUIRED
            PORT        {port}      REQUIRED
            WORDLIST    {wordlist}  REQUIRED
                """)
            elif argsCommands[0] == "set" and argsCommands[1] == "username" and len(argsCommands) == 3:
                FTP_Options["username"] = argsCommands[2]
            elif argsCommands[0] == "set" and argsCommands[1] == "server" and len(argsCommands) == 3:
                FTP_Options["server"] = argsCommands[2]
            elif argsCommands[0] == "set" and argsCommands[1] == "port" and len(argsCommands) == 3:
                FTP_Options["port"] = argsCommands[2]
            elif argsCommands[0] == "set" and argsCommands[1] == "wordlist" and len(argsCommands) == 3:
                FTP_Options["wordlist"] = argsCommands[2]
            elif cmd == "generate" or cmd == "run" or cmd == "start":
                try:
                    ftpcracker = FTP_Breaker(username=FTP_Options["username"], ipaddr=FTP_Options["server"], port=FTP_Options["port"], wordlist=FTP_Options["wordlist"])
                    ftpcracker.Break()
                except:
                    print(colored("[-] AN ERROR HAPPEND CHECK YOUR OPTIONS!", "red", attrs=["bold"]))
            elif cmd == "back" or cmd == "exit":
                self.PasswordCrackingScreen()
                break
            else:
                print("Command Not Exist!, Use help To Show Available Commands.")
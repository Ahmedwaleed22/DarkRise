from core.DarkRiseSettings import DarkRiseSettings
from termcolor import colored
from modules import InformationGathering as IG
from modules import PasswordAttacks as PA
from modules import PayloadAttacks
import subprocess
import os

class DarkRise(DarkRiseSettings):
    def __init__(self):
        super().__init__()
        self.Options = """
    {1}--Information Gathering
    {2}--Password Attacks
    {3}--Payload & Listener
    {0}--INSTALL & UPDATE
    {99}-EXIT
        """

    def Start(self):
        euid = os.geteuid()
        if euid != 0:
            subprocess.call("clear")
            self.logo()
            print(colored("""    DarkRise Toolkit Requires Root Access To Run!""", "red", attrs=["bold"]))
        else:
            try:
                self.Main()
            except KeyboardInterrupt:
                self.Exit()

    def Main(self):
        subprocess.call("clear")
        self.logo()
        print(colored(self.Options, "green", attrs=["bold"]))

        choice = input(colored("DarkRise:~# ", "cyan", attrs=["bold"]))

        while not choice in ["0", "1", "2", "3", "99"]:
            choice = input(colored("DarkRise:~# ", "cyan", attrs=["bold"]))
        else:
            if choice == "1":
                IGModule = IG.IG()
                IGModule.Start()
            elif choice == "2":
                PAModule = PA.PA()
                PAModule.Start()
            elif choice == "3":
                PLA = PayloadAttacks.PayloadAttacks()
                PLA.Start()
            elif choice == "99":
                self.Exit()


    def Exit(self):
        subprocess.call("clear")
        print(colored("Bye, See You Again In Your Next Attack!", "red", attrs=["bold"]))


if __name__ == "__main__":
    DarkRise = DarkRise()
    DarkRise.Start()
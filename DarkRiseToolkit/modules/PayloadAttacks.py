from core.DarkRiseSettings import DarkRiseSettings
import DarkRise
from termcolor import colored
import subprocess
import socket

class PayloadAttacks(DarkRiseSettings):
    def __init__(self):
        super().__init__()
        self.Options = """
    {1}--Create Payloads
    {2}--Listeners - Listen For Payload Connections
    {99}-Back To Main Menu
        """
        self.PayloadsTypes = """
    {1}--MSFVENOM Payloads
    {2}--Custom DarkRise Payloads
        """

    def Start(self):
        subprocess.call("clear")
        self.logo()
        print(colored(self.Options, "green", attrs=["bold"]))

        choice = input(colored("DarkRise:PayloadAttacks~# ", "cyan", attrs=["bold"]))

        while not choice in ["1", "2", "99"]:
            choice = input(colored("DarkRise:PayloadAttacks~# ", "cyan", attrs=["bold"]))
        else:
            if choice == "1":
                self.Payload_Options_Screen()
            elif choice == "2":
                pass
            elif choice == "99":
                MainMenu = DarkRise.DarkRise()
                MainMenu.Start()

    def Payload_Options_Screen(self):
        subprocess.call("clear")
        self.logo()
        print(colored(self.PayloadsTypes, "green", attrs=["bold"]))

        choice = input(colored("DarkRise:PayloadAttacks~# ", "cyan", attrs=["bold"]))

        while not choice in ["1", "2", "99"]:
            choice = input(colored("DarkRise:PayloadAttacks~# ", "cyan", attrs=["bold"]))
        else:
            if choice == "1":
                self.Msfvenom_Payload_Creator()
            elif choice == "2":
                self.Custom_Payload_Creator()
            elif choice == "99":
                MainMenu = DarkRise.DarkRise()
                MainMenu.Start()

    def Msfvenom_Payload_Creator(self):
        pass
        
    def Custom_Payload_Creator(self):
        pass
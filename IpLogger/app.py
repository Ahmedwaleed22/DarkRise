from flask import Flask, render_template, request, redirect
from termcolor import colored
import requests as rq

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("indexenc.html")

@app.route("/nextstep/", methods=["POST"])
def nextstep():
    ipaddr = request.form.get("ip")
    servicesList = []
    serviceCheck = rq.get(f"https://vpnapi.io/api/{ipaddr}?key=F9J3K1V02MFO1C93KA7B").json()

    if serviceCheck['security']['vpn'] == True:
        servicesList.append('VPN')
    elif serviceCheck['security']['proxy'] == True:
        servicesList.append('PROXY')
    elif serviceCheck['security']['tor'] == True:
        servicesList.append('TOR')

    if len(servicesList) < 1:
        services = "REAL IP ADDRESS"
    else:
        services = ",".join(servicesList)
    print(colored(f"[*] FOUND IP ADDRESS --- ({services}) {ipaddr}", "cyan", attrs=["bold"]))
    return "An Error Happend!"

if __name__ == "__main__":
    app.run(debug=True, port=80)

from flask import Flask, render_template, request, redirect
from termcolor import colored

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("indexenc.html")

@app.route("/nextstep/", methods=["POST"])
def nextstep():
    ipaddr = request.form.get("ip")
    print(colored(f"[*] FOUND IP ADDRESS --- {ipaddr}", "cyan", attrs=["bold"]))
    return "An Error Happend!"

if __name__ == "__main__":
    app.run(debug=False, port=80)

from datetime import date as dt
from flask import Flask, render_template
from morse import morse_dict
from sillyName import adjectives, nouns
import os
import random
import socket

app = Flask(__name__)
The_hub = os.getenv("THEHUB")
nouns = list(set(nouns))
adjectives = list(set(adjectives))

today = dt.today()
year = today.year
month = today.month
day = today.day
ip_addresses = ["10.0.0.220", "67.170.203.253"]
try:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
except:
    ip_address = "You have hidden your ip address."


@app.route('/')
def index():
    return render_template("index.html", the_year=year)


@app.route('/interesting')
def interesting():
    return render_template("interesting.html", the_year=year)


@app.route('/hydr')
def hydr():
    return render_template("virus.html", the_year=year)


@app.route('/goofy')
def goofy():
    return render_template("goofy.html", the_year=year)


@app.route('/fun')
def fun():
    return render_template("fun.html", the_year=year)


@app.route('/youdontknowwhowereallyare')
def mainframe():
    return render_template("mainframe.html", the_year=year)


@app.route('/idiot')
def idiot():
    return render_template("idiot.html", the_year=year)


@app.route('/robots.txt')
def robots():
    return render_template("robots.html")


@app.route('/music')
def music():
    return render_template("music.html", the_year=year)


@app.route('/saul')
def saul():
    return render_template("saul.html", the_year=year)


@app.route(f'/{The_hub}')
def hub():
    return render_template("the_hub.html", the_year=year)


@app.route('/iphone')
def iphone():
    return render_template("iphone.html", the_year=year)


@app.route('/my-ip')
def ip():
    return render_template("ip.html", ip_address=ip_address, the_year=year)


@app.route('/bozo')
def dum():
    return render_template("dum.html", ip_address=ip_address, the_year=year)


@app.route('/dum-clicker')
def clicker():
    return render_template("clicker.html",
                           ip_address=ip_address,
                           the_year=year)


@app.route('/miner-clicker')
def cookie():
    result = f"{random.choice(adjectives)} {random.choice(adjectives)} {random.choice(nouns)}"
    return render_template("pie.html",
                           the_year=year,
                           ip_address=ip_address,
                           result=result)


@app.route('/encode/<text>')
def encode(text):
    result = ""
    for char in text.lower():
        if char in morse_dict:
            result += morse_dict[char] + "  "
        else:
            result += char
    result += '...-- -----'
    return render_template("morse.html",
                           the_year=year,
                           result=result,
                           text=text)


@app.route('/sillyname')
def sillyname():
    result = f"{random.choice(adjectives)} {random.choice(adjectives)} {random.choice(nouns)}"
    return render_template("sillyname.html", the_year=year, result=result)


@app.route('/sillyname5')
def sillyname5():
    result1 = f"{random.choice(adjectives)} {random.choice(adjectives)} {random.choice(nouns)}"
    result2 = f"{random.choice(adjectives)} {random.choice(adjectives)} {random.choice(nouns)}"
    result3 = f"{random.choice(adjectives)} {random.choice(adjectives)} {random.choice(nouns)}"
    result4 = f"{random.choice(adjectives)} {random.choice(adjectives)} {random.choice(nouns)}"
    result5 = f"{random.choice(adjectives)} {random.choice(adjectives)} {random.choice(nouns)}"
    return render_template(
        "sillyname5.html",
        the_year=year,
        result1=result1,
        result2=result2,
        result3=result3,
        result4=result4,
        result5=result5,
    )


app.run(host='0.0.0.0', port=3000, debug=False)

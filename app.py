from flask import Flask, request, render_template, redirect, session, make_response, url_for, flash, jsonify
import requests
import dropbox
import json
from datetime import datetime, timedelta
import time
from flask_simple_geoip import SimpleGeoIP

app = Flask(__name__)
app.config['SECRET_KEY'] = "thisisasecret"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["GEOIPIFY_API_KEY"] = "at_JUgVIVTvno9qku9q1jRTPZFDTzfWA"

simple_geoip = SimpleGeoIP(app)

@app.route("/", methods = ["get"])
def index():
    businessJSON = requests.get("https://www.dl.dropboxusercontent.com/s/uq8udyddz9iq8cc/businesses.json?dl=0").json()
    business = []
    for each in businessJSON['businesses']:
        business.append(each)
    return render_template('index.html', businesses=business)

@app.route("/test")
def test():
    geoip_data = simple_geoip.get_geoip_data()
    print(geoip_data)
    return jsonify(data=geoip_data)

@app.route('/gofundme')
def gofundme():
    return render_template('gofundme.html')

if(__name__ == "__main__"):
    app.run(debug=True)

from flask import Flask, request, render_template, redirect, session, make_response, url_for, flash, jsonify
import requests
import json
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = "thisisasecret"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['GOOGLEMAPS_KEY'] = config.GOOGLEMAPS_KEY

GoogleMaps(app)

@app.route("/", methods = ["get"])
def index():
    locationJSON = requests.get("http://ip-api.com/json/" + "99.228.217.72").json()
    lat = str(locationJSON['lat'])
    lng = str(locationJSON['lon'])

    headers = {
        "Authorization": "Bearer " + config.YELP_KEY
      }

    firstJSON = requests.get("https://api.yelp.com/v3/businesses/search?latitude=" + lat + "&longitude=" + lng + "&categories=localservices&limit=25", headers=headers).json()

    secondJSON = requests.get("https://api.yelp.com/v3/businesses/search?latitude=" + lat + "&longitude=" + lng + "&categories=all&limit=25", headers=headers).json()

    businessJSON = []
    businessJSON.extend(firstJSON['businesses'])
    businessJSON.extend(secondJSON['businesses'])

    markerList = [
        {
            "icon": "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
            "lat":lat,
            "lng":lng,
            'infobox': "Your Approximate Location"
        }
    ]

    for i in businessJSON:
        payload = {
            "icon": "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",
            "lat":i["coordinates"]["latitude"],
            "lng":i["coordinates"]["longitude"],
            'infobox': "<img style='width:150px;height:150px' src=" + i["image_url"]+" />"+"\n"+i['name'],
        }

        markerList.append(payload)

    sndmap = Map(
        identifier="sndmap",
        lat=lat,
        lng=lng,
        style= "height:45vh;margin-bottom:7vh;color:black;",
        markers=markerList
    )

    return render_template('index.html', businesses=businessJSON, sndmap=sndmap)

@app.route("/login")
def login():
    code = request.args.get("code")
    clientID = config.LINKEDIN_CLIENT_ID
    clientSecret = config.LINKEDIN_CLIENT_SECRET
    link = "https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&redirect_uri=http://127.0.0.1:5000/login&client_id=" + clientID + "&client_secret=" + clientSecret + "&code=" + code
    getToken = requests.post(link).json()
    access_token = getToken['access_token']
    resp = make_response(redirect('/jobs'))
    resp.set_cookie("linkedinAuth", access_token)
    return resp

@app.route("/jobs")
def jobs():
    access_token = request.cookies.get("linkedinAuth")
    headers = {
        "Authorization": "Bearer " + access_token
    }
    linkedinJSON = requests.get("https://api.linkedin.com/v2/me", headers=headers).json()
    jobsJSON = requests.get("https://www.dl.dropboxusercontent.com/s/uq8udyddz9iq8cc/businesses.json?dl=0").json()
    return render_template('jobs.html', linkedin=linkedinJSON, jobs=jobsJSON['Jobs'])

@app.route("/news")
def news():
    locationJSON = requests.get("http://ip-api.com/json/" + "99.228.217.72").json()
    lat = str(locationJSON['lat'])
    lng = str(locationJSON['lon'])

    headers = {
        "Authorization": config.RADAR_IO_KEY
      }
    geolink = "https://api.radar.io/v1/geocode/reverse?coordinates="+lat+","+lng
    reverseGeo = requests.get(geolink, headers=headers)
    state = reverseGeo.json()['addresses'][0]['state']
    newslink = "https://newsapi.org/v2/everything?q=(" + state + ")AND(Businesses)&sortBy=publishedAt&from=2020-07-01&apiKey="+ config.NEWS_KEY
    news = requests.get(newslink).json()
    return render_template('news.html', news=news['articles'])


@app.route('/business/<id>')
def business(id):
    locationJSON = requests.get("http://ip-api.com/json/" + "99.228.3.238").json()
    lat = str(locationJSON['lat'])
    lng = str(locationJSON['lon'])
    headers = {
        "Authorization": "Bearer " + config.YELP_KEY
      }

    businessJSON = requests.get("https://api.yelp.com/v3/businesses/" + id, headers=headers).json()
    individualMarkers = [{
            "icon": "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",
            "lat":businessJSON['coordinates']['latitude'],
            "lng":businessJSON['coordinates']['longitude'],
            'infobox': businessJSON['name']
        },
        {
            "icon": "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
            "lat":lat,
            "lng":lng,
            'infobox': "Your Approximate Location"
        }]

    soloMap = Map(
        identifier="sndmap",
        lat=lat,
        lng=lng,
        style= "height:45vh;margin-top:7vh;margin-bottom:7vh;color:black;",
        markers=individualMarkers
    )
    mapsLink = "https://www.google.com/maps?saddr=My+Location&daddr=" +str(businessJSON['coordinates']['latitude'])+","+str(businessJSON['coordinates']['longitude'])

    return render_template('business.html', business=businessJSON, soloMap = soloMap, maplink = mapsLink, phone=businessJSON['phone'], times=businessJSON['hours'][0]['open'], days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

if(__name__ == "__main__"):
    app.run(debug=True)

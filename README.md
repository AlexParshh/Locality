# Locality

## Inspiration

We were inspired to build Locality after witnessing the debacle that the COVID-19 pandemic had brought to small businesses. We wanted to do our part to support the backbone of our economy, since small businesses account for half of the GDP.

## What is Locality  

Locality is a platform to promote local businesses during this COVID-19 Pandemic. As many are now relying on online and delivery companies such as Amazon and eBay, local businneses are losing customers and shutting down very rapidly. The purpose of Locality is to allow users to view and support local businesses instead of large corporations and chains. GoFundMe pages of various businesses are embedded on the site, allowing users to donate money for a good cause. Locality also features a news feed about small businesses in the users location, to help keep everyone educated about the current situations in their communities.

## How to View/Access Locality 

To view Locality in your browser, view: [Locality](http://locality.space/).

## Built With

Locality was built with Python, HTML, CSS, and JavaScript. The micro-web Python framework Flask was used to build the backend.

The APIs we used include:
- [Radar.io API](https://radar.io/product/api)
- [IP Geolocation API](http://ip-api.com)
- [Google Maps API](https://developers.google.com/maps/documentation/javascript/overview)
- [Yelp Businesses API](https://www.yelp.com/developers)
- [News API](https://newsapi.org/)
- [Linkedin API](https://docs.microsoft.com/en-us/linkedin/)

To host Locality, we used Heroku and Domain.com for our custom domain, provided by MLH.

## How It Works

Locality makes use of the user's IP address, and via geolocation and the IP Geolocation API, returns the user's latitude and longitude. Then, these coordinates go through the Yelp Deep Search API and our custom filters to find relevant local businneses in the nearby area as well as relevant local small business news. The locations are sorted by their distance from the user automatically. The Google Maps API was used to add styled markers to businesses near the user's location. We also implemented the sign in with Linkedin via Linkedin Oauth feature which would be used to display relevant jobs based on the user.

The Radar.io API was used to reverse Geocode the user's latitude and longitude, in order to find the provice/state they're in. This information was then used in order to filter for relevant small business news based on user location on our /news page.

## Requirements

The custom modules used: 

- requests==2.22.0
- flask
- gunicorn
- flask_simple_geoip
- flask-googlemaps

## Steps and Commands To Run The Code

```
git clone (or download the files)
```
This will download the files to your local system.
```
cd into the folder via Terminal (Mac) or CMD (Windows)
```
This will direct your terminal window to the folder where the code resides.
```
pip3 install -r requirements.txt
```
This will install all the modules required for our Flask back-end to function. Without these, the app.py file will not run.
```
python3 app.py
```
This will execute our website and will open a local version for you to view on localhost:5000 or 127.0.0.1:5000.

## Challenges We Ran Into

- The first challenge we ran into was finding good API's to source our data to our specifications, however after thorough research we were able to find what we needed. 
- We were also experiencing issues with some of the overall CSS, especially for the interactive Google Maps widget.
- Another challenge we had was implementing actual direct donation links. In order to resolve this, we added static interactive donation features and a "Add Business" button which demonstrates the concept of having businesses providing information to be used for features such as donations.

## What's Next?

- We were planning on adding personalized job recommendations for users who logged in via Linkedin, however, this was not possible since we needed to email and request for access to this API feature, which could take up to 2 weeks. Instead, we added static jobs to prove the concept. We want to add this feature in the nearby future.

- We also want to add a way to encourage consumer spending at particular locations, one way this could have been done was by using the Privacy.com API to help users generate gift cards for the favourite businesses. This was not possible through the sandbox API which we initially thought would be possible during brainstorm.

## What We Learned

- How to utilize the Flask framework to efficiently build a web platform, which includes the Jinja web template engine.
- How to implement the Linkedin Oauth Signin onto a webpage with the use of cookies to store login data.
- How to integrate a domain from domain.com into Heroku using DNS Records and CNAME.
- Hot to properlly use the git terminal.
- How to properlly utilize several API's such as the ones listed in the "Built With" section.

## Authors 

This web app was built by **Shubham Shah**, **Alex Parsh**, and **Aditi Parekh** for the 2020 HackItShipIt Hackathon.

### View the Contributer's Profiles here: 

   - [Shubham Shah](https://github.com/SpikePlayz)
   - [Alex Parsh](https://github.com/AlexParshh)
   - [Aditi Parekh](https://github.com/aditip897)

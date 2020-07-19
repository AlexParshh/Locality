# Locality

## Inspiration

We were inspired to build Locality after witnessing the debacle that the COVID-19 pandemic had brought to small businesses. We wanted to do our part to support the backbone of our economy, since small businesses account for half of the GDP.

## What is Locality  

Locality is a platform to promote local businesses during this COVID-19 Pandemic. As many are now relying on online and delivery companies such as Amazon and eBay, local businneses are losing customers and shutting down very rapidly. The purpose of Locality is to allow users to view and support local businesses instead of large corporations and chains. GoFundMe pages of various businesses are embedded on the site, allowing users to donate money for a good cause. Locality also features a news feed about small businesses in the users location, to help keep everyone educated about the current situations in their communities.

## How to View Locality 

To view Locality in your browser, view: [Locality](http://locality.space/)

## Built With

Locality was built with Python, HTML, CSS, and JavaScript. The micro web Python framework Flask was used to build the backend.

The APIs we used include:
- [Radar.io](https://radar.io/product/api)
- [Google Maps API](https://developers.google.com/maps/documentation/javascript/overview)
- [Yelp](https://www.yelp.com/developers)
- [News Api](https://newsapi.org/)

To host Locality, we used Heroku. 

## How it works

Locality makes use of the user's IP address, and via geolocation, returns the user's latitude and longitude. Then, these coordinates go through the Yelp Deep Search API and our custom filters to find relevant local businneses in the nearby area as well as relevant local small business news. The locations are sorted by their distance from the user automatically. The Google Maps API was used to add styled markers to businesses near the user's location. We also implemented the sign in with Linkedin via Linkedin Oauth feature.

The Radar.io API was used to reverse Geocode the users latitude and longitude, in order to find the provice/state they're in. This information was then used in order to filter for relevant small business news based on user location. 

## Requirements

The modules used: 

- requests==2.22.0
- dropbox
- flask
- gunicorn
- flask_simple_geoip
- flask-googlemaps

## How to get the code running

To get the code running, clone the git repository, open on your computer, make sure all the requirements are installed.
To launch the app cd into the directory containing the app and type "python app.py". Then check your localhoast. 

## Challenges we ran into

The first challenege we ran into was finding good api's to source our data to our specifications, however after thorough research we were able to find what we needed. 
We were also experiencing issues with some of the overall website layout such as the styling for the interactive google maps.
Another challenge we had was implementing actual direct donation links. In order to resolve this, we added static interactive donation features and a "Add Business" button which demonstrates the concept of having businesses providing information to be used for features such as donations.

## Things we want to add

We were planning on adding personalized job recommendations for users who logged in via Linkedin, however, this was not possible since we needed to email and request for access to this API feature, which could take up to 2 weeks. Instead we added static jobs to prove the concept. We want to add this feature in the nearby future.

We also want to add a way to encourage consumer spending at particular locations, one way this could have been done was by using the Privacy.com API to help users generate gift cards for the favourite businesses.

## What we learned

How to utilize the Flask framework to efficiently build a web platform, which includes the Jinja web template engine.
How to implement the Linkedin Oauth Signin onto a webpage with the use of cookies.
How to integrate a domain into Heroku.
Hot to properlly use the git terminal.
How to properlly utilize several API's such as the ones listed in the "Built With" section.

## Authors 

This web app was built by **Shubham Shah**, **Alex Parsh**, and **Aditi Parekh** for the 2020 HackItShipIt Hackathon.

### View the Contributer's Profiles here: 

   - [Shubham Shah](https://github.com/SpikePlayz)
   - [Alex Parsh](https://github.com/AlexParshh)
   - [Aditi Parekh](https://github.com/aditip897)

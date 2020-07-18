# Locality

## What is Locality  

**Locality is a platform to promote local businesses during this COVID-19 Pandemic. As many are now relying on online and delivery companies such as Amazon and eBay, local businneses are losing money and shutting down at a much higher rate.**

**The purpose of Locality is to allow users to view and support local businesses. GoFundMe pages of various businesses are embedded on the site, allowing users to donate money for a good cause.**

## How to View Locality 

To view Locality in your browser, view: [Locality](http://locality.space/)

## Built With

Locality was built with Python, HTML, CSS, and JavaScript. The APIs we used include, [Radar.io](https://radar.io/product/api), [Google Maps API](https://developers.google.com/maps/documentation/javascript/overview), and [Yelp](https://www.yelp.com/developers).


Heroku makes use of the user's IP address, and via geolocation, returns the user's latitude and longitude. Then, these coordinates go through the Yelp Deep Search API and our custom filters to find relevant local businneses in the nearby area. The locations are sorted by their distance from the user automatically. 

The Google Maps API was used to add styled markers to businesses near the user's location. 

The purpose of the Radar.io API in Locality was to reverse geolocate the longitude and latitude of a user's location, to return the region where they are located. The keyword that was returned was then used to filter local news for business names. 


## Modules  

The modules used: 

- [Dropbox](https://www.npmjs.com/package/dropbox)
- [Flask](https://pypi.org/project/Flask/)
- [Gunicorn](https://gunicorn.org/)
- [Flask_simple_geoip](https://pypi.org/project/Flask-Simple-GeoIP/)
- [Flask-googlemaps](https://pypi.org/project/flask-googlemaps/)

## What We Learned

By building Locality, we were introduced to the Radar.io, Google Maps, and Yelp APIs. Because we implemented them into our code, we were able to learn more about their functions and how they work. For example, by studying how Radar.io works, we were able to geolocate users to get their locations. And by using the Google Maps API, we learned how to show markers on the user's nearby locations, have a pop-up when a marker is clicked, and change the marker style.  

Moreover, we learned some more functionalities inside HTML, such as implementing favicons. 

In terms of Python, we determined how to directly send http requests. 

To build Locality, we used Flask, JSON, and some other libraries, languages, and APIs, and not all of us were too experienced working with them. Through this project, we were able to grasp a lot more information about Flask and JSON and therefore, able to implement them into the programming of Locality. Additionally, we learned how to apply the OAuth protocol for Linkedin to fetch data.  

Working on Locality allowed all of us to significantly increase our programming knowledge and develop new skills to build a project that is beneficial to many around the world. 


## What We Would Like to Add 

To take Locality a step forward, we would like to add a feature that allows businesses to connect with Locality and post advertisements, promotion flyers, etc. to have themselves further known. This page would be accessed from the Locality navigation bar and would be organized in a way similar to social media posts. The feature would be very beneficial to businesses, and would also support the purpose of Locality.
   

## Authors 

This web app was built by **Shubham Shah**, **Alex Parsh**,  **Aditi Parekh**, and **Christopher Haley**.

### View the Contributer's Profiles here: 

   - [Shubham Shah](https://github.com/SpikePlayz)
   - [Alex Parsh](https://github.com/AlexParshh)
   - [Aditi Parekh](https://github.com/aditip897)
   - [Christopher Haley](https://github.com/Chalgorithm)

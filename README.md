# Locality

## What is Locality  

Locality is a platform to promote local businesses during this COVID-19 Pandemic. As many are now relying on online and delivery companies such as Amazon and eBay, local businesses are losing money and shutting down at a much higher rate.

The purpose of Locality is to allow users to view and support local businesses. GoFundMe pages of various businesses are embedded on the site, allowing users to donate money for a good cause. Moreover, based on the user's longitude and latitude, the locations of various nearby small businesses appear on a Google Maps as well as on various cards when you scroll down. This lets users learn more about places that might need their support. Moreover, by clicking a business card, you are led to another page on Locality, itself, containing information about the business. This includes its phone number, address, personalized directions, its location on a map in distance to yours, as well as a donate feature. You can also see it's opening and closing times every day in an organized manner. 

You can view an image showing this by looking at the Image Gallery. 

An additional feature on Locality is the News tab on the navigation bar. By clicking it, you are led to a separate page on Locality that uses your location coordinates to return multiple local, country-based, news about the pandemic in general and its impacts on businesses and people. Information appears in cards. These cards contain the publisher, publishing date, article name, and a summary of the article. This feature educates users about the pandemic. 

Plus, on the top-right corner is the sign-in with LinkedIn button. Clicking this would prompt you to sign in to your LinkedIn account. After doing so, you see cards with information on some jobs that are hiring. When you click on a card, you are taken to that job posting's page where you can learn more and apply. 

## How to View Locality 

To view Locality in your browser, view: [Locality](http://locality.space/)

We also create a Devpost Image Gallery for our project where you can see images of different sections/pages on Locality.

## Built With

Locality was built with Python, HTML, CSS, and JavaScript. The APIs we used include, [Radar.io](https://radar.io/product/api), [Google Maps API](https://developers.google.com/maps/documentation/javascript/overview),  [Yelp](https://www.yelp.com/developers), and [News API](https://newsapi.org/)

Heroku makes use of the user's IP address, and via geolocation, returns the user's latitude and longitude. Then, these coordinates go through the Yelp Deep Search API and our custom filters to find relevant local businesses in the nearby area. The locations are sorted by their distance from the user automatically. 

The News API used the user's location and pandemic and business keywords to return local news about the situation. 

The Google Maps API was used to add styled markers to businesses located near the user's location as well as a green marker on the user's current approximate location. 

The purpose of the Radar.io API in Locality was to reverse geolocate the longitude and latitude of a user's location, to return the region where they are located. The keyword that was returned was then used to filter local news for business names. 

We connected our web app to a Domain.com domain using Heroku.


## Modules  

The modules used: 

- [Dropbox](https://www.npmjs.com/package/dropbox)
- [Flask](https://pypi.org/project/Flask/)
- [Gunicorn](https://gunicorn.org/)
- [Flask_simple_geoip](https://pypi.org/project/Flask-Simple-GeoIP/)
- [Flask-googlemaps](https://pypi.org/project/flask-googlemaps/)

## What We Learned

By building Locality, we were introduced to the Radar.io, Google Maps, and Yelp APIs. Because we implemented them into our code, we were able to learn more about their functions and how they work. For example, by studying how Radar.io works, we were able to geolocate users to get their locations. And by using the Google Maps API, we learned how to show markers on the user's nearby locations, have a pop-up when a marker is clicked, and change the marker style.  Plus, by learning how to use the News API, we were able to showcase news related to small businesses during this pandemic on the news page of our web app. 

Moreover, we learned some more functionalities inside HTML and CSS, such as some new styling techniques. 
By building Locality, we all learned a lot more about UI/UX design.

In terms of Python, we determined how to directly send HTTP requests. 

To build Locality, we used Flask, JSON, and some other libraries, languages, and APIs, and not all of us were too experienced working with them. Through this project, we were able to grasp a lot more information about Flask and JSON and therefore, able to implement them into the programming of Locality. Additionally, we learned how to apply the OAuth protocol for Linkedin to allow users to sign in, fetch some account data, and return job postings for them.  

Working on Locality allowed all of us to significantly increase our programming knowledge and develop new skills to build a project that is beneficial to many around the world. 


## What We Would Like to Add 

To take Locality a step forward, we would like to add a feature that allows businesses to connect with Locality and post advertisements, promotion flyers, etc. to have themselves further known. This page would be accessed from the Locality navigation bar and would be organized in a way similar to social media posts. The feature would be very beneficial to businesses, and would also support the purpose of Locality.

In the future, we would also like to add a feature that lets users get gift cards on Locality itself to use for donating to local businesses. This would be done using the Privacy.com API. 
   

## Acknowledgements

We would like to thank MLH and HackItShipIt for providing us with an opportunity to use and build upon our programming knowledge to develop a web app that is beneficial to tons of people around the world during this pandemic.

## Authors 

This web app was built by **Shubham Shah**, **Alex Parsh**,  **Aditi Parekh**.

### View the Contributer's Profiles here: 

   - [Shubham Shah](https://github.com/SpikePlayz)
   - [Alex Parsh](https://github.com/AlexParshh)
   - [Aditi Parekh](https://github.com/aditip897)

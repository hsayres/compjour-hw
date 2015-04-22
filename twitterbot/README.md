# **Pitch--**

Anyone who tweets at my bot with the hashtag **#feedme**-- and includes an **address** in the tweet if they do not have geolocation enabled-- will receive a tweet back with the name of the **highest rated restaurant near them**. The user can specify **#xmiles**, where x is the number of miles around them (i.e. the radius if they are the center), that my bot searches for a restaurant. The default is 5 miles.

# **Steps--**

1. Bot checks Twitter API endpoint of Twitter's status/ mentions API ([see here](https://dev.twitter.com/rest/reference/get/statuses/mentions_timeline)).
2. For each Tweet, the bot checks to see if the #feedme hashtag was used, and records the user's screen name and the ID of the tag.
3. If the location is in the other text in the tweet, that is the location that is used. If not, and the tweet has geolocation enabled, that is the location. If no location is included and geolocating is not enabled, the bot has some sort of witty response.
4. If the location is an address string, it will use the Google Maps Geocoding API to get the longitude and latitude coordinates ([see here](https://developers.google.com/maps/documentation/geocoding/)).
5. It will use Yelp's Search API to return the top rated restaurant within a specified distance from the provided longitude and latitude coordinates ([see here](https://www.yelp.com/developers/documentation/v2/search_api)).
6. It will extract that restaurant's name and address
7. It will use Twitter's statuses/ update endpoint and reply back to the user with the name and address ([see here](https://dev.twitter.com/rest/reference/post/statuses/update)).

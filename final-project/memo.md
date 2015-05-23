## **Pitch--**

Who are your neighbors? My site will tell you just that-- what crimes are being convicted in your neighborhood, why the people down the hall got evicted, and even how many homeless guys are shitting outside your apartment.

## **The old way--**
You used to have to find out via word of mouth, walking outside your apartment and taking a wiff, and googling the names of your neighbors to uncover any arrest records.

## **The new way--**
You visit my website, zoom in to your neighborhood, and the information is right there.

## **Data details--**

###_Where does the data come from? How is it collected?_###
Some data comes from eviction notices filed with the San Francisco Rent Board per San Francisco Administrative (see here: https://data.sfgov.org/Housing-and-Buildings/Eviction-Notices/5cei-gny5), crime incidents are derived from SFPD Crime Incident Reporting system and are updated on a daily basis (see here: https://data.sfgov.org/Public-Safety/Map-Crime-Incidents-from-1-Jan-2003/gxxq-x39z); and the poop information comes from a human waste report on SF Open Data, and data is recorded via voice-ins and twitter (see here: https://data.sfgov.org/City-Management-and-Ethics/-Duplicate-Human-Waste-/eswg-wnti).


###_What data-cleaning/ processing needs to be done?_###
All data will be downloaded and converted into CSVs. Some of the location variables will need to be changed to GPS coordinates that I can use with Google Maps API.

###_How will the data be stored?_###
I will keep the data in a Google spreadsheet and just have the HTML read it in.

##Who else has done it and how is my attempt better?##
There a few different websites that aggregate crime data including crimemapping.com, sanfrancisco.crimespotting.org, http://www.city-data.com/crime/crime-San-Francisco-California.html, and http://www.neighborhoodscout.com/ca/san-francisco/crime/. My site will be better because it will be interactiive, and include more sources of crime and information about devious neighbor activity than the other sites do. It will be focused on San Francisco so it will be more navigateable.

## Pre-mortem-- ##
My biggest challenge will be designing the cleanest way to display all types of data without taking away from one information source. I'm trying to include a lot of different information, so can't have one type of crime data take away from the readability of another type.

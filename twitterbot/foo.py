def find_first_feedme_tagged_mention(mentions):
	"""
    Given a list of tweets (ostensibly from the mentions-API-endpoint),
    find the earliest one that has the #FEEDME hashtag in it
    
    Arguments:
        mentions (list): a list of Twitter tweet objects that are dicts
    
    Returns:
        if any such tweet is found, return that tweet (dict)
        else, return None
    """

def latest_feedme_reply(tweets):
    """
    Given a list of tweets (ostensibly from user_timeline API endpoint),
    find the earliest one that has the #FEEDME hashtag in it
    
    Arguments:
        tweets (list): a list of Twitter tweet objects that are dicts
    
    Returns:
        if any such tweet is found, return that tweet (dict)
        else, return None
    """

def make_feedme_text():
	"""
    Create a custom #FEEDME  message
    Arguments:
        None
    Returns:
        A text string with the #FEEDME hashtag and something extra special
    """

def get_closest_restaurant(longitude, latitude):
    """
    Given a location, returns the name of a restaurant and its address in string form.
    Arguments:
        Location-- longitude and latitude, as specified by the user if they tweet an
        address, the bot finds the longitude and latitude using the Google maps API.
        If they don't tweet an address but the tweet is geolocated, it uses that latitude
        and longitude.
    Returns:
        A text string with the name of a restaurant and its address
    """

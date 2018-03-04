from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import sys

# read inputs for executing twitter search
tvShowTitle = sys.argv[1]
artistName = sys.argv[2]
movieTitle = sys.argv[3]

# create an instance of the TV Show API
print("3 Most Latest Tweets for TV Show: " + tvShowTitle)
api_instance = swagger_client.TVShowsApi()
try:
    api_response = api_instance.get_tv_show_tweets_by_title(tvShowTitle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling API: %s\n" % e)

print()

# create an instance of the Music API
print("3 Most Latest Tweets for Music Artist: " + artistName)
api_instance = swagger_client.MusicApi()
try:
    api_response = api_instance.get_music_tweets_by_artist(artistName)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling API: %s\n" % e)

print()

# create an instance of the Movies API
print("3 Most Latest Tweets for Movie Title: " + movieTitle)
api_instance = swagger_client.MoviesApi()
try:
    api_response = api_instance.get_movie_tweets_by_title(movieTitle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling API: %s\n" % e)

print()

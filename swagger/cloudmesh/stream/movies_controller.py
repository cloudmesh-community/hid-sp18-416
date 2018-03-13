import connexion
import six
import tweepy
from tweepy import Stream
import json
import yaml
from pprint import pprint
import os
import ast

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server.models.tweet import Tweet
from swagger_server import util


class StreamListener(tweepy.StreamListener):
    tweet_count = 0
    max_tweet_count = 3

    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        self.tweet_count = self.tweet_count + 1
        if self.tweet_count <= self.max_tweet_count:
            all_data = json.loads(data)
            tweet = all_data["text"]
            likes_for_original = 0
            retweets_for_original = 0
            is_retweet = 'retweeted_status' in all_data
            if is_retweet:
                likes_for_original = \
                    all_data["retweeted_status"]["favorite_count"]
                retweets_for_original = all_data["retweeted_status"][
                    "retweet_count"]
            username = all_data["user"]["screen_name"]
            official = all_data["user"]["verified"]
            created_at = all_data["created_at"]
            id = all_data["id"]

            tweet_obj = Tweet(id, username, tweet, is_retweet,
                              retweets_for_original, likes_for_original,
                              created_at, official)

            with open('tweet' + str(self.tweet_count) + '.txt', 'w') as f:
                f.write(str(tweet_obj))

            return True

        else:
            return False


class Authentication:
    @staticmethod
    def authenticate():
        filepath = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(filepath, 'credentials.yaml')
        credentials = yaml.load(open(filename))
        consumer_key = credentials['consumer_key']
        consumer_secret = credentials['consumer_secret']
        access_token = credentials['access_token']
        access_token_secret = credentials['access_token_secret']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        return auth


def get_movie_tweets_by_title(movieTitle):  # noqa: E501
    """Find latest tweets related to a movie

    Returns latest tweets related to a movie # noqa: E501

    :param movieTitle: Title of Movie
    :type movieTitle: str

    :rtype: Movie
    """
    auth = Authentication.authenticate()

    twitterStream = Stream(auth, StreamListener())
    twitterStream.filter(track=[movieTitle], languages=["en"])

    try:
        movie_arr = []
        for i in range(1, (StreamListener.max_tweet_count + 1)):
            text = open('tweet' + str(i) + '.txt', 'r').read().replace(
                "\\n", "")
            twitter_dict = ast.literal_eval(text)
            tweet_obj = Tweet(twitter_dict["id"], twitter_dict["user"],
                              twitter_dict["tweet"], twitter_dict[
                                  "is_retweet"], twitter_dict[
                                  "retweets_for_original"], twitter_dict[
                                  "likes_for_original"], twitter_dict[
                                  "created_at"], twitter_dict["official"])
            movie_arr.append(tweet_obj)
        return Movie(movieTitle, list(movie_arr))
    except:
        return Error.message

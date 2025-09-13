# Tweepy is a Python library for accessing the Twitter API. It allows you to interact with Twitter data, such as posting tweets, reading timelines, and managing followers.

import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)

search = "zerotomastery"
numberOfTweets = 2


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)


# Follow
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.name == 'nice_person':
        print(follower.name)
        follower.follow()
        print('You are now following {}'.format(follower.name))


# Retweet
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# Send DM
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.name == 'nice_person':
        print(follower.name)
        api.send_direct_message(follower.id, 'Hello! This is a DM.')
        print('You sent a DM to {}'.format(follower.name))

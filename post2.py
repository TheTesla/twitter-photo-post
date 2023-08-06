
import tweepy
import secrets

tweepy_auth = tweepy.OAuth1UserHandler(
    secrets.twitter_auth_keys['consumer_key'],
    secrets.twitter_auth_keys['consumer_secret'],
    secrets.twitter_auth_keys['access_token'],
    secrets.twitter_auth_keys['access_token_secret']
)

tweepy_api = tweepy.API(tweepy_auth)


client = tweepy.Client(
    consumer_key=secrets.twitter_auth_keys['consumer_key'], #API Key
    consumer_secret=secrets.twitter_auth_keys['consumer_secret'], #API Secret
    access_token=secrets.twitter_auth_keys['access_token'],
    access_token_secret=secrets.twitter_auth_keys['access_token_secret']
)

text = 'Many men from Indonesia are wearing inflatable pants.'

post = tweepy_api.simple_upload('Many men from Indonesia are wearing inflatable pants._HEIGHT_512_WIDTH_512_SEED_2.png')
print(post)
print(post.media_id)

response = client.create_tweet(text=text, media_ids=[post.media_id])

print(f"https://twitter.com/user/status/{response.data['id']}")


#import oauth2 as oauth
from twitter import Twitter, OAuth
#import simplejson as json

CONSUMER_KEY='mykey'
CONSUMER_SECRET='mysecret'
tokenkey='mytokenkey'
tokensecret='mytokensecret'


t = Twitter(
auth=OAuth(tokenkey,tokensecret, CONSUMER_KEY,CONSUMER_SECRET))

tweets = t.statuses.user_timeline(screen_name="realDonaldTrump")

f = open('OrangeTweets.txt', 'w')
for t in tweets:
    text = t["text"]
    create_time = t["created_at"]
    f.write(create_time + ',' + text.encode('ascii','ignore')+'\n')
f.close()
from twython import Twython, TwythonError
from datetime import date, timedelta
import twitter_settings
import sentiment


OAUTH_TOKEN = twitter_settings.oauth_token
OAUTH_TOKEN_SECRET = twitter_settings.oauth_token_secret

APP_KEY = twitter_settings.consumer_key
APP_SECRET = twitter_settings.consumer_secret

username = twitter_settings.username

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
try:
    user_timeline = twitter.get_user_timeline(screen_name=username, count=200)
except TwythonError as e:
    print e

date_str = str((date.today() - timedelta(days=0)).strftime('%a %b %d'))
date_key = str((date.today() - timedelta(days=0)).strftime('%y%m%d'))


tweet_count = 0
total_sentiment_score = 0
tweets = ""


for i in range(0, len(user_timeline)):
    if date_str in user_timeline[i]['created_at']:
        tweet_count += 1
        sentiment_score = sentiment.get_sentiment(user_timeline[i]['text'])
        total_sentiment_score += sentiment_score
        tweets += user_timeline[i][
            'text'] + ' - ' + str(sentiment_score) + '\n'
    else:
        break
if tweet_count > 0:
    avg_sentiment_score = total_sentiment_score / tweet_count
    print "Today's tweet count for " + username + ": " + str(tweet_count)
    print('\nAvg Sentiment Score : %.2f' % avg_sentiment_score)
else:
    print 'No tweets for ' + username + ' @ '

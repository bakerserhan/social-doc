import sys
import json
import re
import twitter_settings

def get_sentiment(text):
  # load a tab delimited dict of sentiment scores
  afinnfile = open(twitter_settings.sentiment_file)
  scores = {}
  for line in afinnfile:
    term, score  = line.split("\t")
    scores[term] = int(score)

  score = 0    
  tweet_text = text.split()
  for word in tweet_text:
    if re.match("^[A-Za-z0-9_-]*$", word):
      score += scores.get(word, 0)
  return float(score)

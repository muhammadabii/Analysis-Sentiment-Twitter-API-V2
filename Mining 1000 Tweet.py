import tweepy
import config
import csv

# Retrive tweet
client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = 'Emmeril Kahn lang:id -is:retweet'  # query tweet

response = tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100,
                            tweet_fields=['created_at', 'lang'],
                            expansions=['author_id']).flatten(limit=1000)

fname = 'dataset'
with open('%s.csv' % fname, 'w', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['tweet_id', 'author_id', 'created_at', 'lang', 'text'])
    for tweet in response:
        w.writerow([tweet.id, tweet.author_id, tweet.created_at, tweet.lang, tweet.text])

print('%s.csv saved!' % fname)

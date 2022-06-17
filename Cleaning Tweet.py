import pandas as pd
import re
from googletrans import Translator

trans = Translator().translate
df = pd.read_csv('dataset.csv')


# Cleaning the dataset.csv
def clean_tweet(tweet):
    tweet = re.sub(r'\d+', '', tweet)  # remove numbers
    tweet = re.sub(r'[\u0600-\u06FF[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|'
                   r'[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]', '', tweet)  # remove arabic characters https://gist.github.com/Humoud/f40f58cd85c5935a444c
    tweet = tweet.replace("#", "").replace("_", " ")  # Remove #hashtag sign but keep the text
    tweet = re.sub(r'@[A-Za-z0-9]+', "", tweet)  # Remove @username
    tweet = re.sub(r'http\S+', ' ', tweet)  # Remove http links
    tweet = re.sub(r'www\S+', ' ', tweet)  # Remove www links
    tweet = re.sub(r'bit\Sly\S*\S', ' ', tweet)  # Remove bit.ly links
    tweet = re.sub(r'[^\w\s]', ' ', tweet)  # Remove punctuation and special characters
    tweet = re.sub(r'\s+', ' ', tweet)  # Remove multiple spaces
    return tweet


def clean_df(column_name):
    clean_list = []
    for tweet in df[column_name]:
        clean_tweets = clean_tweet(tweet)
        clean_list.append(clean_tweets)  # Append cleaned tweets to a clean_list
    df[column_name] = clean_list  # Replace the original column with the clean_list
    translated_text = []
    for tweet in df['text']:
        tanslate_tweet = trans(tweet, dest='en')
        tweet_text = tanslate_tweet.text
        translated_text.append(tweet_text)
    df['en_text'] = translated_text
    date_list = []
    for date in df['created_at']:
        date = str(date)[:10]  # Keep only the date from the created_at column (YYYY-MM-DD)
        date_list.append(date)  # Append dates to a date_list
    df['created_at'] = date_list  # Replace the original column with the date_list
    return df  # Return the cleaned dataframe


clean_df('text')  # use the clean_df function to clean the text column of the dataset.csv
df.drop_duplicates(subset=['text'], keep='first', inplace=True)  # Drop duplicate tweets
df.to_csv('dataset_clean.csv', index=False)  # save the cleaned dataset to a new csv file called dataset_clean.csv
print('dataset_clean.csv saved!')

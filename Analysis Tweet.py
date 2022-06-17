from flair.data import Sentence
from flair.models import TextClassifier
import pandas as pd


df = pd.read_csv('dataset_clean.csv')
classifier = TextClassifier.load('sentiment')


def add_sentiment():
    sentiment_column_n = []
    sentiment_column_l = []
    for t in df['en_text']:
        sentence = Sentence(t)
        classifier.predict(sentence)
        numeric_score = sentence.score
        label_score = sentence.tag
        sentiment_column_n.append(numeric_score)
        sentiment_column_l.append(label_score)
    df['Sentiment Outcome'] = sentiment_column_l
    df['Confidence Score'] = sentiment_column_n


add_sentiment()  # add sentiment to the dataframe

sen_positive = 0
sen_negative = 0
for sen in df['Sentiment Outcome']:  # count the number of positive and negative tweets
    if sen == 'POSITIVE':
        sen_positive += 1
    else:
        sen_negative += 1
print('Count Positive:', sen_positive)
print('Count Negative:', sen_negative)

if sen_positive > sen_negative:  # check if the number of positive tweets is greater than the number of negative tweets
    print('Sentiment is Positive')
elif sen_positive < sen_negative:
    print('Sentiment is Negative')
else:
    print('Sentiment is Neutral')

# save the cleaned dataset to a new csv file called Analysis Tweet.csv
df.to_csv('Analysis Tweet.csv', index=False)

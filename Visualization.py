import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Analysis Tweet.csv')

# Create a dataframe with the positive and negative counts and dates
pos = df['Sentiment Outcome'].apply(lambda x: 1 if x == 'POSITIVE' else 0)
neg = df['Sentiment Outcome'].apply(lambda x: 1 if x == 'NEGATIVE' else 0)
df_sentiment = pd.DataFrame({'created_at': df['created_at'], 'positive': pos, 'negative': neg})
sen = df_sentiment.groupby('created_at').sum()
# Create value counts for the positive and negative counts
positive = df['Sentiment Outcome'].value_counts()['POSITIVE']
negative = df['Sentiment Outcome'].value_counts()['NEGATIVE']


# create pie chart of the number of positive and negative tweets
plt.pie([positive, negative], labels=['Positive', 'Negative'], autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Sentiment Analysis')
plt.text(1, 1, 'Positive: %d\nNegative: %d' % (positive, negative), ha='center')
plt.show()

# Create plot of the number of positive and negative tweets per day
fig, ax = plt.subplots()
ax.plot(sen['positive'], color='b', label='Positive')
ax.plot(sen['negative'], color='r', label='Negative')
ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Number of Tweets')
ax.set_title('Sentiment Analysis')
plt.show()

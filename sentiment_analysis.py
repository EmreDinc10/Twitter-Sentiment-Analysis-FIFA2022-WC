"""
Module docstring
"""

import re
import pandas as pd
from textblob import TextBlob

def analyze_sentiments(search_text):
    df = pd.read_csv('fifa2022.csv')
    df = df[df['full_text'].str.contains(search_text, case=False, na=False)]

    # Define the sentiment analysis function
    def get_sentiment(tweet):
        analysis = TextBlob(tweet)
        if analysis.sentiment.polarity > 0:
            return 'Positive'
        elif analysis.sentiment.polarity == 0:
            return 'Neutral'
        else:
            return 'Negative'

    # Apply the function to the DataFrame
    df['Sentiment'] = df['full_text'].apply(get_sentiment)

    # Calculate the percentages
    sentiment_counts = df['Sentiment'].value_counts(normalize=True)
    positive = round(sentiment_counts.get('Positive', 0.0) * 100, 1)
    neutral = round(sentiment_counts.get('Neutral', 0.0) * 100, 1)
    negative = round(sentiment_counts.get('Negative', 0.0) * 100, 1)

    # Return the percentages
    return [positive, neutral, negative]

print(analyze_sentiments("football")[1])
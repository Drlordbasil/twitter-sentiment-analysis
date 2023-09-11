import matplotlib.pyplot as plt
import tweepy
from collections import Counter
Here are some optimizations for the Python script:

1. Use a main() function: Move the functionality inside the if __name__ == "__main__" block into a separate main() function. This will improve readability and allow for better code organization.

```python


def main():
    query = input(
        "Enter a keyword to perform sentiment analysis on social media posts: ")
    sentiment_analysis(query)


if __name__ == "__main__":
    main()
```

2. Combine the get_tweets() and preprocess_tweets() functions: Instead of making separate functions for fetching tweets and preprocessing them, combine them into a single function. This will reduce unnecessary function calls and improve efficiency.

```python


def get_and_preprocess_tweets(api, query, count=100):
    try:
        fetched_tweets = api.search(q=query, count=count)
        cleaned_tweets = []
        for tweet in fetched_tweets:
            cleaned_tweet = ''.join(
                char for char in tweet.text if char.isalnum() or char.isspace())
            cleaned_tweets.append(cleaned_tweet)
        return cleaned_tweets
    except tweepy.TweepError as e:
        print("Error : " + str(e))


```

3. Use a Counter instead of a dictionary for sentiment_counts: Replace the sentiment_counts dictionary with a Counter object from the collections module. This will simplify the sentiment analysis and eliminate the need for manual tracking of sentiment counts.

```python


def analyze_sentiment(cleaned_tweets):
    sentiment_counts = Counter()
    for tweet in cleaned_tweets:
        sentiment = get_tweet_sentiment(tweet)
        sentiment_counts[sentiment] += 1
    return sentiment_counts


```

4. Use list comprehension for creating the tweets list: Instead of using a loop to create the tweets list with a dictionary comprehension, use a list comprehension directly. This will make the code more concise.

```python
tweets = [{'text': tweet.text, 'sentiment': get_tweet_sentiment(
    tweet.text)} for tweet in fetched_tweets]
```

5. Remove unused imports: Remove the unused imports for matplotlib.pyplot and textblob. This will reduce the overhead of unnecessary imports.

6. Remove redundant comments: Remove comments that simply repeat what the code is doing. Comments should usually explain why the code is doing something, not what it is doing.

7. Use a try -except -else block: Instead of having the try -except block in the get_and_preprocess_tweets() function, use a try -except -else block. This will make the code more structured and easier to understand.

Here's the optimized code:

```python

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'


def authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def get_and_preprocess_tweets(api, query, count=100):
    try:
        fetched_tweets = api.search(q=query, count=count)
        cleaned_tweets = [''.join(char for char in tweet.text if char.isalnum(
        ) or char.isspace()) for tweet in fetched_tweets]
        return cleaned_tweets
    except tweepy.TweepError as e:
        print("Error : " + str(e))


def get_tweet_sentiment(tweet):
    analysis = TextBlob(tweet)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity == 0:
        return 'neutral'
    else:
        return 'negative'


def plot_sentiment_pie_chart(sentiment_counts):
    labels = list(sentiment_counts.keys())
    sizes = list(sentiment_counts.values())
    colors = ['green', 'yellow', 'red']
    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title("Sentiment Analysis: Social Media Posts")
    plt.show()


def analyze_sentiment(cleaned_tweets):
    sentiment_counts = Counter()
    for tweet in cleaned_tweets:
        sentiment = get_tweet_sentiment(tweet)
        sentiment_counts[sentiment] += 1
    return sentiment_counts


def preprocess_tweets(tweets):
    cleaned_tweets = [''.join(char for char in tweet['text'] if char.isalnum(
    ) or char.isspace()) for tweet in tweets]
    return cleaned_tweets


def sentiment_analysis(query):
    api = authenticate()
    tweets = get_and_preprocess_tweets(api, query)
    cleaned_tweets = preprocess_tweets(tweets)
    sentiment_counts = analyze_sentiment(cleaned_tweets)
    plot_sentiment_pie_chart(sentiment_counts)


def main():
    query = input(
        "Enter a keyword to perform sentiment analysis on social media posts: ")
    sentiment_analysis(query)


if __name__ == "__main__":
    main()
```

These optimizations should help improve the performance and readability of the Python script.

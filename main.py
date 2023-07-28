import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'


def authenticate():
    # Authenticating with Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def get_tweets(api, query, count=100):
    # Fetching tweets based on query
    try:
        fetched_tweets = api.search(q=query, count=count)
        tweets = [{'text': tweet.text, 'sentiment': get_tweet_sentiment(
            tweet.text)} for tweet in fetched_tweets]
        return tweets
    except tweepy.TweepError as e:
        print("Error : " + str(e))


def get_tweet_sentiment(tweet):
    # Analyzing sentiment using TextBlob
    analysis = TextBlob(tweet)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity == 0:
        return 'neutral'
    else:
        return 'negative'


def plot_sentiment_pie_chart(sentiment_counts):
    # Plotting pie chart of sentiment distribution
    labels = list(sentiment_counts.keys())
    sizes = list(sentiment_counts.values())
    colors = ['green', 'yellow', 'red']
    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title("Sentiment Analysis: Social Media Posts")
    plt.show()


def preprocess_tweets(tweets):
    # Preprocessing tweets
    cleaned_tweets = []
    for tweet in tweets:
        cleaned_tweet = ''.join(
            char for char in tweet['text'] if char.isalnum() or char.isspace())
        cleaned_tweets.append(cleaned_tweet)
    return cleaned_tweets


def analyze_sentiment(cleaned_tweets):
    # Sentiment analysis
    sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
    for tweet in cleaned_tweets:
        sentiment = get_tweet_sentiment(tweet)
        sentiment_counts[sentiment] += 1
    return sentiment_counts


def sentiment_analysis(query):
    # Authenticating with Twitter API
    api = authenticate()

    # Collecting social media posts
    tweets = get_tweets(api, query)

    # Preprocessing tweets
    cleaned_tweets = preprocess_tweets(tweets)

    # Sentiment analysis
    sentiment_counts = analyze_sentiment(cleaned_tweets)

    # Visualization
    plot_sentiment_pie_chart(sentiment_counts)


# Main driver function
if __name__ == "__main__":
    query = input(
        "Enter a keyword to perform sentiment analysis on social media posts: ")
    sentiment_analysis(query)

import tweepy
import re

consumer_key = "usVkDJZc177AqydGU******"
consumer_secret = "GfWmpMd99wGQNNZv89yftQjFy3EoSCsSlKAsuQBJ704k******"
access_token = "549353393-JwYmPTKX6uZw74JK0dBqZRJqvGLvjTxIr6******"
access_token_secret = "BegmNEQgn7qBh6qlvK5IJrWNMfApuZwYWX1zVWW******"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


search_query = "Nigeria news"
num_tweets = 1500  # Set the number of tweets to scrape

tweets = tweepy.Cursor(api.search, q=search_query, lang="en").items(num_tweets)

sports_keywords = ["sports", "football", "basketball", "tennis"]
entertainment_keywords = ["movies", "music", "celebrities", "gossip"]
politics_keywords = ["politics", "government", "elections", "president"]
tech_keywords = ["Artificial Intelligence", "technologies", "cybersecurity", "Cryptocurrency"]
business_keywords = ["Economy", "Stock Market", "Entrepreneurship", "revenue"]

categorized_tweets = {
    "sports": [],
    "entertainment": [],
    "politics": [],
    "tech": [],
    "business": []
}

for tweet in tweets:
    text = tweet.text.lower()

    if any(keyword in text for keyword in sports_keywords):
        categorized_tweets["sports"].append(text)
    elif any(keyword in text for keyword in entertainment_keywords):
        categorized_tweets["entertainment"].append(text)
    elif any(keyword in text for keyword in politics_keywords):
        categorized_tweets["politics"].append(text)
    elif any(keyword in text for keyword in politics_keywords):
        categorized_tweets["tech"].append(text)
    else:
        categorized_tweets["business"].append(text)



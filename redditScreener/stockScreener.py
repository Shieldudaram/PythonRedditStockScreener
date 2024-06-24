import praw
import re
from collections import Counter

# Initialize Reddit API
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT')

# Function to scrape Reddit data
def get_reddit_posts(subreddit, limit=100):
    posts = []
    for submission in reddit.subreddit(subreddit).hot(limit=limit):
        posts.append(submission.title)
    return posts

# Function to filter tickers
def filter_tickers(posts):
    tickers = []
    pattern = re.compile(r'\b[A-Z]{1,4}\b')
    for post in posts:
        found_tickers = pattern.findall(post)
        tickers.extend(found_tickers)
    return tickers

# Function to count ticker occurrences
def count_ticker_occurrences(tickers):
    return Counter(tickers)

# Main function to execute the script
def main(subreddit='wallstreetbets', post_limit=100):
    posts = get_reddit_posts(subreddit, post_limit)
    tickers = filter_tickers(posts)
    ticker_counts = count_ticker_occurrences(tickers)
    print(ticker_counts)

# Execute the main function
if __name__ == "__main__":
    main()

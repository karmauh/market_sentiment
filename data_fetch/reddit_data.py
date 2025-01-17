import praw

def get_reddit_posts(subreddit, keyword, limit=10):
    reddit = praw.Reddit(
        client_id='',
        client_secret='',
        user_agent='market_sentiment_app',
    )

    # Pobieranie postów
    posts = reddit.subreddit(subreddit).search(keyword, limit=limit)
    return [post.title for post in posts]

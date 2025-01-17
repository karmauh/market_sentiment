from textblob import TextBlob

def analyze_sentiment(posts):
    polarity_scores = []
    positive_count = 0
    negative_count = 0

    for post in posts:
        analysis = TextBlob(post)
        polarity_scores.append(analysis.sentiment.polarity)  # Zakres: -1 (negatywne) do 1 (pozytywne)

        if analysis.sentiment.polarity > 0:
            positive_count += 1
        elif analysis.sentiment.polarity < 0:
            negative_count += 1

    average_polarity = sum(polarity_scores) / len(polarity_scores) if polarity_scores else 0
    return average_polarity, positive_count, negative_count

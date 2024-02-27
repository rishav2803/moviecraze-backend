from textblob import TextBlob


def sentiment_analysis(tweet):
    def getSubjectivity(text):
        return TextBlob(text).sentiment.subjectivity

    def getPolarity(text):
        return TextBlob(text).sentiment.polarity

    tweet['TextBlob_Subjectivity'] = tweet['tweet'].apply(getSubjectivity)
    tweet['TextBlob_Polarity'] = tweet['tweet'].apply(getPolarity)

    def getAnalysis(score):
        if score < 0:
            return 'Negative'
        elif score == 0:
            return 'Neutral'
        else:
            return 'Positive'

    tweet['TextBlob_Analysis'] = tweet['TextBlob_Polarity'].apply(getAnalysis)
    print(tweet)

    return 'Helo world'

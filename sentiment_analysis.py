import re
import pickle
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


class SentimentAnalysis:
    def __init__(self):
        self.nlp_model = load_model("text_classification.h5")

        with open('tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)

    def remove_users(self, tweet):
        """
        Takes a string and removes retweet and @user information.
        """
        tweet = re.sub('(RT\s@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)  # remove re-tweet
        tweet = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)  # remove tweeted at
        return tweet

    def remove_hashtags(self, tweet):
        """
        Takes a string and removes any hash tags.
        """
        tweet = re.sub('(#[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)  # remove hash tags
        return tweet

    def remove_av(self, tweet):
        """
        Takes a string and removes AUDIO/VIDEO tags or labels.
        """
        tweet = re.sub('VIDEO:', '', tweet)  # remove 'VIDEO:' from start of tweet
        tweet = re.sub('AUDIO:', '', tweet)  # remove 'AUDIO:' from start of tweet
        return tweet

    def predict(self, tweet):
        tweet = tweet.lower()
        tweet = re.sub('[^a-zA-z0-9\s]','',tweet)
        tweet = self.remove_hashtags(tweet)
        tweet = self.remove_users(tweet)
        tweet = self.remove_av(tweet)

        tweet = self.tokenizer.texts_to_sequences(tweet)
        tweet = pad_sequences(tweet)

        sentiment = self.nlp_model.predict(tweet, batch_size=1)[0]

        return self.convertToString(np.argmax(sentiment))

    def convertToString(self, modelOutput):
        if modelOutput == 0:
            out = "Extremely Negative"
        elif modelOutput == 1:
            out = 'Extremely Positive'
        elif modelOutput == 2:
            out = "Negative"
        elif modelOutput == 3:
            out = "Neutral"
        elif modelOutput == 4:
            out = "Positive"
        else:
            out = "Neutral"

        return out
        
        









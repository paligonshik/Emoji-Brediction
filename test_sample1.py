from textblob import TextBlob
import pytest
# def extract_sentiment(text: str):
#         '''Extract sentiment using textblob. 
#         Polarity is within range [-1, 1]'''

#         text = TextBlob(text)

#         return text.sentiment.polarity


# def extract_sentiment(text: str):
#         '''Extract sentiment using textblob. 
#         Polarity is within range [-1, 1]'''

#         text = TextBlob(text)

#         return text.sentiment.polarity

# def test_extract_sentiment():

#     text = "I think this song is just a great song"

#     sentiment = extract_sentiment(text)

#     assert sentiment < 0


#sentiment.py

# def test_extract_sentiment_positive():

#     text = "I think you will perform very best"

#     sentiment = extract_sentiment(text)

#     assert sentiment > 0

# def test_extract_sentiment_negative():

#     text = "I hate you, you dissapoitned me"

#     sentiment = extract_sentiment(text)

#     assert sentiment > 0



def extract_sentiment(text: str):
        '''Extract sentiment using textblob. 
        Polarity is within range [-1, 1]'''

        text = TextBlob(text)

        return text.sentiment.polarity

testdata = ["I think today will be a great day","I do not think this will turn out well"]

#list of examples
@pytest.mark.parametrize('sample', testdata) 
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0
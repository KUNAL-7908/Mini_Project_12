# mini project 12
# Install the following before proceeding to the code:
# !pip install tweepy

import os
from cv2 import displayOverlay
import tweepy as tw
import pandas as pd

access_token = "501682241-ZG1DshytyxUIUY8FXPoH2AXaDG9d5DQlORemfAzU"
access_token_secret = "mxwCYkDjgWG5qWy8ONtVs3j2lxiYSxyberVVa92jmd27z"
consumer_key = "we0Drpnvc1FZNazKkiKoFWlGf"
consumer_secret = "OXRvmJwM6ca9k90XMIMoktSCa5XvjNieqJivcfjbOAlmpO6RhH"
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Collecting tweets
results = api.search(q='IPL', count=100)

# Creting a dataframe using pandas
data = pd.DataFrame(data=[tweet.text for tweet in results], columns=['Tweets'])

# Displaying first 10 elements of the dataframe
displayOverlay(data.head(10))

df=pd.read_csv('D:\Coding\Python programmming\summer_school\ipl.csv.png')
df

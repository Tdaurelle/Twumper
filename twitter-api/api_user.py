# api_user.py
# Mathew Titus, March 6, 2020
#
# Get latest tweets for a specific user
#
#
# #############################

# exec(open('./twitter-api/api_user.py').read())
from twython import Twython
import json
import pandas as pd

# load credentials
with open("./twitter-api/twitter_credentials.json", "r") as file:
    creds = json.load(file)

# instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# create query
query = {'q': 'italian',
         'result_type': 'recent',
         'count': 20,
         'lang': 'en'
         }

# search
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': [], 'id': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])
    dict_['id'].append(status['id'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
# df.sort_values(by='favorite_count', inplace=True, ascending=False)
print(df.head(5))

latest = dict_['id'][-1]

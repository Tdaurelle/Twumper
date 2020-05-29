# api_call.py
# Mathew Titus, March 6, 2020
#
# API is rate-limited to 450 responses / 15 minutes
# Sourced from https://stackabuse.com/accessing-the-twitter-api-with-python/
#
# #############################

# exec(open('./twitter-api/api_call.py').read())
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


# create query
query2 = {'q': 'italian',
         'result_type': 'recent',
         'count': 100,
         'lang': 'en',
          'since_id': latest
         }

# search
dict2_ = {'user': [], 'date': [], 'text': [], 'favorite_count': [], 'id': []}
for status in python_tweets.search(**query)['statuses']:
    dict2_['user'].append(status['user']['screen_name'])
    dict2_['date'].append(status['created_at'])
    dict2_['text'].append(status['text'])
    dict2_['favorite_count'].append(status['favorite_count'])
    dict2_['id'].append(status['id'])

# Structure data in a pandas DataFrame for easier manipulation
df2 = pd.DataFrame(dict2_)
# df2.sort_values(by='favorite_count', inplace=True, ascending=False)
print(df2.head(50))

print(len(dict2_['id']))
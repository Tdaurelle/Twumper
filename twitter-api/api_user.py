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
# ACCESS_TOKEN = python_tweets.obtain_access_token()

# create query
num_per_query = 100
query = {'q': 'italian',
         'result_type': 'recent',
         'count': num_per_query,
         'lang': 'en'
         }

# search
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': [], 'id': []}

response = python_tweets.search(**query)
for status in response['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])
    dict_['id'].append(status['id'])

query_count = 1

while (len(response) > 0) & (query_count < 4): #00):
    latest = dict_['id'][-1]
    query['max_id'] = latest
    for status in python_tweets.search(**query)['statuses']:
        dict_['user'].append(status['user']['screen_name'])
        dict_['date'].append(status['created_at'])
        dict_['text'].append(status['text'])
        dict_['favorite_count'].append(status['favorite_count'])
        dict_['id'].append(status['id'])
    print("dict_ now of length {}".format(len(dict_['id'])))
    query_count += 1

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
# df.sort_values(by='favorite_count', inplace=True, ascending=False)
print(df.head(5))


query = {'q': "New Yorkers may begin to see",
         'screen_name': 'MarioFloris4',
         'result_type': 'recent',
         'count': num_per_query,
         'lang': 'en'
         }


response = python_tweets.search(**query)
for status in response['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])
    dict_['id'].append(status['id'])


#######################################################
#######################################################

# instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'], oauth_version=2)
ACCESS_TOKEN = python_tweets.obtain_access_token()
client_args = {
    'headers': {
        'Authorization': 'Bearer ' + ACCESS_TOKEN
    }
}

twitter = Twython(creds['CONSUMER_KEY'],access_token=ACCESS_TOKEN,client_args=client_args)
params = {
    'screen_name': 'realDonaldTrump',
    'count': "10"
}
twitter.get_followers_list(**params)


params = {
    'screen_name': 'realDonaldTrump'
}

prof = twitter.lookup_user(**params)

for profile in prof:
    if profile['screen_name'] == 'realDonaldTrump':
        twump_id = profile['id']



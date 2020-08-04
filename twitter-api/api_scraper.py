# api_call.py
# Mathew Titus, June 11, 2020
#
# API is rate-limited to 450 responses / 15 minutes
#
# #####################################################

from twython import Twython
import json
import pandas as pd
import numpy as np
import datetime as dt


# load credentials
with open("./twitter-api/twitter_credentials.json", "r") as file:
    creds = json.load(file)

# instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
# ACCESS_TOKEN = python_tweets.obtain_access_token()

# create dictionary of activity to track response count by timestamp
num_responses = {}
print("{} responses so far.".format(np.sum([num_responses[k] for k in num_responses.keys()])))


def response_count():
    now_ = dt.datetime.now()
    start_ = dt.timedelta(seconds=-15*60) + now_
    now_ts = now_.timestamp()
    start_ts = start_.timestamp()
    query_times = np.where( (np.array(list(num_responses)) < now_ts) & (np.array(list(num_responses)) >= start_ts) )[0]
    return len(query_times)


def tweet_scrape(query_text: str='italian', num_per_query: int=10)
    # define arguments
    query_text = 'italian'
    num_per_query = 10

    # create query
    query = {'q': query_text,
             'result_type': 'recent',
             'count': num_per_query,
             'lang': 'en'
             }

    # search
    dict_ = {'user': [], 'user_id': [], 'date': [], 'text': [], 'favorite_count': [], 'id': []}
    for status in python_tweets.search(**query)['statuses']:
        dict_['user'].append(status['user']['screen_name'])
        dict_['user_id'].append(status['user']['id'])
        dict_['date'].append(status['created_at'])
        dict_['text'].append(status['text'])
        dict_['favorite_count'].append(status['favorite_count'])
        dict_['id'].append(status['id'])

    # print("dict_ now of length {}".format(len(dict_['id'])))
    query_count = 1
    ### TODO: Incorporate response_count() function into stopping calls
    while (len(response) > 0) & (query_count < 10):
        latest = dict_['id'][-1]
        query['max_id'] = latest
        for status in python_tweets.search(**query)['statuses']:
            dict_['user'].append(status['user']['screen_name'])
            dict_['user_id'].append(status['user']['id'])
            dict_['date'].append(status['created_at'])
            dict_['text'].append(status['text'])
            dict_['favorite_count'].append(status['favorite_count'])
            dict_['id'].append(status['id'])
        print("dict_ now of length {}".format(len(dict_['id'])))
        query_count += 1
    return dict_

def user_scrape(user_list):

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
# df.sort_values(by='favorite_count', inplace=True, ascending=False)
print(df.head(5))

#######################################################
#######################################################

# instantiate an OAuth2 object
twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'], oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
client_args = {
    'headers': {
        'Authorization': 'Bearer ' + ACCESS_TOKEN
    }
}

twitter = Twython(creds['CONSUMER_KEY'], access_token=ACCESS_TOKEN, client_args=client_args)

# search through tweet stash and collect users + followers + friends
##
user_set = set(dict_['user'])
usr = {}
fol = {}
fri = {}
for user in user_set:
    params = {
        'screen_name': user
    }
    usr[user] = user
    fol[user] = twitter.get_followers_list(**params)
    fri[user] = twitter.get_friends_list(**params)

# second degree
followers = []; [followers.extend(fol[f]) for f in fol]; followers = set(followers);
user_set2 = followers.copy()
friends = []; [friends.extend(fri[f]) for f in fri]; friends = set(friends);
user_set2.union(friends)
user_set2 = user_set2.difference(user_set)
for user in user_set2:
    params = {
        'screen_name': user
    }
    usr[user] = user
    fol[user] = twitter.get_followers_list(**params)
    fri[user] = twitter.get_friends_list(**params)

# prof = twitter.lookup_user(**params)
#
# for profile in prof:
#     if profile['screen_name'] == 'realDonaldTrump':
#         twump_id = profile['id']
#

hashtag = "DontOnABC"
user = "Dont_ABC"
params = {
        'screen_name': 'schnap'
}
prof = twitter.lookup_user(**params)

query = {
    'q':"#lotrlcg"
}

dict_ = {'user': [], 'user_id': [], 'date': [], 'text': [], 'favorite_count': [], 'id': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['user_id'].append(status['user']['id'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])
    dict_['id'].append(status['id'])




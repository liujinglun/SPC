# -*- coding: utf-8 -*-
from twitter import *
import unicodedata
twitter = Twitter(auth=OAuth("776468987907547136-3JlUa5JhVmMqEjAtWbZeKAirYDM1P5R",
                             "XKl172qKv5x4cJNGvHu1bisGTBpimFXi0zhuA9XLiyaym",
                             "7GMyjy5A20WyhVw7KM4yTZQw2",
                             "gToDHMwoJaiaXUkRE7eth7uWvcjpjBvGxjxTWkJARJsdTRYqcy"))

query = twitter.search.tweets(q='i need some good friends', count = "100")
print 'search finish'
# print query
# print 'length:', len(query['statuses'])

#use tweet_query to store query from twitter
tweet_query = []
tweet_query[:] = query['statuses'][:]
#print tweet_query

#use tweet_info to store useful info in query
tweet_info = []
tweet = []
#print tweet_query

#print query['statuses'][0]
zombie_flag = 0
for result in tweet_query:
    #print result
    #print 'content:', result['text']
    result['text'] = unicodedata.normalize('NFKD', result['text']).encode('ascii','ignore')
    tweet_info.append(result['text'])
    #print 'create_time:', result["created_at"]
    #print 'tweet number:', result['statuses_count']
    #print 'eneity length', len(result['entities'])
    #print 'screen name', result['user']['screen_name']
    result['user']['screen_name'] = unicodedata.normalize('NFKD', result['user']['screen_name']).encode('ascii','ignore')
    tweet_info.append(result['user']['screen_name'])
    #print 'follower:', result['user']['followers_count']
    tweet_info.append(result['user']['followers_count'])
    #print 'following:', result['user']['friends_count']
    tweet_info.append(result['user']['friends_count'])
    #print 'statuses_count', result['user']['statuses_count']
    tweet_info.append(result['user']['statuses_count'])
    #print len(tweet_info)
    tweet.append(tweet_info)
    tweet_info = []
print 'data load finish'
for i in range(len(tweet)):
    #print i, tweet[i]
    #print i, 'tweet:', tweet[i][0], 'user:', tweet[i][1], 'follower:',tweet[i][2], 'following:',tweet[i][3], 'number of post:', tweet[i][4]
    if (tweet[i][2] == 0 and tweet[i][4] < 20) or (tweet[i][2] * 6 < tweet[i][3] and tweet[i][4] < 20) or (tweet[i][2] * 6 < tweet[i][3] and tweet[i][4] > 200):
        print i, 'Alert, user', tweet[i][1], 'is likely to be a zombie fan.'
        print 'Information of User', tweet[i][1], ':'
        print 'tweet number:', tweet[i][4]
        print 'follower number:', tweet[i][2] 
        print 'following number:', tweet[i][3]
        zombie_flag = 1
if zombie_flag == 0:
    print 'No Alert'

print 'alert finish'

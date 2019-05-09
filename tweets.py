from TwitterSearch import *

try:
    tweets = TwitterSearch(
        consumer_key = 'XXXXXXXXX',
        consumer_secret = 'XXXXX',
        access_token = 'XXXXXXX',
        access_token_secret = 'XXXXXXX'
    )
    pesquisa = TwitterSearchOrder()
    pesquisa.set_keywords(['chatbot'])
    pesquisa.set_language('pt')

    for tweet in tweets.search_tweets_iterable(pesquisa):
        print('@{0} tweeted: {1}'.format(tweet['user']['screen_name'], tweet['text']))

except TwitterSearchException as e:
    print(e)

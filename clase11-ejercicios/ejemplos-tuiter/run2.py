from credenciales import *
import tweepy
import codecs
# https://tweepy.readthedocs.io/en/v3.5.0/

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser(), wait_on_rate_limit=True)

# For loop to iterate over tweets with #ocean, limit to 10
lista = ["djosuejj","pedrojsalinas","fernandogdo1"]
data = {
'screen_name': 'sadasda',
'followers_count': 23432,
'listed_count': 245,
'friends_count': 324,
'favourites_count': 234,
'name': 'sadasda',
'created_at': 'sadasda'
}
for l in lista:
    archivo =codecs.open("%s.csv" % l, "w",encoding="utf-8")
    user_data = api.followers(l)
    for i in user_data['users']:
        archivo.write(u"{}|{}|{}|{}|{}|{}|{} \n".format(i['screen_name'],i['followers_count'],i['listed_count'],i['friends_count'],i['favourites_count'],i['name'],i['created_at']))
    archivo.close()
    # print "%s - %s" % (l, user_data['created_at'])

from credenciales import *
import tweepy
import codecs

#Credenciales
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser(), wait_on_rate_limit=True)

periodicos = ["lahoraecuador","elcomerciocom","Expresoec","el_telegrafo"]

for periodico in periodicos:
    archivo =codecs.open("periodicos/%s.csv" % periodico, "w",encoding="utf-8")
    user_data = api.followers(periodico)
    archivo.write(u"screen_name|followers_count|listed_count|friends_count|favourites_count|name|created_at \n")
    for i in user_data['users']:
        archivo.write(u"{}|{}|{}|{}|{}|{}|{} \n".format(i['screen_name'],i['followers_count'],i['listed_count'],i['friends_count'],i['favourites_count'],i['name'],i['created_at']))
    archivo.close()

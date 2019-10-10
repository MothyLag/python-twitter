import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os 
import unicodedata
os.system("cls")

ckey = "UQQYVWck9gAp0AAGpy7gjHukm"
csecret = "BppYNluotrzIvfcxuVWOgsvXvGL2Gc1KIDdaZcjmARkiP925d8"
atoken = "245975745-zL9VRzcT46iRZVCOVuooJg0sWSf8MmxU3akA6tcR"
asecret = "Ut7LLhz0tC4Jz4e316z7Fq96d4z5RuoXLLLDbXH0Buxe6"


file =  open('tweetsNombreTextoCompleto.txt', 'a',encoding="utf-8")

class listener(StreamListener):

    def on_data(self, data):
 
        try:
            decoded = json.loads(data)
            #print(decoded)
        except Exception as e:
            print (e) #we don't want the listener to stop
            return True
        if decoded.get("retweeted_status") is not None:
            print("retweet descartado")
            return True
        if decoded.get('place') is not None:
            location = decoded.get('place').get('full_name')
        else:
            location = 'NA'
        retweet = decoded
        longtext = decoded.get('extended_tweet')
        #print(longtext)
        if longtext is None:
            print('Entro 2')
            text = decoded['text'].replace('\n',' ')
        else:
            print('Entro 1')
            text = decoded.get('extended_tweet').get('full_text').replace('\n',' ')
        print(text)
        print(len(text))
        user = '@' + decoded.get('user').get('screen_name')
        created = decoded.get('created_at')
        tweet = '%s;%s;%s\n' % (user,location,text)
        tweet = '%s|%s|%s|%s\n' % (user,location,created,text)
        #tweet1 = str(tweet.encode('unicode_escape'))
        print ("Tweet:",tweet)
       # file.write(tweet)
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':
    print ("Iniciando....")
    
    auth =OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener(),tweet_mode='extended')
    twitterStream.filter(track=['Zacatecas','#zacatecas','zacatecas','#Zac'])
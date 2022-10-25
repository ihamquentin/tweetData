from textblob import TextBlob
import tweepy 
import csv 
#import nltk



class twitterData():
    def __init__(self, cKey, cSecret, accessToken, accessTokenSecret) -> None:
        self.ckey = cKey
        self.csecret = cSecret
        self.accessToken = accessToken
        self.accessTokenSecret = accessTokenSecret
        #pass
    
    def auth(self, searchterm, limit):
        #searchTerm = input('enter keyword to stream through :' )
        #noOfSearchTerms = int(input('Enter how many tweets to search: '))
        auth = tweepy.OAuthHandler(self.ckey, self.csecret)
        auth.set_access_token(self.accessToken, self.accessTokenSecret)
        api = tweepy.API(auth)
        mysearch = tweepy.Cursor(api.search_tweets, q=searchterm, lang = "en").items(limit)

        filename = f'{searchterm}.csv'
        f = open(filename, "w+", encoding='utf-8')
        headers = "texts, polarity, subjectivity\n"
        f.write(headers)

        for tweet in mysearch:
            c = tweet.text
            texts = ' '.join(word for word in c.split() if word[0]!='#' and word[0]!='@' and word[0:5]!='https' and word[0:2]!='RT')
            #texts = nltk.word_tokenize(str(untokenized))
            analysis = TextBlob(tweet.text)
            polar = analysis.sentiment.polarity
            subje = analysis.sentiment.subjectivity
            f.write(texts.replace(',', '^') + ',' + str(polar) + ',' + str(subje) + '\n')
    
            #print('texts: ' + str(texts))
            #print('polarity: ' + str(polar))
            #print('subjectivity: ' + str(subje))
        f.close()
        return 'Done'
    
    def percentage(self, part,whole):
        return 100 *float(part)/float(whole)


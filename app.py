from tweeterData import twitterData


cKey =""
cSecret = ""
accessToken =""
accessTokenSecret =""


searches = ['japa', 'japa wave']

call = twitterData(cKey, cSecret, accessToken, accessTokenSecret)

for i in searches:
    call.auth(i, 500)
    print(f'searches on {i} Done!')

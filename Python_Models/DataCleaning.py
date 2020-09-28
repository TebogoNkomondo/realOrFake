import keras.preprocessing.text as kpt
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
import re
import string

nltk.download('stopwords')
nltk.download('punkt')
stopword = nltk.corpus.stopwords.words('english')

porter =  PorterStemmer()

#punctutation removal
def clean_text(text):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text
#end clean_text

# Tockenization
def tokenization(text):
    text = re.split('\W+', text)
    return text
#end tokenization

# stopword removal
def remove_stopwords(text):
    text = [word for word in text if word not in stopword]
    return text

# return to string
def listToString(s):     
    # initialize an empty string 
    str1 = " " 
    # return string   
    return (str1.join(s))
#end listToString

def sentenceStemmer(text):
    words = word_tokenize(text)
    corpus = []
    for word in words:
        corpus.append(porter.stem(word))
        corpus.append(" ")
    #end for
    return "".join(corpus)
#end sentenceStemmer

#remove emojis from text
def remove_emoji(text):
    tweet = re.compile("["
                           u"\U0001F600-\U0001F64F"
                           u"\U0001F300-\U0001F5FF"
                           u"\U0001F680-\U0001F6FF"
                           u"\U0001F1E0-\U0001F1FF"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return tweet.sub(r'', text)
#end remove_emoji

def rename(tweet):

    #correct some acronyms while we are at it
    tweet = re.sub("tnwx", "tennessee weather", tweet)
    tweet = re.sub(r"azwx", "arizona weather", tweet)  
    tweet = re.sub(r"alwx", "alabama weather", tweet)
    tweet = re.sub(r"wordpressdotcom", "wordpress", tweet)      
    tweet = re.sub(r"gawx", "georgia weather", tweet)  
    tweet = re.sub(r"scwx", "south carolina weather", tweet)  
    tweet = re.sub(r"cawx", "california weather", tweet)
    tweet = re.sub(r"usnwsgov", "united states national weather service", tweet) 
    tweet = re.sub(r"MH370", "malaysia airlines flight 370", tweet)
    tweet = re.sub(r"okwx", "oklahoma city weather", tweet)
    tweet = re.sub(r"arwx", "arkansas weather", tweet)  
    tweet = re.sub(r"lmao", "laughing my ass off", tweet)  
    tweet = re.sub(r"amirite", "am i right", tweet)
    
    #and some typos/abbreviations
    tweet = re.sub(r"w/e", "whatever", tweet)
    tweet = re.sub(r"w/", "with", tweet)
    tweet = re.sub(r"usagov", "usa government", tweet)
    tweet = re.sub(r"recentlu", "recently", tweet)
    tweet = re.sub(r"ph0tos", "photos", tweet)
    tweet = re.sub(r"exp0sed", "exposed", tweet)
    tweet = re.sub(r"<3", "love", tweet)
    tweet = re.sub(r"amageddon", "armageddon", tweet)
    tweet = re.sub(r"trfc", "traffic", tweet)
    tweet = re.sub(r"windStorm", "wind storm", tweet)
    tweet = re.sub(r"16yr", "16 year", tweet)
    tweet = re.sub(r"traumatised", "traumatized", tweet)
    
    #hashtags and usernames
    tweet = re.sub(r"irandeal", "iran deal", tweet)
    tweet = re.sub(r"arianagrande", "ariana grande", tweet)
    tweet = re.sub(r"camilacabello97", "camila cabello", tweet) 
    tweet = re.sub(r"rondarousey", "ronda rousey", tweet)     
    tweet = re.sub(r"mtvhottest", "mtv hottest", tweet)
    tweet = re.sub(r"trapmusic", "trap music", tweet)
    tweet = re.sub(r"prophetmuhammad", "prophet Mmuhammad", tweet)
    tweet = re.sub(r"PantherAttack", "panther attack", tweet)
    tweet = re.sub(r"strategicpatience", "strategic patience", tweet)
    tweet = re.sub(r"socialnews", "social news", tweet)
    tweet = re.sub(r"idps:", "internally displaced people :", tweet)
    tweet = re.sub(r"artistsUnited", "artists united", tweet)
    tweet = re.sub(r"claytonBryant", "clayton bryant", tweet)
    tweet = re.sub(r"uk", "united kingdom", tweet)
    tweet = re.sub(r"usa", "united states of america", tweet)
    tweet = re.sub(r"ny", "new york", tweet)
    tweet = re.sub(r"newcastleupontyne", "newcastle upon tyne", tweet)
    tweet = re.sub(r"jimmyfallon", "jimmy fallon", tweet)
    tweet = re.sub(r"justinbieber", "justin bieber", tweet)
    tweet = re.sub(r"time2015", "time 2015", tweet)
    tweet = re.sub(r"djicemoon", "dj icemoon", tweet)
    tweet = re.sub(r"livingsafely", "living safely", tweet)
    tweet = re.sub(r"fifa16", "fifa 2016", tweet)
    tweet = re.sub(r"thisiswhywecanthavenicethings", "this is why we cannot have nice things", tweet)
    tweet = re.sub(r"bbcnews", "bbc news", tweet)
    tweet = re.sub(r"undergroundrailraod", "underground railraod", tweet)
    tweet = re.sub(r"c4news", "c4 news", tweet)
    tweet = re.sub(r"mudslide", "mud slide", tweet)
    tweet = re.sub(r"nosurrender", "no surrender", tweet)
    tweet = re.sub(r"notexplained", "not explained", tweet)
    tweet = re.sub(r"greatbritishbakeoff", "great british bake off", tweet)
    tweet = re.sub(r"londonfire", "london fire", tweet)
    tweet = re.sub(r"kotaweather", "kota weather", tweet)
    tweet = re.sub(r"luchaunderground", "lucha underground", tweet)
    tweet = re.sub(r"koin6news", "koin 6 news", tweet)
    tweet = re.sub(r"liveOnK2", "live on K2", tweet)
    tweet = re.sub(r"9newsgoldcoast", "9 news gold coast", tweet)
    tweet = re.sub(r"nikeplus", "nike plus", tweet)
    tweet = re.sub(r"david_cameron", "david cameron", tweet)
    tweet = re.sub(r"peterjukes", "peter jukes", tweet)
    tweet = re.sub(r"mikeparractor", "michael parr", tweet)
    tweet = re.sub(r"4playthursdays", "foreplay thursdays", tweet)
    tweet = re.sub(r"tgf2015", "tonti town grape festival", tweet)
    tweet = re.sub(r"realmandyrain", "mandy rain", tweet)
    tweet = re.sub(r"graysondolan", "grayson dolan", tweet)
    tweet = re.sub(r"apollobrown", "apollo brown", tweet)
    tweet = re.sub(r"saddlebrooke", "saddle brooke", tweet)
    tweet = re.sub(r"tontitowngrape", "tonti town grape", tweet)
    tweet = re.sub(r"abbswinston", "abbs winston", tweet)
    tweet = re.sub(r"shaunKing", "sshaun king", tweet)
    tweet = re.sub(r"meekmill", "meek mill", tweet)
    tweet = re.sub(r"tornadogiveaway", "tornado giveaway", tweet)
    tweet = re.sub(r"grupdates", "gr updates", tweet)
    tweet = re.sub(r"southdowns", "south downs", tweet)
    tweet = re.sub(r"braininjury", "brain injury", tweet)
    tweet = re.sub(r"auspol", "australian politics", tweet)
    tweet = re.sub(r"PlannedParenthood", "Planned Parenthood", tweet)
    tweet = re.sub(r"calgaryweather", "calgary weather", tweet)
    tweet = re.sub(r"weallheartonedirection", "we all heart one direction", tweet)
    tweet = re.sub(r"edsheeran", "ed sheeran", tweet)
    tweet = re.sub(r"trueHeroes", "true heroes", tweet)
    tweet = re.sub(r"complexmag", "complex magazine", tweet)
    tweet = re.sub(r"theadvocatemag", "the advocate magazine", tweet)
    tweet = re.sub(r"cityofcalgary", "city of calgary", tweet)
    tweet = re.sub(r"ebolaoutbreak", "ebola outbreak", tweet)
    tweet = re.sub(r"summerfate", "summer fate", tweet)
    tweet = re.sub(r"ramag", "royal academy magazine", tweet)
    tweet = re.sub(r"offers2go", "offers to go", tweet)
    tweet = re.sub(r"modiministry", "modi ministry", tweet)
    tweet = re.sub(r"taxiways", "taxi ways", tweet)
    tweet = re.sub(r"calum5sos", "calum hood", tweet)
    tweet = re.sub(r"jamesmelville", "james melville", tweet)
    tweet = re.sub(r"jamaicaobserver", "jamaica observer", tweet)
    tweet = re.sub(r"tweetlikeitsseptember11th2001", "tweet like it is september 11th 2001", tweet)
    tweet = re.sub(r"cbplawyers", "cbp lawyers", tweet)
    tweet = re.sub(r"fewmoretweets", "few more tweets", tweet)
    tweet = re.sub(r"blacklivesmatter", "black lives matter", tweet)
    tweet = re.sub(r"nasahurricane", "nasa hurricane", tweet)
    tweet = re.sub(r"onlinecommunities", "online communities", tweet)
    tweet = re.sub(r"humanconsumption", "human consumption", tweet)
    tweet = re.sub(r"typhoon-devastated", "typhoon devastated", tweet)
    tweet = re.sub(r"meat-loving", "meat loving", tweet)
    tweet = re.sub(r"facialabuse", "facial abuse", tweet)
    tweet = re.sub(r"lakecounty", "lake county", tweet)
    tweet = re.sub(r"beingauthor", "being author", tweet)
    tweet = re.sub(r"withheavenly", "with heavenly", tweet)
    tweet = re.sub(r"thanku", "thank you", tweet)
    tweet = re.sub(r"itunesmusic", "itunes music", tweet)
    tweet = re.sub(r"offensivecontent", "offensive content", tweet)
    tweet = re.sub(r"worstsummerjob", "worst summer job", tweet)
    tweet = re.sub(r"harrybecareful", "harry be careful", tweet)
    tweet = re.sub(r"nasasolarsystem", "nasa solar system", tweet)
    tweet = re.sub(r"animalrescue", "animal rescue", tweet)
    tweet = re.sub(r"kurtschlichter", "kurt schlichter", tweet)
    tweet = re.sub(r"throwingknifes", "throwing knives", tweet)
    tweet = re.sub(r"godsLove", "god's love", tweet)
    tweet = re.sub(r"bookboost", "book boost", tweet)
    tweet = re.sub(r"ibooklove", "I book love", tweet)
    tweet = re.sub(r"nestleindia", "nestle india", tweet)
    tweet = re.sub(r"realdonaldtrump", "donald trump", tweet)
    tweet = re.sub(r"davidvonderhaar", "david vonderhaar", tweet)
    tweet = re.sub(r"ceciltheLion", "cecil the lion", tweet)
    tweet = re.sub(r"weathernetwork", "weather network", tweet)
    tweet = re.sub(r"gopdebate", "gop debate", tweet)
    tweet = re.sub(r"rickperry", "rick perry", tweet)
    tweet = re.sub(r"frontpage", "front page", tweet)
    tweet = re.sub(r"newsintweets", "news in tweets", tweet)
    tweet = re.sub(r"viralspell", "viral spell", tweet)
    tweet = re.sub(r"til_now", "until now", tweet)
    tweet = re.sub(r"volcanoinrussia", "volcano in russia", tweet)
    tweet = re.sub(r"zippednews", "Zipped news", tweet)
    tweet = re.sub(r"michelebachman", "michele bachman", tweet)
    tweet = re.sub(r"53inch", "53 inch", tweet)
    tweet = re.sub(r"kerricktrial", "kerrick trial", tweet)
    tweet = re.sub(r"abstorm", "alberta storm", tweet)
    tweet = re.sub(r"beyhive", "beyonce hive", tweet)
    tweet = re.sub(r"rockyfire", "rocky fire", tweet)
    tweet = re.sub(r"listen/buy", "listen or buy", tweet)
    tweet = re.sub(r"artistsunited", "artists united", tweet)
    tweet = re.sub(r"engvsaus", "england vs australia", tweet)
    tweet = re.sub(r"scottwalker", "scott walker", tweet)
    tweet = re.sub(r"africanbaze", "african baze", tweet)
    tweet = re.sub(r"engineshed", "engine shed", tweet)
    tweet = re.sub(r"newsnigeria", "nigeria news", tweet)
    return tweet
#end rename

from random import randint as rand
import requests

newsSite = ["New Yorker", "Slate", "Daily Show", "The Guardian", "Al Jazeera America", "NPR", "Colbert Report", "New York Times", "BuzzFeed", "PBS", "BBC", "Huffington Post" , "Washington Post", "The Economist", "Politico", "MSNBC", "CNN", "NBC News", "CBS News", "Google News", "Bloomberg", "ABC News", "USA TODAY", "Yahoo News", "Wall Street Journal", "Fox News", "Drudge Report", "Breitbart", "Ruch Limbaugh Show", "The Blaze", "Sean Hannity Show", "Glenn Beck Program"]
#Assigns Liberal-Conservative Index based on Washington Post Article found here: 
#https://www.washingtonpost.com/news/the-fix/wp/2014/10/21/lets-rank-the-media-from-liberal-to-conservative-based-on-their-audiences/?noredirect=on&utm_term=.273b3ed0bdb5
politicalIndex = {"New Yorker" : -5.9, "Slate" : -5.9, "Daily Show": -5, "The Guardian": -5.4, "Al Jazeera America" : -5.2, "NPR": -5, "Colbert Report" : -4.8, "New York Times": -4.6, "BuzzFeed" : -4, "PBS" : -3.9, "BBC":-3.8, "Huffington Post":-3.7 , "Washington Post": -3.6, "The Economist" :-3.5, "Politico": -3.4, "MSNBC": -2.4, "CNN": -2.2, "NBC News": -2, "CBS News": -1.9, "Google News": -1.8, "Bloomberg": -1.7, "ABC News" :-1.6, "USA TODAY": -1.7,"Yahoo News" : -0.8, "Wall Street Journal" : -0.6, "Fox News": 2, "Drudge Report": 4.6, "Breitbart": 5.6 , "Ruch Limbaugh Show": 5.7, "The Blaze": 5.8, "Sean Hannity Show": 5.9, "Glenn Beck Program" : 6
}
#A value of "" means key not found in API 
idDict = {
    "New Yorker" : "", "Slate" : "", "Daily Show" : "", "The Guardian": "", "Al Jazeera America": "al-jazeera-english", "NPR" : "", "Colbert Report" : "", "New York Times" : "the-new-york-times", "BuzzFeed" : "buzzfeed", "PBS" : "", "BBC" : "bbc-news", "Huffington Post" : "the-huffington-post" , "Washington Post" : "the-washington-post", "The Economist": "the-economist", "Politico" : "politico", "MSNBC" : "msnbc", "CNN" : "cnn" , "NBC News": "nbc-news", "CBS News": "cbs-news", "Google News" : "google-news", "Bloomberg" : "bloomberg", "ABC News" :  "abc-news", "USA TODAY" : "usa-today", "Yahoo News": "", "Wall Street Journal" : "the-wall-street-journal", "Fox News" : "fox-news", "Drudge Report" : "", "Breitbart" : "breitbart-news", "Ruch Limbaugh Show" : "", "The Blaze" : "", "Sean Hannity Show" : "", "Glenn Beck Program" : ""
}

tempNews = [{
    "title": "",
    "author": "",
    "url": "",
    "urlToImage": None,
} for i in range(0,9)]

#Returns single pseudo-random site
def getRandomSite():
    x = rand(0, len(newsSite)-1)
    site = newsSite[x]
    while(idDict[site]==""):
        x = rand(0, len(newsSite)-1)
        site = newsSite[x]
    return site
    
#Returns pseudo-random site with Liberal-Conservative Index greater than zero(Conservative)
def getConservativeSite():
    site = getRandomSite()
    while(politicalIndex[site] < 0):
        site = getRandomSite()
    return site
    
#Returns pseudo-random site with Liberal-Conservative Index less than zero(Liberal)
def getLiberalSite():
    site = getRandomSite()
    while(politicalIndex[site] > 0):
        site = getRandomSite()
    return site
    
#Returns list of sites for articles to be displayed
def getSiteList(maxArticles):
    aggregateIndex = 0
    siteList = []
    while(len(siteList) < maxArticles):
        #If sum of indicies of sites in sites to be displayed is liberal(<0), adds conservative site
        if aggregateIndex <0:
            site = getConservativeSite()
            siteList.append(site)
            aggregateIndex+= politicalIndex[site]
        #If sum of indicies of sites in sites to be displayed is conservative(>0), adds liberal site
        elif aggregateIndex >0:
            site = getLiberalSite()
            siteList.append(site)
            aggregateIndex+= politicalIndex[site]
        #If sum of indicies of sites in sites to be displayed is neutral, adds random site
        else: 
            site = getRandomSite()
            siteList.append(site)
            aggregateIndex+= politicalIndex[site]
    return siteList
    
def get_json_response(url, apiKey, params):
    compiled = url +"?"
    for key in params:
        compiled += key + "=" + params[key] + "&"
    compiled+= "apiKey=" + apiKey
    response = requests.get(compiled).json()
    return response
    
#  sources, q, language, country, category
def getTopResponse(siteId):
    #print("\n SITE ID: " + siteId + " \n")
    data = get_json_response(
        "https://newsapi.org/v2/top-headlines", 
        '12126d1b282e4c94a45c9a108b94f246',
        #"be18c103021f45059454abfe91436f61",
        {
            "sources" : siteId,
            "language": "en"
        },
    )
    #print(data)
    if data["totalResults"] > 0:
        randNum = rand(0,len(data["articles"]) - 1)
        data["articles"][randNum]["content"] = None
        return data["articles"][randNum]
    else:
        return False
 
def getArticlesByQuery(query):
    data = get_json_response(
        "https://newsapi.org/v2/everything", 
        '12126d1b282e4c94a45c9a108b94f246',
        #"be18c103021f45059454abfe91436f61",
        {
            "q": query,
            "language": "en"
        },
    )
    return data["articles"]

def getTopHeadlines():
    data = get_json_response(
        "https://newsapi.org/v2/top-headlines", 
        #'12126d1b282e4c94a45c9a108b94f246',
        "be18c103021f45059454abfe91436f61",
        {
            "language": "en"
        },
    )
    return data["articles"]
 
# https://www.allsides.com/media-bias/media-bias-ratings
# Media Bias Ratings are determined using multiple methods and represent 
# the average judgment of Americans. They are based on blind surveys of 
# people across the political spectrum, multi-partisan analysis, editorial 
# reviews, third party data, and tens of thousands of user feedback ratings.

left = [
    "the-huffington-post",
    "msnbc",
    "newsweek",
    "new-york-magazine",
    "vice-news",
    
    "abc-news",
    "al-jazeera-english",
    "buzzfeed",
    "cbs-news",
    "cnn",
    "nbc-news",
    "politico",
    "the-economist",
    "the-new-york-times",
    "the-verge",
    "the-washington-post",
    "time",
]
center = [
    "associated-press",
    "bbc-news",
    "bloomberg",
    "reuters",
    "the-hill",
    "the-wall-street-journal",
    "usa-today",
]
right = [
    "the-washington-times",
    "the-american-conservative",
    
    "fox-news",
    "national-review",
]

def getRandomArticle(siteIdList, titlesDict):
    article = False
    counter = 0
    while not article and counter < 5:
        siteId = siteIdList[rand(0, len(siteIdList)-1)]
        article = getTopResponse(siteId)
        if article:
            if article["title"] in titlesDict:
                article = False
            else:
                titlesDict[article["title"]] = True
        counter += 1
    return article

def cleanImg(articlesList):
    for element in articlesList:
        if(element['urlToImage'] == None):
            element['urlToImage'] = "../static/gavel.jpg"
    return articlesList
    
def getArticles(numArticles):
    articlesList = []
    titlesDict = {}
    for i in range(0, numArticles):
        article = getRandomArticle(left, titlesDict)        
        articlesList.append(article)
        article = getRandomArticle(center, titlesDict)        
        articlesList.append(article)
        article = getRandomArticle(right, titlesDict)        
        articlesList.append(article)
    articlesList = cleanImg(articlesList)
    return articlesList

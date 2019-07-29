from random import randint as rand
import apiUtils
newsSite = ["New Yorker", "Slate", "Daily Show", "The Guardian", "Al Jazeera America", "NPR", "Colbert Report", "New York Times", "BuzzFeed", "PBS", "BBC", "Huffington Post" , "Washington Post", "The Economist", "Politico", "MSNBC", "CNN", "NBC News", "CBS News", "Google News", "Bloomberg", "ABC News", "USA TODAY", "Yahoo News", "Wall Street Journal", "Fox News", "Drudge Report", "Breitbart", "Ruch Limbaugh Show", "The Blaze", "Sean Hannity Show", "Glenn Beck Program"]
#Assigns Liberal-Conservative Index based on Washington Post Article found here: 
#https://www.washingtonpost.com/news/the-fix/wp/2014/10/21/lets-rank-the-media-from-liberal-to-conservative-based-on-their-audiences/?noredirect=on&utm_term=.273b3ed0bdb5
politicalIndex = {"New Yorker" : -5.9, "Slate" : -5.9, "Daily Show": -5, "The Guardian": -5.4, "Al Jazeera America" : -5.2, "NPR": -5, "Colbert Report" : -4.8, "New York Times": -4.6, "BuzzFeed" : -4, "PBS" : -3.9, "BBC":-3.8, "Huffington Post":-3.7 , "Washington Post": -3.6, "The Economist" :-3.5, "Politico": -3.4, "MSNBC": -2.4, "CNN": -2.2, "NBC News": -2, "CBS News": -1.9, "Google News": -1.8, "Bloomberg": -1.7, "ABC News" :-1.6, "USA TODAY": -1.7,"Yahoo News" : -0.8, "Wall Street Journal" : -0.6, "Fox News": 2, "Drudge Report": 4.6, "Breitbart": 5.6 , "Ruch Limbaugh Show": 5.7, "The Blaze": 5.8, "Sean Hannity Show": 5.9, "Glenn Beck Program" : 6
}

#Returns single pseudo-random site
def getRandomSite():
    x = rand(0, len(newsSite)-1)
    site = newsSite[x]
    while(apiUtils.idDict[site]==""):
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


if __name__ == "__main__":
    li = getSiteList(12)
    for site in li:
        siteId = apiUtils.idDict[site]
        tile = apiUtils.getTopResponse(siteId)
        print(tile)
    

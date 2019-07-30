import requests


#A value of "" means key not found in API 
idDict = {
    "New Yorker" : "", "Slate" : "", "Daily Show" : "", "The Guardian": "", "Al Jazeera America": "al-jazeera-english", "NPR" : "", "Colbert Report" : "", "New York Times" : "the-new-york-times", "BuzzFeed" : "buzzfeed", "PBS" : "", "BBC" : "bbc-news", "Huffington Post" : "the-huffington-post" , "Washington Post" : "the-washington-post", "The Economist": "the-economist", "Politico" : "politico", "MSNBC" : "msnbc", "CNN" : "cnn" , "NBC News": "nbc-news", "CBS News": "cbs-news", "Google News" : "google-news", "Bloomberg" : "bloomberg", "ABC News" :  "abc-news", "USA TODAY" : "usa-today", "Yahoo News": "", "Wall Street Journal" : "the-wall-street-journal", "Fox News" : "fox-news", "Drudge Report" : "", "Breitbart" : "breitbart-news", "Ruch Limbaugh Show" : "", "The Blaze" : "", "Sean Hannity Show" : "", "Glenn Beck Program" : ""
}

def test():
    print("test")

def get_json_response(url, apiKey, params):
    compiled = url +"?"
    for key in params:
        compiled += key + "=" + params[key] + "&"
    compiled+= "apiKey=" + apiKey
    response = requests.get(compiled).json()
    return response
    
#  sources, q, language, country, category
def getTopResponse(siteId):
    data = get_json_response(
        'https://newsapi.org/v2/everything', 
        '12126d1b282e4c94a45c9a108b94f246',
        {
            'sources' : siteId
        },
    )
    print(siteId)
    print(data["status"])
    print(data)
    return data["articles"][0]
'''
print(getTopResponse("new-yorker"))
idDict = {
    "New Yorker" : "", "Slate" : "", "Daily Show" : "", "The Guardian": "", "Al Jazeera America": "al-jeezera-english", "NPR" : "", "Colbert Report" : "", "New York Times" : "the-new-york-times", "BuzzFeed" : "buzzfeed", "PBS" : "", "BBC" : "bbc-news", "Huffington Post" : "the-huffington-post" , "Washington Post" : "the-washington-post", "The Economist": "the-economist", "Politico" : "politico", "MSNBC" : "msnbc", "CNN" : "cnn" , "NBC News": "nbc-news", "CBS News": "cbs-news", "Google News" : "google-news", "Bloomberg" : "bloomberg", "ABC News" :  "abc-news", "USA TODAY" : "usa-today", "Yahoo News": "", "Wall Street Journal" : "the-wall-street-journal", "Fox News" : "fox-news", "Drudge Report" : "", "Breitbart" : "breitbart-news", "Ruch Limbaugh Show" : "", "The Blaze" : "", "Sean Hannity Show" : "", "Glenn Beck Program" : ""
}
'''
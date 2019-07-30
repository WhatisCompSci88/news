import requests

def get_stock_articles(symbol, num_articles):
    base_url = "https://cloud.iexapis.com/stable/stock/"
    token = "?token=pk_245ac17ee4f34b488211e66a01a69e14"
    url = base_url + symbol + "/news/last/" + str(num_articles) + token
    response = requests.get(url).json()
    return response

# apple_articles = get_stock_articles("aapl", 10)
# for article in apple_articles:
#     for key in article:
#         print(key, ":", article[key])
#     print("\n")

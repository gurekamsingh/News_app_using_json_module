import requests
#
#
# url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-18&pageSize=8&sortBy=publishedAt&apiKey=d817aba6c2134b63b615c16e94cec9ad"
# url1 = "https://newsapi.org/v2/everything?q=sports&from=2023-06-18&pageSize=8&sortBy=publishedAt&apiKey=d817aba6c2134b63b615c16e94cec9ad"
# url2 = "https://newsapi.org/v2/everything?domains=wsj.com&pageSize=8&apiKey=d817aba6c2134b63b615c16e94cec9ad"
# url3 = "https://newsapi.org/v2/everything?q=technology&from=2023-06-18&pageSize=8&sortBy=publishedAt&apiKey=d817aba6c2134b63b615c16e94cec9ad"
#
# # d = int(input("What kind of news do you want? \nPress 1 for Sports \nPress 2 for Tesla \nPress 3 for Wallstreet Journal \nPress 4 for Tech news\n"))
# if (d:=int(input("What kind of news do you want? \nPress 1 for Sports \nPress 2 for Tesla \nPress 3 for Wallstreet Journal \nPress 4 for Tech news\n"))) < 5 :
#
#     if d == 1:
#         x = requests.get(url1)
#         print(x.text)
#
#     elif d == 2:
#         x = requests.get(url)
#         print(x.text)
#
#     elif d == 3:
#         x = requests.get(url2)
#         print(x.text)
#
#     elif d == 4:
#         x = requests.get(url3)
#         print(x.text)
#
# else:
#     print("Invalid input")

import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-01-28&sortBy=publishedAt&apiKey=dbe57b028aeb41e285a226a94865f7a7"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------------")

import requests

api_key = "418cfcb3b4314098a6358ce488664b2f"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-10-04&sortBy=publishedAt&apiKey=418cfcb3b4314098a6358ce488664b2f"

#Make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
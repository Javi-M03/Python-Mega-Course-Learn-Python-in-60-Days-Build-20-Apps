import requests
from send_email import send_email
import credentiales

url = "https://newsapi.org/v2/everything?"\
        "q=tesla&"\
        "from=2024-10-04&"\
        f"sortBy=publishedAt&apiKey={credentiales.apiKey}&"\
        "language=en"

#Make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

message = ""

#Access the article title and description
for article in content["articles"][:20]:
    if article["title"] is not None:
        message = "Subject: Today's News" \
        +"\n"+ message + article["title"] + "\n" \
        + article["description"] \
        + '\n' + article["url"] + 2*'\n'
        
message = message.encode("utf-8")
send_email(message)
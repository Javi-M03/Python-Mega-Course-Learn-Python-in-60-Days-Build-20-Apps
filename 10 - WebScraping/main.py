import requests, selectorlib,smtplib,ssl, credentiales, time


URL  = "https://programmer100.pythonanywhere.com/tours"

def scrape(url):
    response= requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def send_email(message):
        host = "smtp.gmail.com"
        port = 465

        password = credentiales.PASSWORD
        username = credentiales.SENDER 
        reciever = credentiales.SENDER 

        context = ssl.create_default_context()


        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username,password)
            server.sendmail(username,reciever, message)

def store(extracted):
    with open("data.txt","a") as file:
        file.write(extracted + '\n')

def read(extracted):
    with open("data.txt","r") as file:
         return file.read()

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted =  extract(scraped)
        print(extracted)
        content= read(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email("Hey, new event was found!") 
        time.sleep(3600)



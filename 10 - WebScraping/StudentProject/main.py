import requests, selectorlib,smtplib,ssl, time, streamlit as st,datetime




URL = "https://programmer100.pythonanywhere.com/"
now = str(datetime.datetime.now())

def scrape(url):
    response= requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    return value

def write_temp(extracted):
    with open("data.txt","a") as file:
        file.write(extracted + '\n')



if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    extracted = now + ", " + extracted  
    write_temp(extracted)
    print(extracted)
    

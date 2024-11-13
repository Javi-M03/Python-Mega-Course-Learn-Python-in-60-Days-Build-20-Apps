import requests, selectorlib,sqlite3
from datetime import datetime

connection = sqlite3.connect("data.db")

URL = "https://programmer100.pythonanywhere.com/"


def scrape(url):
    response= requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    return value

def write_temp(extracted):
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    print(extracted)
    print(now)
    cursor.execute("INSERT INTO temperatures VALUES(?,?)", (extracted,now))
    connection.commit()



if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    extracted = extracted  
    write_temp(extracted)
    print(extracted)
    

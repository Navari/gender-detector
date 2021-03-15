import requests
from detector import detect
from bs4 import BeautifulSoup 

# instagram URL
URL = "https://www.instagram.com/{}/"


# scrape function
def scrape_data(username): 
      
    # getting the request from url 
    r = requests.get(URL.format(username)) 
      
    # converting the text 
    s = BeautifulSoup(r.text, "html.parser") 
      
    # finding meta info 
    meta = s.find("meta", property ="og:image") 
      
    # calling parse method 
    return parse_data(meta.attrs['content']) 


def download_image(url):
    r = requests.get(url)
    file = open("static/sample.png", "wb")
    file.write(r.content)
    file.close()


def run(username):
    d = scrape_data(username)
    download_image(d)
    return detect.detect_face()

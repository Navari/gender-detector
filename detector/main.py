import requests
from detector import detect

# instagram URL
URL = "https://www.instagram.com/{}/?__a=1"

proxies = {
    'http': 'http://uwtpptej-dest:gzz8s03me3jp@45.15.223.0:9018',
    'https': 'https://uwtpptej-dest:gzz8s03me3jp@45.15.223.0:9018',
}
session = requests.Session()
session.proxies.update(proxies)


# scrape function
def scrape_data(username):
    # getting the request from url
    r = session.get(URL.format(username))
    print(r.status_code)
    if r.status_code != 200:
        print(r.content)
        return ''
    re = r.json()
    print(re)
    image_hd = re['graphql']['user']['profile_pic_url_hd']
    return image_hd


def download_image(url):
    r = session.get(url)
    file = open("static/sample.png", "wb")
    file.write(r.content)
    file.close()


def run(username):
    d = scrape_data(username)
    if d != '':
        download_image(d)
        return detect.detect_face()
    else:
        return []

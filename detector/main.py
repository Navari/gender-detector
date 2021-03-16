import requests
from detector import detect

def download_image(url):
    r = requests.get(url)
    file = open("static/sample.png", "wb")
    file.write(r.content)
    file.close()


def run(username):
    download_image(username)
    return detect.detect_face()

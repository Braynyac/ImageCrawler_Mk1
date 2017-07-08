import requests
from bs4 import BeautifulSoup
import urllib.request
import random
from sys import platform
from os import system


def image_crawler(phrase, max_pages):
    keywords = phrase.strip().replace(" ", "+")
    folder_name = create_folder(phrase)
    for page in range(max_pages):
        url = 'https://www.google.com/search?hl=en&authuser=0&site=imghp&tbm=isch&source=hp&biw=1855&bih=917&q='+keywords+'&oq=google+images&gs_l=img.3..0l10.2061.4248.0.4407.15.15.0.0.0.0.85.889.13.13.0....0...1.1.64.img..2.13.888.0..35i39k1.9LjMRpJcHXY'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")

        for img in soup.findAll('img'):
            src = str(img.get('src'))
            print(src)
            if 'http' in src:
                download_image(folder_name, src)


def download_image(folder_name, url):
    name = str(random.randrange(1, 100000000)) + '.jpg'
    urllib.request.urlretrieve(url, 'images/'+folder_name+'/'+name)
    print(name)


def create_folder(phrase):
    folder_name = phrase.strip().lower().replace(" ", "_")
    if platform == 'linux':
        system("mkdir images/" + folder_name + '/')
    else:
        system("mkdir images\\" + folder_name + '\\')
    return folder_name


def interface():
    phrase = input("Keywords: ")
    image_crawler(phrase, 1)

interface()

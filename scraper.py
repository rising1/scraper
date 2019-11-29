import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://uk.advfn.com/p.php?pid=message&msg=0'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

soup.findAll('a')
import urllib3
import requests
from bs4 import BeautifulSoup
#url="https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/"
url="https://stackoverflow.com/questions/36516183/what-should-i-use-to-open-a-url-instead-of-urlopen-in-urllib3"
response=requests.get(url)
#page=urllib3.urlopen(url)
x=BeautifulSoup(response.content,'html.parser')
#print (x.find_all("a"))
print(x)
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
import numpy as np

url = input("which page u like")
keyword =input("whta is your keywotd")
keyword=keyword.casefold()
try :
    req=Request(url,headers={'User-Agent': 'Mozilla/6.0'})
    html=urlopen(url)

except HTTPError as e:
    print(e)
data = BeautifulSoup(html,"html.parser")

def seo_title(keyword,data):
    if data.title:
        if keyword in data.title.text.casefold():
            status ="Found"
        else:
            status="Not Found"
    else:
        status="not title found"
    return status

def seo_title_stop_words(data):


    words=0
    list_words=[]
    if data.title:
        with open("stopwords.txt",'r') as f:
            for line in f:
                if re.search(r'\b'+ line.rstrip('\n')+r'\b',data.title.text.casefold()):
                    words +=1
                    print("kff0"+line)
                    list_words.append(line.rstrip('\n'))
        if words >0:
            stopwords= "we found stopwords {} in title .you should remove it{} ".format(words,list_words)
        else:
            stopwords="we found no stopwords in title"


    else:
        stop_words="we coul nt find a title"
    return stopwords

def seo_title_lenght(data):
    if data.title:
        if len(data.title.text)<60:
            lenght = "Your lenght is under max suggested lenght of character .your title is {}".format(len(data.title.text))
        else:
            lenght = "Your lenght is over max suggested lenght of character .your title is {}".format(len(data.title.text))
    else:
        lenght="No title was Found"
    return lenght
def seo_url(url):
    if url:
        if keyword in url:
            slug = "Your keyword was found in your slug"
        else:
            slug = "Your keyword is not in your slug .Its suggested to add your keyword to your slug"
        return slug
def seo_url_lenght(ulr):
    if url:
        if len(url)<100:
            url_lenght="your url lenght is less then 100"
        else:
            ulr_lenght="your url lenght is over 100"
    else:
        url_lenght="no url"
    return url_lenght

print(seo_title(keyword,data))
print(seo_title_stop_words(data))

print(seo_title_lenght(data))
print(seo_url(url))
print(seo_url_lenght(url))

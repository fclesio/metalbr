# -*- coding:utf-8 -*-
import requests
from multiprocessing import Pool
from pyquery import PyQuery
from tqdm import tqdm

BASE_URL = "https://www.letras.mus.br"
ANGRA = "/angra/"
#ANGRA = "/mais-acessadas/sertanejo/"

def get_top1000_page():
    retry = 3
    response = None
    while(retry):
        try:
            response = requests.get(BASE_URL + ANGRA)
            if 200 <= response.status_code < 300:
                break
            else:
                retry -= 1
        except:
            retry -= 1
    return response
    
    resp = get_top1000_page()
    
# Faz o parsing na página das músicas do top 1000 e extrai todas as hrefs de letras
def get_top1000_urls(response):
    pq = PyQuery(response.text)
    hrefs = [i.attr('href') for i in pq('cnt-list').items()]
    return hrefs
    

pq = PyQuery(resp.text)
for i in pq:
    print(i)
    
    
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs4
soup = BeautifulSoup(resp.text, 'html.parser')

mydivs = soup.findAll("div", {"class": "artista-todas"})

soup = BeautifulSoup(resp.text, 'lxml')
for li in soup.find_all(class_="cnt-list--alp"):
    #print(li)
    print(li.a.get('href'))
    
    if(li.a.get('href') is not None):
        print(li.a.get('href'))
    else:
        print("X1 variable is Null or None")
        
        
soup = BeautifulSoup(resp.text, 'html.parser') # making the soup
IsoUrl = soup.find_all(class_="cnt-list")

#print(soup.prettify())

#soup.find_all('a')

musicas = []
for link in soup.find_all('a'):
    #print(link.get('href'))
    
    value = link.get('href')
    musicas.append(link.get('href'))
    
    
filter(lambda k: 'angra' in k, musicas)


xxx = filter(lambda k: '/angra/' in k, musicas)
for i in xxx:
    print(i)

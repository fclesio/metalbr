# -*- coding:utf-8 -*-
import requests
from multiprocessing import Pool
from pyquery import PyQuery
from tqdm import tqdm

BASE_URL = "https://www.letras.mus.br"
SERTANEJO_TOP = "/mais-acessadas/sertanejo/"

# Captura a página onde estão listadas as músicas do top 1000
def get_top1000_page():
    retry = 3
    response = None
    while(retry):
        try:
            response = requests.get(BASE_URL + SERTANEJO_TOP)
            if 200 <= response.status_code < 300:
                break
            else:
                retry -= 1
        except:
            retry -= 1
    return response

# Faz o parsing na página das músicas do top 1000 e extrai todas as hrefs de letras
def get_top1000_urls(response):
    pq = PyQuery(response.text)
    hrefs = [i.attr('href') for i in pq('ol.top-list_mus.cnt-list--col1-3 a').items()]
    return hrefs

# Captura a página da música e extrai as informações de título, interprete e letra
def fetch_lyrics(url):
    retry = 3
    response = None
    while(retry):
        try:
            response = requests.get(BASE_URL + url)
            if 200 <= response.status_code < 300:
                break
            else:
                retry -= 1
        except:
            retry -= 1
            
    pq = PyQuery(response.text)
    title, artist = pq('div.cnt-head_title').text().split('\n')
    lyrics = pq('div.cnt-letra.p402_premium').text()
    return (title, artist, lyrics)


# Processamento paralelo utilizando um Pool de threads
def mmap(function, iterable):
    p = Pool()
    result = list(tqdm(p.imap(function, iterable), total=len(iterable)))
    p.close()
    return result

resp = get_top1000_page()
hrefs = get_top1000_urls(resp)
title_artist_lyrics = mmap(fetch_lyrics, hrefs)


# Transformação das tuplas em um Dataframe
import pandas as pd
songs = pd.DataFrame(title_artist_lyrics, columns=["title", "artist", "lyrics"])
songs.head()

from dotenv import load_dotenv
from keys import PVT_KEY, APY_KEY
from time import time
from model.hero import Heroi, HeroiConvocado


import os
import hashlib
import requests

load_dotenv()


def get_hash():
    ts = int(time())
    pvt = PVT_KEY
    apikey = APY_KEY
    # hashed = '313d8b70628db1284d42404a965d6044'

    cripto = str(ts) + pvt + apikey

    hash_mervel = hashlib.md5(cripto.encode()).hexdigest()

    return ts, apikey, hash_mervel


def busca_herois(search):
    info_hash = get_hash()
    params = {
        "limit": 100,
        "ts": info_hash[0],
        "apikey": info_hash[1],
        "hash": info_hash[2],
    }
    if search:
        params['name'] = search

    resp = requests.get('https://gateway.marvel.com:443/v1/public/characters', params)
    json = resp.json()
    data = json['data']
    results = data['results']
    return results


def get_convocado(id):
    info_hash = get_hash()
    params = {
        "ts": info_hash[0],
        "apikey": info_hash[1],
        "hash": info_hash[2],
    }

    resp = requests.get('https://gateway.marvel.com:443/v1/public/characters/' + str(id), params)
    json = resp.json()
    data = json['data']
    results = data['results']
    return results[0]


def get_convocados(convocados):
    convocados_list = []
    for hero in convocados:
        item = get_convocado(hero.hero_id)
        item['dbId'] = hero.id
        item['dbType'] = hero.type
        convocados_list.append(item)

    return map(lambda hero: HeroiConvocado(
        hero['id'],
        hero['thumbnail']['path'] + "." + hero['thumbnail']['extension'],
        hero['name'],
        hero['description'],
        hero['dbId'],
        hero['dbType']
    ), convocados_list)


def herois(search):
    lista = busca_herois(search)
    return map(lambda hero: Heroi(
        hero['id'],
        hero['thumbnail']['path'] + "." + hero['thumbnail']['extension'],
        hero['name'],
        hero['description'],
    ), lista)




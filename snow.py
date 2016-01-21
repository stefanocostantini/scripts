#!/usr/bin/env python

import requests
from BeautifulSoup import BeautifulSoup
import pytumblr
import time

url = 'http://www.dolomitisuperski.com/en/ski-area/val-di-fassa/weather'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

tables = soup.findAll('div', attrs={'class': 'col col-sm-6'})

table = tables[1].find('table', attrs={'class': 'table table-not-auto no-hover table-wetter-detail'})

snow = table.findAll('td', attrs={'class': 'big'})

date_raw = tables[1].find('div', attrs={'class': 'text-white'})

valley = snow[0].text
mountain = snow[1].text
last = snow[2].text
date = date_raw.text

key = 'nSzFKCgG1S7Bw24XbFeKNQ9J1loSMSfNS5bfSPt5C9lwDOYyqc'
secret = 'N22mXvMvhxCM6fUlMOVRLvEe0IA1JymRSAiSrI1SA7wcKEACtz'
token = 'pRjGlpDImJeAVohedJgBlYb4M0Eo1KwP0PcEbKbOOxFIpnaYv4'
tokenSecret = 'lPk64Pd7srtVnhityD5I4Lr8m8TMJDO86QddHH4wQFunMH10zY'


client = pytumblr.TumblrRestClient(
    key,
    secret,
    token,
    tokenSecret,
)

current = time.strftime("%d/%m/%Y")

client.create_text("snow-report", state="published", slug="snow-report", title=current, body="Valley: " + valley + " | Mountain: " + mountain + " | Last snowfall: " + last + " on " + date)


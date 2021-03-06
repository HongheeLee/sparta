import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select("#body-content > div.newest-list > div > table > tbody > tr")

for song in songs:
    rank = song.select_one("td.number").text.split()[0].strip()
    title = song.select_one("td.info > a.title.ellipsis").text.strip()
    singer = song.select_one("td.info > a.artist.ellipsis").text
    print(rank, title, singer)

    doc = {"rank":rank, "title":title, "singer":singer}
    db.genie_chart.insert_one(doc)


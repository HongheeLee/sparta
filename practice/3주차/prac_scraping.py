import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기

trs = soup.select("#old_content > table > tbody > tr")

# 영화 제목들 출력하기
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(7) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(2) > td.point
for tr in trs:
    title = tr.select_one("td.title > div > a")
    if title:
        title = title.text
        ranking = tr.select_one("td:nth-child(1) > img")["alt"]
        rating = tr.select_one("td.point").text
        print(ranking, title, rating)
    
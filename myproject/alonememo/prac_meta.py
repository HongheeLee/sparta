import requests
from bs4 import BeautifulSoup

url = 'https://platum.kr/archives/120958'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.
# <meta property="og:title" content="[Startup’s Story #449] 중국서 공유주택 열기 일으킨 창업가, 한국서 이어간다 - 'Startup's Story Platform’">
# head > meta:nth-child(28)
# <h1> .... </h1> --> title.text
og_image = soup.select_one('meta[property="og:image"]')
og_title = soup.select_one('meta[property="og:title"]')
og_description = soup.select_one('meta[property="og:description"]')

# print(og_description, og_image, og_title)

title = og_title.get("content")
image = og_image.get("content")
desc = og_description.get("content")

# title = og_title["content"]

print(title, image, desc)
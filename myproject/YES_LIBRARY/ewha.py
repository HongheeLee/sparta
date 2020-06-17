from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
driver = webdriver.Chrome(r'C:\Users\HongheeLee\chromedriver')

# URL 설정 및 브라우저 실행
keyword = '쇼코의+미소+최은영'
url_ewha = "http://lib.ewha.ac.kr/search/tot/result?st=KWRD&si=TOTAL&websysdiv=tot&q=" + keyword
driver.get(url_ewha)

# 대출현황 보기 위해 토글 열기
# 유독 이대 도서관 홈페이지에서 클릭이 불규칙적임. 어떤 토글은 열릴 때도 있고 아닐 때도 있고, 잘못 클릭해서 다른 페이지로 넘어갈 때도 있고.
jss = driver.find_elements_by_xpath("//p[@class='location']/a/span")
for js in jss:
    js.click()

# 크롤링 토대
time.sleep(5)
req = driver.page_source
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
soup = BeautifulSoup(req, 'html.parser')
lis = soup.select("div.result > form > fieldset > ul > li")
tables = soup.select("table")


# 도서 정보 가져오기
count = 0
for li in lis:
    title = li.select_one("dl > dd.title > a").text.split("/")[0].strip()
    img = li.select_one("dl > dd.book > a > img")['src']
    author = li.select_one("dl > dd.title > a").text.split("/")[1].strip()
    company = li.select_one("dl > dd.info").text.split(",")[0].split(":")[1].strip()
    year = li.select_one("dl > dd.info").text.split(",")[1].strip()
    locs = li.select("dl > dd.holdingInfo > div > p.location > a")
    print(title, img, author, company, year)
    for loc in locs:
        if loc:
            print(loc.text)
    count += 1
    if count == 2:
            break

# 대출 현황 데이터프레임 형태로 가져오기
count2 = 0
for table in tables:
    table_html = str(table)
    table_df_list = pd.read_html(table_html)
    table_df = table_df_list[0]
    print(table_df)
    count2 += 1
    if count2 == 2:
        break
    
driver.close()
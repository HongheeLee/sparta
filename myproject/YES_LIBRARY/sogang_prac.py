from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(r'C:\Users\HongheeLee\chromedriver')
import pandas as pd
import time

# URL 설정 및 브라우저 실행
keyword = '쇼코의+미소+최은영'
url_sogang = "https://library.sogang.ac.kr/searchTotal/result?st=KWRD&si=TOTAL&q=" + keyword
driver.get(url_sogang)

# 대출현황 보기 위해 토글 열기
jss = driver.find_elements_by_xpath("//p[@class='location']")
for js in jss:
    js.click()

# 크롤링 토대
time.sleep(2)
req = driver.page_source
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
soup = BeautifulSoup(req, 'html.parser')
lis = soup.select("#catalogs > ul > li")
tables = soup.select("table")

# 도서 정보 가져오기
count = 0
for li in lis:
    title = li.select_one("p > a").text
    bookcover = li.select_one("div.information > p.bookCover > img")['src']
    author = li.select_one("div.information > p:nth-child(2)").text
    company = li.select_one("div.information > p:nth-child(3)").text
    year = li.select_one("div.information > p:nth-child(4)").text
    loc = li.select_one("div.holdingInfo > div > p > a").text

    print(title, bookcover, author, company, year, loc)
    # 원하는 권수만큼 크롤링하고 반복문 종료.
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
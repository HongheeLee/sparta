import requests
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(r'C:\Users\HongheeLee\chromedriver')
import time

keyword = '쇼코의+미소+최은영'
url_sogang = "https://library.sogang.ac.kr/searchTotal/result?st=KWRD&si=TOTAL&q=" + keyword

driver.get(url_sogang)
driver.find_element_by_xpath("//p[@class='location']").click()
time.sleep(3)
req = driver.page_source
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(url_sogang, headers=headers,verify= False)
soup = BeautifulSoup(req, 'html.parser')
lis = soup.select("#catalogs > ul > li")


count = 0
for li in lis:
    title = li.select_one("p > a").text
    bookcover = li.select_one("div.information > p.bookCover > img")['src']
    author = li.select_one("div.information > p:nth-child(2)").text
    company = li.select_one("div.information > p:nth-child(3)").text
    year = li.select_one("div.information > p:nth-child(4)").text
    loc = li.select_one("div.holdingInfo > div > p > a").text
    loanBook = li.select_one("#holdingW_CAT000000795123_1 > div > table > tbody > tr > td").text

    print(title, bookcover, author, company, year, loc, loanBook)
    # 원하는 권수만큼 크롤링하고 반복문 종료.
    count += 1
    if count == 1:
        break

driver.close()
#holdingW_CAT000000795123_1 > div > table > tbody > tr.first > td.num.footable-first-column
#holdingW_CAT000000795123_1 > div > table
#holdingW_CAT000000795123_1 > div > table > tbody > tr.first > td.location
# bookcover = soup.select_one()
#holdingW_CAT000000795123_1 > div > table > tbody > tr.first.footable-detail-show > td.location.footable-last-column
#catalogs > ul > li:nth-child(1) > div.holdingInfo > div > p > a
# for li in lis:
#     title = lis.select_one("p > a > span").text
#     print(title)
#bookImg_CAT000000795123
#catalogs > ul > li:nth-child(1) > div.information > p.bookCover
#catalogs > ul > li:nth-child(1) > div.information > p:nth-child(2)
#catalogs > ul > li:nth-child(1) > div.information > p:nth-child(3)

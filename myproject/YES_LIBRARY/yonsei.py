from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(r'C:\Users\HongheeLee\chromedriver')
import pandas as pd
import time

# URL 설정 및 실행
keyword = '쇼코의+미소+최은영'
url_yonsei = "https://library.yonsei.ac.kr/main/searchBrief?q=" + keyword
driver.get(url_yonsei)

# 대출 현황 보기 위해 토글 열기
campus = list(driver.find_elements_by_xpath("//a[@class='availableBtn']"))
for i in range(len(campus)):
    campus[i].click()
    locs = list(driver.find_elements_by_xpath("//div[@class='locationList']"))
    locs[i].click()
        
# 크롤링 토대
time.sleep(3)
req = driver.page_source
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
soup = BeautifulSoup(req, 'html.parser')
divs = soup.select("#divContent > div.searchResult > div.pcWrap > div.mid > div > div.sectionList > div")

# 도서 정보 가져오기
count1 = 0
for div in divs:
    title = div.select_one("dl > dt > a").text
    img = div.select_one("dd.imgList > a > span > img")['src']
    author = div.select_one("dd.imgList > ul > li:nth-child(1)").text
    company = div.select_one("dd.imgList > ul > li:nth-child(2)").text
    year = div.select_one("dd.imgList > ul > li:nth-child(3)").text
    print(title, img, author, company, year)

    # 대출 현황 가져오기
    cams = div.select("a.availableBtn")
    locs = div.select("div.locationList")
    for i in range(len(cams)):
        cam = cams[i].parent.text
        loc = locs[i].select_one("dl > dt").text
        nums = locs[i].select("dl> dd > ul > li > p > a")
        print(cam, loc)
        for num in nums:
            print(num.text)
    # 원하는 만큼 크롤링하고 반복문 종료
    count1 += 1
    if count1 == 2:
        break

driver.close()
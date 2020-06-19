from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Users\HongheeLee\chromedriver')
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# # 혹은 options.add_argument("--disable-gpu")

# driver = webdriver.Chrome(r'C:\Users\HongheeLee\chromedriver', chrome_options=options)
    
api = {'libraryStatus': 
    {
    'sogang': [],
    'yonsei': [],
    'ewha' : []
    }
}

def sogang_search(keyword):
    url_sogang = "https://library.sogang.ac.kr/searchTotal/result?st=KWRD&si=TOTAL&q=" + keyword
    driver.get(url_sogang)

     # 대출현황 보기 위해 토글 열기
    jss = driver.find_elements_by_xpath("//p[@class='location']")
    js_count = 0
    for js in jss:
        js.click()
        time.sleep(1)
        js_count += 1
        if js_count == 2:
            break

    # 크롤링 토대
    time.sleep(3)
    req = driver.page_source
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    soup = BeautifulSoup(req, 'html.parser')
    lis = soup.select("#catalogs > ul > li")
    sogang_list = []
    count = 0

    for li in lis:
        sogang_dict = {}
        status_list = []
        loc_list = []
        # 가져와야 할 도서 정보 경로 지정
        title = li.select_one("p > a").text
        bookcover = li.select_one("div.information > p.bookCover > img")['src']
        author = li.select_one("div.information > p:nth-child(2)").text
        company = li.select_one("div.information > p:nth-child(3)").text
        year = li.select_one("div.information > p:nth-child(4)").text
        book_url = li.select_one("p > a")['href']
        loc = li.select_one("div.holdingInfo > div > p > a").text
        loc_list.append(loc)
        trs = li.select("div.holdingInfo > div > div > div > table > tbody > tr")
        
        # 표 안에 있는 정보들은 한번 더 타고 들어가야 함.
        for tr in trs:
            status_dict = {}
            book_loc = tr.select_one("td.location").text
            callnum = tr.select_one("td.callNum").text
            borrow = tr.select_one("td.bookStatus").text

            status_dict['book_loc'] = book_loc
            status_dict['callnum'] = callnum
            status_dict['borrow'] = borrow
            status_list.append(status_dict)
        
        # dict에 추가
        sogang_dict['title']=title
        if (bookcover[0] != '/'):
            sogang_dict['bookcover']=bookcover
        sogang_dict['author']=author
        sogang_dict['company']=company
        sogang_dict['year']=year
        sogang_dict['book_url'] = book_url
        sogang_dict['loc']=loc_list
        sogang_dict['status'] = status_list

        sogang_list.append(sogang_dict)
        
        # 원하는 권수만큼 크롤링하고 반복문 종료.
        count += 1
        if count == 2:
            break

        # api에 추가
        api['libraryStatus']['sogang']= sogang_list
        api['libraryStatus']['url_sogang'] = url_sogang

def yonsei_search(keyword):
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
    yonsei_list = []

    # 가져와야 할 도서 정보 경로 지정
    count1 = 0
    for div in divs:
        yonsei_dict = {}
        loc_list = []
        status_list = []

        title = div.select_one("dl > dt > a").text
        bookcover = div.select_one("dd.imgList > a > span > img")['src']
        author = div.select_one("dd.imgList > ul > li:nth-child(1)").text
        company = div.select_one("dd.imgList > ul > li:nth-child(2)").text
        year = div.select_one("dd.imgList > ul > li:nth-child(3)").text
        book_url = "https://library.yonsei.ac.kr/" + div.select_one("dl > dt > a")['href']
        locs = div.select("a.availableBtn")
        docs = div.select("div.locationList")

        # 표 안에 있는 정보들은 한번 더 타고 들어가야 함.
        for loc in locs:
            location = loc.parent.text
            loc_list.append(location)
            lis = loc.parent.parent.select("div > dl > dd > ul > li")
            for li in lis:
                status_dict = {}
                book_loc = li.parent.parent.parent.select_one("dt").text
                callnum = li.select_one("p:nth-child(1) > a").text
                borrow = li.select_one("p:nth-child(2) > a > span").text
                status_dict['book_loc'] = book_loc
                status_dict['callnum'] = callnum
                status_dict['borrow'] = borrow
                status_list.append(status_dict)

        # dict에 추가     
        yonsei_dict['title']=title
        if (bookcover[0] != '/'):
            yonsei_dict['bookcover']=bookcover
        yonsei_dict['author']=author
        yonsei_dict['company']=company
        yonsei_dict['year']=year
        yonsei_dict['book_url'] = book_url
        yonsei_dict['loc'] = loc_list
        yonsei_dict['status'] = status_list

        yonsei_list.append(yonsei_dict)
        
        # 원하는 권수만큼 크롤링하고 반복문 종료.
        count1 += 1
        if count1 == 2:
            break

    # api에 추가       
    api['libraryStatus']['yonsei'] = yonsei_list
    api['libraryStatus']['url_yonsei'] = url_yonsei

def ewha_search(keyword):
    url_ewha = "http://lib.ewha.ac.kr/search/tot/result?st=KWRD&si=TOTAL&websysdiv=tot&q=" + keyword
    driver.get(url_ewha)

    # 대출현황 보기 위해 토글 열기
    jss = driver.find_elements_by_xpath("//p[@class='location']/a/span")
    js_count = 0
    for js in jss:
        js.click()
        time.sleep(0.5)
        js_count += 1
        if js_count == 2:
            break

    # 크롤링 토대
    time.sleep(5)
    req = driver.page_source
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    soup = BeautifulSoup(req, 'html.parser')
    lis = soup.select("div.result > form > fieldset > ul > li")
    ewha_list = []

    # 가져와야 할 도서 정보 경로 지정
    count = 0
    for li in lis:
        ewha_dict = {}
        loc_list = []
        status_list =[]

        title = li.select_one("dl > dd.title > a").text.split("/")[0].strip()
        bookcover = li.select_one("dl > dd.book > a > img")['src']
        author = li.select_one("dl > dd.title > a").text.split("/")[1].strip()
        company = li.select_one("dl > dd.info").text.split(",")[0].split(":")[1].strip()
        year = li.select_one("dl > dd.info").text.split(",")[1].strip()
        book_url = li.select_one("dl > dd.book > a")['href']
        locs = li.select("dl > dd.holdingInfo > div > p.location > a")
        divs = li.select("dl > dd.holdingInfo > div > div.holdingW")

        for loc in locs:
            if loc:
                loc = loc.text
                loc_list.append(loc)

        # 표 안에 있는 정보들은 한번 더 타고 들어가야 함.
        for div in divs:
            status_dict = {}
            trs = div.select("div.listTable > table > tbody > tr")
            for tr in trs:
                book_loc = tr.select_one("td.location.expand").text
                callnum = tr.select_one("td.callNum").text
                borrow = tr.select_one("td > span").text
                status_dict['book_loc'] = book_loc
                status_dict['callnum'] = callnum
                status_dict['borrow'] = borrow
                status_list.append(status_dict)

        # dict에 추가
        ewha_dict['title']=title
        if (bookcover[0] != '/'):
            ewha_dict['bookcover']=bookcover
        ewha_dict['author']=author
        ewha_dict['company']=company
        ewha_dict['year']=year
        ewha_dict['book_url'] = book_url
        ewha_dict['loc']=loc_list
        ewha_dict['status'] = status_list

        ewha_list.append(ewha_dict)

        # 원하는 권수만큼 크롤링하고 반복문 종료.
        count += 1
        if count == 2:
                break
    # api에 추가
    api['libraryStatus']['ewha']= ewha_list
    api['libraryStatus']['url_ewha'] = url_ewha



## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('main.html')

@app.route('/result')
def result():
    keyword = request.args.get('keyword_give')
    return render_template('result.html', keyword = keyword)

## API 역할을 하는 부분
# @app.route('/result/', methods=['POST'])
# def get_keyword():
#    keyword_receive = request.form['keyword_give']
#    return jsonify({'result':'success', 'msg': '검색 완료'})

@app.route('/result/getlist', methods=['GET'])
def give_result():
    keyword_receive = request.args.get('keyword_give')
    sogang_search(keyword_receive)
    yonsei_search(keyword_receive)
    ewha_search(keyword_receive)

    return jsonify({'result': "success", 'msg':'정상 처리되었습니다.', 'row':api})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
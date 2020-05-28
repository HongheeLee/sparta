from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  

song_by_singer = list(db.genie_chart.find({"singer": "아이유 (IU)"}))
print(len(song_by_singer))

for song in song_by_singer:
    print(song['title'])




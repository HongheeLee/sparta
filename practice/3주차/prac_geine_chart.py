from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  

song_targ = db.genie_chart.find_one({"title": "Blueming"})
print(song_targ["singer"])

singer_targ = song_targ["singer"]

songs = list(db.genie_chart.find({"singer":singer_targ}))
print(len(songs))

for song in songs:
    print(song["title"])

db.genie_chart.update_many({"singer":singer_targ}, {"$set":{"rank":'10'}})
# song_by_singer = list(db.genie_chart.find({"singer": "아이유 (IU)"}))
# print(len(song_by_singer))

# for song in song_by_singer:
#     print(song['title'])

# db.genie_chart.update_many({"singer":"아이유 (IU)"}, {"$set":{"singer":}})
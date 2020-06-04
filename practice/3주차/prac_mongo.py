from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

mov_targ = db.movies.find_one({"title":"매트릭스"})
print(mov_targ["star"])

star_targ = mov_targ["star"]

same_stars = list(db.movies.find({"star": star_targ}))
print(len(same_stars))

for movie in same_stars:
    print(movie["title"])
    
db.movies.update_many({"star": star_targ}, {"$set":{"star": '0.00'}})


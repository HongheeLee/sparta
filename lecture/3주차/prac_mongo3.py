from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


# 영화 제목 '매트릭스'의 평점 가져오기

movie_targ = db.movies.find_one({"title": "매트릭스"})
print(movie_targ["star"])

# 매트릭스의 평점과 같은 평점의 영화 제목들을 가져오기
star_targ = movie_targ["star"]
same_star = list(db.movies.find({'star': star_targ}))
# print(len(same_star))

for movie in same_star:
    print(movie['title'])


# 이 영화들의 평점을 0으로 만들기

db.movies.update_many({"star": star_targ}, {'$set':{'star':'0.00'}})

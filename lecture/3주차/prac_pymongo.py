from pprint import pprint
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# db.users.insert_one({"name": "bobby", "age": 21})
# db.users.insert_one({"name": "kay", "age": 27})
# db.users.insert_one({"name": "john", "age": 30})

all_users = list(db.users.find())
# pprint(all_users)

bobbys = list(db.users.find({'name':'bobby'}, {'_id': False}))
# pprint(bobbys)

kay = db.users.find_one({'name':'kay'}, {'_id' : False})
# print(kay)

# db.users.update_one({'name': 'john'}, {'$set':{'name': 'jack', 'age': 20}})
db.users.update_many({'name':'bobby'}, {'$set': {'occupation': 'student'}})

db.users.delete_one({'name':'bobby', 'age': 21})
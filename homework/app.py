from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('shoppingmall.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_orders():
    name = request.form['name_give']
    num = request.form['num_give']
    address = request.form['address_give']
    phone_num = request.form['phone_num_give']

    doc = {
        'name':name,
        'num':num,
        'address':address,
        'phone_num':phone_num
    }

    db.shoppingmall.insert_one(doc)
    return jsonify({'result':'success', 'msg': '주문이 완료되었습니다.'})


@app.route('/orders', methods=['GET'])
def read_orders():
    order_list = list(db.shoppingmall.find({}, {'_id':False}))

    return jsonify({'result':'success', 'msg': '이 요청은 GET!', 'order_list':order_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
# from pprint import pprint

print("Hello, World")

text = "aaaa"
text = 'aaaa'
text = """ dddd
            sssss
            ssfef"""
text = '''asdd'''

a_list = []
a_list = [1, 2, 3, 'aaa', [1, 2, 0]]
print(a_list[4][1])

a_dict = {}
a_dict = {"key": 3, "bob": "2134"}
print(a_dict["bob"])

people = [{"age": 20, "name": "bob"}, {"age": 38, "name": "carry"}]
print(people[0]["age"])

person = {"age": 28, "name":"carry"}
people.append(person)

# pprint(people)

# 함수
def sumsum(num1, num2):
    result = num1+num2
    return num1 + num2

c = sumsum(3, 5)
print(c)

# 조건문

a = 3
if a % 2 == 1:
    print("a is odd")
else:
    print("a is even")


x = 120

if x < 100:
    print(1)
elif x < 200:
    print(2)
else:
    print(3)

# 반복문

"""
let a_list = [2, 3, 4, 5, 6]
for (let i = 0; i <a_list.length; i++) {
    console.log(a_list[i])
}
"""
a_list = [2, 3, 4, 5]
for i in range(len(a_list)):
    print(a_list[i])

for i in a_list:
    print(a/7)

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
count_apple = 0
for fruit in fruits:
    if fruit == "사과":
        count_apple = count_apple + 1

print(count_apple)

"""
리스트가 주어졌을 때 임의의 과일(fruit_x)의 개수를 세주는 함수 만들기

def count_fruit(fruits, fruit_x):
"""
fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
def count_fruit(fruit_list, fruit_x):
    count = 0

    for fruit in fruit_list:
        if fruit == fruit_x:
            count = count+1
    return count

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
print(count_fruit(fruits, "감"))
print(count_fruit([1, 2, 3, 4, 5], 5))


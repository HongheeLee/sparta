print("Hello, World!")

a = 5
b = 3

print(a + b)

a_list = ["사과", "배", "귤"]

print(a_list[2])

a_list.append("배")

a_dict = {"name" : "bob", "age": 30}

a_dict["height"] = 178

a_list.append(a_dict)

print(a_list[4])


def is_adult(age):
    if age < 50:
        print("오십이하")
    elif age < 80:
        print("팔십이하")
    else:
        print("팔십이상")

is_adult(60)

def sumsum(num1, num2):
    result = num1 + num2
    return result

print(sumsum(4, 6))

# fruits = ['사과','배','감','귤']

# for fruit in fruits:
#     print(fruit)

# for i in range(len(fruits)):
#     print(fruits[i])

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']


def count_fruit(name, fruit_list):
    count = 0
    for fruit in fruit_list:
        if fruit == name:
            count += 1
    return count

result = count_fruit("배", fruits)
print(result)

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

for person in people:
    print(person["name"], person["age"])

def get_age(name):
    for person in people:
        if person["name"] == name:
            return person["age"]
    print("해당하는 이름이 없습니다.")
            

result = get_age("john")
print(result)


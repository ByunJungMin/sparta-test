# 예외처리

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby'},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
   try:   # 예외 구문 
      if person['age'] > 20:
         print(person['name'])
   except: # try 에서 에러가 났을경우
      print(person['name'], '에러입니다')
# map, filter, lambda

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

def check_adult(person):                                                          # check_adult 함수
   return ('성인' if person['age'] > 20 else '청소년')


result = map(check_adult, people)                                                 # people 을 돌면서 check_adult에 넣어라

print(list(result))

''''''''''''''''''''''''''

result = map(lambda person : ('성인' if person['age'] > 20 else '청소년'), people) # people를 돌면서 person에다 값을 넣을건데 : 을 기준으로 오른쪽에 있는 함수를 적용할거다
                                                                                  # lambda 함수를 한줄로 줄여쓰기 위한 표현식
print(list(result))


result = filter(lambda person : person['age'] > 20, people)                       # filter 조건에 맞는것만 출력

print(list(result))

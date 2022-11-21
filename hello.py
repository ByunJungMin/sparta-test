# 튜플
a = [1,2,3,4,5] # 리스트 양식
b = (1,2,3,4,5) # 튜플 양식

# a[1] = 5 # 튜플은 불변형이라 수정이나 추가가 불가능

print(a, b)   

# 집합

student_a = ['물리2','국어','수학1','음악','화학1','화학2','체육']
student_b = ['물리1','수학1','미술','화학2','체육']

set_a = set(student_a) # 중복 제거
set_b = set(student_b) 

print(set_a & set_b) # 교집합
print(set_a | set_b) # 합집합
print(set_a - set_b) # 차집합
print(set_a.difference(set_b)) # 차집합
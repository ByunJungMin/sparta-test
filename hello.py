# 한줄로 줄여 쓰기

num = 3

'''   기본적인 if 문
if num % 2 == 0:
   result = '짝수'
else:
   result = '홀수'
'''
result = ('짝수' if num % 2 == 0 else '홀수') # 한줄로 줄여 쓰기

print(f'{num}은 {result}입니다')


a_list = [1,3,2,4,1,2]

b_list = []

'''   기본적인 for 문
for a in a_list:
   b_list.append(a*2)
'''

b_list = [a*2 for a in a_list] # 한줄로 줄여 쓰기

print(b_list)
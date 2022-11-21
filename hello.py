# f-string

scores = [
    {'name':'영수','score':70},
    {'name':'영희','score':65},
    {'name':'기찬','score':75},
    {'name':'희수','score':23},
    {'name':'서경','score':99},
    {'name':'미주','score':100},
    {'name':'병태','score':32}    
]

for s in scores:
  name = s['name']
  score = str(s['score']) # 숫자를 문자열로 변환
  print(name + '의 점수는 ' + score + '점 입니다.') # f-string 없이 나타낼 때
  print(f'{name}의 점수는 {score}점 입니다.') # f-string 적용시
  
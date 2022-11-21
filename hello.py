# 함수 인자 다루는 법

def cal(a,b):
   return a + 2 * b

result = cal(a=1,b=2)   # a=1 b=2 처럼 값을 고정해서 넘겨줄 경우 순서에 상관이 없다.
                        # ex) (b=2,a=1)  
print(result)

''''''''''''

def cal(a,b=2):         # 매개변수에 값을 정해준 경우 넘겨받는 값이 없으면 기존에 설정 되어 있는 값으로 진행한다.
   return a + 2 * b

result = cal(a=1)       
                       
print(result)



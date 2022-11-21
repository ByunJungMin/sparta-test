# 함수

def check_gender(pin):
   num = pin.split('-')[1][:1]
   num = int(num)
   if num % 2 == 0:
      print('여자입니다')
   else:
      print('남자입니다')



check_gender('150101-1012345')
check_gender('150101-2012345')
check_gender('150101-4012345')
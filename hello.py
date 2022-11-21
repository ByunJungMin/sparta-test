# 클래스

class Monster():                   # class 선언
   hp = 100
   alive = True

   def damage(self, attack):       # damage 함수
      self.hp = self.hp - attack
      if self.hp < 0:
         self.alive = False


   def status_check(self):         # status_check 함수
      if self.alive == True:
         print('살았다')
      else:
         print('죽었다')



m1 = Monster()                      # m1을 인스턴스라 한다
m1.damage(150)
m1.status_check()

m2 = Monster()                      # m2도 인스턴스
m2.damage(90)
m2.status_check()

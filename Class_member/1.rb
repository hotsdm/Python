require 'date'
d1 = Date.new(2000, 1, 1)
d2 = Date.new(2010, 1, 1)
p d1.year() # 인스턴스 소속 (d1)
p d2.year() # 인스턴스 소속 (d2)
p Date.today() # Date 라는 클래스의 소속 (Date)
               # 인스턴스 값과는 상관 없음. 클래스의 맴버

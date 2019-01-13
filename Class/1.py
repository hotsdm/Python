class Cal(object): # object는 써도 되고 안 써도 됨. 상속과 관련된 것
    def __init__(self, v1, v2): # 첫 번째 매개 변수(self, 이름 바꿔도 됨)는 꼭 지정해야 함! 인스턴스 변수 지정 시 앞에 붙음
        self.v1 = v1
        self.v2 = v2

    def add(self): #self를 기입해야 인스턴스 변수를 사용할 수 있음
        return self.v1 + self.v2
        
    def subtract(self):
        return self.v1 - self.v2

c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())

c2 = Cal(30,20)
print(c2.add())
print(c2.subtract())
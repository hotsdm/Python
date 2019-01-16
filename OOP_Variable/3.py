class Cal(object): 
    def __init__(self, v1, v2): 
        self.v1 = v1
        self.v2 = v2

    def add(self): 
        return self.v1 + self.v2
        
    def subtract(self):
        return self.v1 - self.v2

    def setV1(self, v1):
        if isinstance(v1, int): # 첫 번째 인자(v1)가 만약 int 라는 class에 해당 된다면 True, 아니면 Flase
                                # 단순히 c1.v1 = 20 를 할 경우, isinstance 처럼 입력값을 확인할 수 있는 방법이 없음 (메소드로서 작성한 이유임!)
            self.v1 = v1
            
    def getV1(self):
        return self.v1

c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())
c1.setV1('one')
c1.setV1(20)
print(c1.add())
print(c1.getV1())
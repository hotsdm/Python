class Cal(object): 
    def __init__(self, v1, v2): 
        self.v1 = v1
        self.v2 = v2

    def add(self): 
        return self.v1 + self.v2
        
    def subtract(self):
        return self.v1 - self.v2

    def setV1(self, v1):
        if isinstance(v1, int): 
            self.v1 = v1
            
    def getV1(self):
        return self.v1

class CalMultiply(Cal):
    def multiply(self):
        return self.v1 * self.v2

class CalDivide(CalMultiply):
    def divide(self):
        return self.v1 / self.v2

# 상속을 활용하면 재활용성의 증대임
# 장기적으로는 재활용성 외에 다른 면에서도 유용함

c1 = CalMultiply(10, 10)
print(c1, c1.add())
print(c1, c1.multiply())
c2 = CalDivide(20, 10)
print(c2, c2.subtract())
print(c2, c2.divide())
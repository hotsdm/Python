class Cal(object): 
    _history = []
    def __init__(self, v1, v2): 
        self.v1 = v1
        self.v2 = v2

    def add(self): 
        result = self.v1 + self.v2
        Cal._history.append("add : %d + %d = %d " % (self.v1, self.v2, result) )
        return result
        
    def subtract(self):
        result = self.v1 - self.v2
        Cal._history.append("subtract : %d - %d = %d " % (self.v1, self.v2, result) )
        return result

    def setV1(self, v1):
        if isinstance(v1, int): 
            self.v1 = v1
            
    def getV1(self):
        return self.v1
    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)

class CalMultiply(Cal):
    def multiply(self):
        result = self.v1 * self.v2
        Cal._history.append("multiply : %d * %d = %d " % (self.v1, self.v2, result) )
        return result

class CalDivide(CalMultiply):
    def divide(self):
        result = self.v1 / self.v2
        Cal._history.append("divide : %d / %d = %d " % (self.v1, self.v2, result) )
        return result
        
# 상속을 활용하면 재활용성의 증대임
# 장기적으로는 재활용성 외에 다른 면에서도 유용함


c2 = CalDivide(20, 10)
print(c2.subtract())
print(c2.divide())
Cal.history()
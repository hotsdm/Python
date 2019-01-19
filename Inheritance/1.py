class Class1(object):
    def method1(self): 
        return 'm1'

class Class2(Class1): #Class2가 Class1의 메소드를 전부 상속한다는 의미
    def method2(self):
        return 'm2'

c1 = Class1()
print(c1, c1.method1())

c2 = Class2()
print(c2, c2.method1())
print(c2, c2.method2())

    
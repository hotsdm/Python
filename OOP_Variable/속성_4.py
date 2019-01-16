class C(object):
    def __init__(self, v): 
        self.__value = v # 변수 앞에 __ 가 붙으면 인스턴스 외부에서 접근하는 게 불가능해짐
    def show(self):
        print(self.__value)

c1 = C(10)
# print(c1.__value) # 외부에서 접근이 안 됨
c1.show() # 메소드로서는 접근 가능해짐. 메소드 안에 print + 변수값이 있기 때문(?)
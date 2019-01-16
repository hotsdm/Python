class C(object):
    def __init__(self, v): #인스턴스 변수 설정하는 생성자! init
        self.value = v #인스턴스 변수
    def show(self):
        print(self.value)


c1 = C(10)
print(c1.value)
c1.value = 20   # 인스턴스 변수의 값을 바꿀 수 있음
print(c1.value) # 메소드(함수) 밖에서 인스턴스 변수를 출력 가능함
c1.value = 30
c1.show()
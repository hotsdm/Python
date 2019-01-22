class Cs(object):
    @staticmethod   # 클래스 메소드 멤버 설정을 위한 장식자
    def static_method():
        print("Static method")
    @classmethod    # 클래스 메소드 멤버 설정을 위한 장식자
    def class_method(cls):  # cls가 꼭 들어가야 함
        print("Class method")
    def instance_method(self):
        print("Instance method")

i = Cs()
Cs.static_method()  # 클래스 메소드
Cs.class_method()   # 클래스 메소드
i.instance_method()
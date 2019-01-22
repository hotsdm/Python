# 클래스 변수

class Cs(object):
    count = 0
    def __init__(self):
        Cs.count = Cs.count + 1     
        # 위에 있는 클래스 내부의 count에 접근하기 위해서는 Cs.count여야 함 
    @classmethod                # 클래스 메소드 설정하기 위해서 입력
    def getCount(cls):          # 클래스 메소드는 첫 번째 인자로 cls를 입력
        return Cs.count

i1 = Cs()
i2 = Cs()
i3 = Cs()
i4 = Cs()
print(Cs.getCount())
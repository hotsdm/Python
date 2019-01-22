# 클래스 변수
class Cs
    @@count = 0                 # 메소드 밖 클래스 안에서 최초 값을 지정
    def initialize()
        @@count = @@count + 1    # 클래스에 속한 변수 (인스턴스랑 상관 없음)
                                # 인스턴스가 생성 될 때마다 클래스 변수값을 +1
    end
    def Cs.getCount()           # 클래스 메소드
        return @@count        
    end
end

# 여기서 count 라는 변수는 클래스 변수이기 때문에 모든 인스턴스에서 동일한 값이 됨

i1 = Cs.new()
i2 = Cs.new()
i3 = Cs.new()
i4 = Cs.new()
p Cs.getCount()

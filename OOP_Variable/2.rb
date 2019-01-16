class C
    def initialize(v)
        @value = v        
    end
    def show()
        p @value        
    end
    def getValue()
        return @value
    end
    def setValue()
        return @value = v
    end
end

c1 = C.new(10)
# p c1.value <- 메소드(함수) 밖에서 인스턴스 변수를 출력할 수 없음
p c1.getValue() # 메소드를 이용해서 인스턴스 변수를 출력할 수 있음 (getValue는 관습적 용어)
# c1.value = 20 <- 인스턴스 변수의 값을 바꿀 수 없음
c1.setValue(20) # 메소드를 이용해서 인스턴스 변수를 바꿀 수 있음 (setValue는 관습적 용어)
p c1.getValue()
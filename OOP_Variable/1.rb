class C
    def initialize(v)
        @value = v        
    end
    def show()
        p @value        
    end
end

c1 = C.new(10)
# p c1.value <- 메소드(함수) 밖에서 인스턴스 변수를 출력할 수 없음
# c1.value = 20 <- 인스턴스 변수의 값을 바꿀 수 없음
c1.show()

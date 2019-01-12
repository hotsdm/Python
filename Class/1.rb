class Cal
    def initialize(v1, v2) # 생성자(Constructor) 새로운 인스턴스가 생기면 반드시 실행됨! (=초기화)
        @v1 = v1 # 앞에 @가 붙으면 인스턴스 변수. 즉, 해당 Class 안의 모든 메소드에서 사용됨
        @v2 = v2
        # @가 붙지 않으면 지역 변수. 즉 initialize 안에서만 사용 가능
    end        

    def add()
        return @v1 + @v2
    end
    
    def subtract()
        return @v1 - @v2
    end
end

c1 = Cal.new(10,10) #c1 라는 인스턴스
p c1.add()
p c1.subtract()

c2 = Cal.new(30,20) #c2 라는 인스턴스
p c2.add()
p c2.subtract()
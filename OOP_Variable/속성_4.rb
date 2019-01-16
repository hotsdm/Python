class C
    attr_reader :value # 읽는 속성
    attr_writer :value # 쓰는 속성
    #attr_accessor :vlaue # 읽고 쓰기가 가능해짐 (reader, writer 동시) 
    # ruby에서는 attribute. value를 외부에서 읽고 쓰기가 가능한 값으로 만듦
    def initialize(v)
        @value = v        
    end
    def show()
        p @value        
    end

end

c1 = C.new(10)
c1.value = 20
p c1.value # 내부가 아닌 외부에서 접근하는 것을 속성이라고 함
c1.show
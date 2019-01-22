class Cs
    def Cs.class_method()
        p "Class method"
    end

    def instance_method()
        p "Instance method"
    end
end

i = Cs.new()
Cs.class_method()   # 클래스 메소드는 클래스의 소속으로 사용
                    # 즉, i.class_method()로는 실행 안 됨
i.instance_method() # 인스턴스 메소드는 인스턴스 소속으로 사용
                    # 즉, Cs.instance_method()로는 실행 안 됨
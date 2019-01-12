def margin(_mg, _tp):
        import math
        duty = 1.08
        cal_mg = 1 - float(_mg)
        cal_tp = int(_tp) * duty
        return math.ceil(cal_tp / cal_mg) 

input_tp = input("TP를 입력해주세요. \n")
input_mg = input("마진을 입력해주세요. \n")
print(margin(input_mg, input_tp))
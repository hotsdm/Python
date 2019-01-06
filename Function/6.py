def margin(_mg):
        return 1 - float(_mg)

def price(_tp):
        duty = 1.08
        return int(_tp) * duty

input_tp=input("TP를 입력해주세요. \n")
input_margin=input("마진을 입력해주세요. \n (관세는 8% 고정. 마진 5%인 경우, 0.05 입력) \n")

import math
print(math.ceil(price(input_tp)/margin(input_margin)))
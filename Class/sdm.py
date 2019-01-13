class Cal_margin(object):
        def __init__(self, tp, mg):
                self.tp = int(tp)                
                self.mg = 1 - float(mg)
                self.duty_ise = 1.08
                self.duty_ksc = 1.05                

        def ksc_m(self):
                import math                
                ksc_tp = self.tp * self.duty_ksc
                return math.ceil(ksc_tp / self.mg)

        def ise_m(self):
                import math                
                ise_tp = self.tp * self.duty_ise
                return math.ceil(ise_tp / self.mg)

input_cust = input("고객명을 입력해주세요. \n(경신=ksc, 영화=yht, ISE=ise, 브라이스톤=bs) \n")
input_tp = input("TP를 입력해주세요. \n")
input_mg = input("마진을 입력해주세요. \n")

if input_cust == 'ksc':
        input_ksc = Cal_margin(input_tp, input_mg)
        print("계산된 경신의 SP는 " + str(input_ksc.ksc_m()) + "입니다.")
elif input_cust == 'ise':
        input_ise = Cal_margin(input_tp, input_mg)
        print(input_ise.ise_m())
elif input_cust == 'yht':
        print("아직 설정되지 않았습니다.")
elif input_cust == 'bs':
        print("아직 설정되지 않았습니다.")
else:
        print("고객명 입력이 잘못 되었습니다.")
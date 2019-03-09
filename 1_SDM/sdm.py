class Cal_margin(object):
        def __init__(self, tp, mg):
                self.tp = int(tp)           
                self.mg = 1 - float(mg)
                self.duty_ksc = 1.05  
                self.duty_ise = 1.08
        
        def ksc_m(self):
                import math                
                ksc_tp = self.tp * self.duty_ksc
                return math.ceil(ksc_tp / self.mg)

        def ise_m(self):      
                import math 
                ise_tp = self.tp * self.duty_ise
                return math.ceil(ise_tp / self.mg)

input_cust = input("고객명을 입력해주세요. \n(경신=ksc, 영화=yht, ISE=ise, 브라이스톤=bs) \n")

customers = ['ksc','ise','yht','bs']
for cust in customers:
        if cust == input_cust:
                input_tp, input_mg = input("TP와 마진(5% = 0.05)을 입력해주세요. \n(단위는 생략하여 입력. 예시 -> 500 0.05) \n").split()
                if input_cust == 'ksc':
                        input_ksc = Cal_margin(input_tp, input_mg)
                        print("계산된 경신의 SP는 " + str(input_ksc.ksc_m()) + "입니다.")
                        import sys
                        sys.exit()
                elif input_cust == 'ise':
                        input_ise = Cal_margin(input_tp, input_mg)
                        print("계산된 ISE의 SP는 " + str(input_ise.ise_m()) + "입니다.")
                        import sys
                        sys.exit()
                elif input_cust == 'yht':
                        print("아직 설정되지 않았습니다.")
                        import sys
                        sys.exit()
                elif input_cust == 'bs':
                        print("아직 설정되지 않았습니다.")
                        import sys
                        sys.exit()
print("입력한 고객명을 확인해주세요.")
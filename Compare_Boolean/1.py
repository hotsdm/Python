import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
a=1
b=1
name="har"
print(1==1)
print(1==2)
print(1>2)
print(1<2)
print(True)
print(False)
print("항상 "+name+"님의 많은 도움 감사합니다")

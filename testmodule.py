import util
import sys
sys.path.append(r"C:\Users\JinSH\Desktop\승현이글\프로그래밍\python\temp")
#모듈의 경로를 추가해준다
import util2


print(util.INCH)
print(util.calcsum(10))
#__main__이 아니므로 테스트코드는 실행 x



print(util2.sizeofRound(int(input("size of round which radius is : "))))


#
#import rootPakage.util3 # rootPakage 는 패키지
#print("3+5= ",rootPakage.util3.add(3,5))
#

from rootPakage import *
print("3+5= ",util3.add(3,5))


#필요한 외부 모듈은 pip을 통해 설치가능

#동적코드실행 - 인터프리터 언어의 특징... 실행중에 새로운 코드 생성 가능

#simple calculator
import math

try:
    expr = input("수식을 입력하시오 :")
    print(eval(expr))
except:
    print("수식이 잘못되었습니다")

#repr : 해석기가 해석할 수 있는 값을 반환
print(str('korea'))
print(repr('korea'))

eval(repr('korea')+repr('japan'))
#eval(str('korea')+str('japan')) #error!!


#eval 과 exec의 차이 : eval은 표현식을 exec은 문장을 실행가능
#eval은 이미 있는 변수를 평가하여 해석해 반환할 뿐 새로 생성 불가
#exec은 실행된 위치에 해당하는 문자열이 코드로써 추가되는 것과 같이 작동

#eval("a = 123") #error!
exec("a = 123")
print(a)

#multiline도 가능 - indent에 주의
exec("""
for i in range(5):
    print(i, end=",")
print()
""")

#compile(source, filename, mode)
#source는 문자열 소스, filename = 파일 or '<string>' , mode는 evel or exec or single
#미리 분석해놓기에 반복시 속도 향상
code = compile("""
for i in range(5):
    print("*hello*", end = "---")
print()
""", '<string', 'exec')

for n in range(5):
    exec(code)

print("open first.py")
exec(open('first.py').read())

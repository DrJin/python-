#decorator
#함수형 언어, 함수를 변수처럼

def add(a,b):
    return a+b
def mult(a,b):
    return a*b

plus = add
print(plus(1,4))

def calc(op,a,b):
    return op(a,b)

print(calc(add,2,3))
print(calc(mult,2,3))

#지역함수 : 함수 내장함
def makeHello(message):
    def hello(name): #지역함수
        print(message + ", " + name) #반환되더라도 message가 사라지지 않는 이유 클로
    return hello #함수를 반환?!

engHello = makeHello("Hello~")
korHello = makeHello("안녕~")

engHello("Jin!")
korHello("승현~")


def para(func):
    def wrapper():
        return "<p>" + str(func()) + "</p>"
    return wrapper

@para #decorator - 원래 함수를 넣어서 새로운 함수로 바꿔 다시 대입해준다
#여기서는 para의 func에 outname을 넣은 함수를 반환해 outname에 대입해준다
def outname():
    return "진승현"

@para
def outage():
    return "23"

print(outname())
print(outage())

from functools import wraps

def div(func):
    @wraps(func) #__name__속성과 __doc__ 속성등을 보호하기 위한 처리
    def wrapper(*args, **kwargs): #인수를 가진 함수를 처리하기 위해 가변인수와 가변 키워드 인수를 추가
        return "<div>" + str(func(*args, **kwargs)) + "</div>" 
    return wrapper

@div
def outname(name): #인수를 가진 함수
    return "이름 : " + name + "님"

print(outname("진승현"))
print(outname.__name__) # @wraps(func)를 붙이지 않으면 wrapper로 뜸

#Class decorator : __call__을 이용해 '객체명'()으로 데코레이터처럼 사용 가능 @'객체명' 도 가

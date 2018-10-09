#util2.py module

PI = 3.14

def sizeofRound(r):
    return r**2 * PI

if __name__ == "__main__": #__name__은 실행중인 모듈의 이름 __main__은 단독실행시
    print("반지름 3인 구 크기 : ", sizeofRound(3))


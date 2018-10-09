#iterator

class Seq:
    def __init__(self,data):
        self.data = data
        self.index = -3
        
    def __iter__(self): #반복자를 리턴해주는 메서드
        return self
    
    def __next__(self): #순서값을 관리하며 다음 요소로
        self.index+=3 #가변적으로 하려면 size를 init에서 지정해 사용할수도
        if self.index >= len(self.data):
            raise StopIteration #이 예외가 발생시 반복 종료
        return self.data[self.index:self.index+3]

data = "일요일월요일화요일수요일목요일금요일토요일"
yoil = Seq(data)
for k in yoil:
    print(k, end=",")

print()



#generator

def seqgen(data):
    for index in range(0, len(data), 3):
       yield data[index:index+3] #제너레이터 위의 작업을 내부적으로 해줌

for k in seqgen(data):
    print(k, end=",")

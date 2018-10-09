class Human:
    def __init__(self,name,age): #self는 java에서의 this와 같은 역할,
        self.name = name
        self.age = age
    def intro(self):
        print("제 이름은 %s이고요 전 %d살입니다" %(self.name, self.age))

Jin = Human("진승현",23)
Jin.intro()
Human.intro(Jin) #두가지 호출법이 있다

class Student(Human): #상속!!
    def __init__(self,name,age,major):
        super().__init__(name,age)
        self.major = major
    def intro(self):
        super().intro()
        print("전공은 " + self.major + "입니다~")
    def study(self):
        print("공부합니다~")

Jin = Student("진승현",23,"컴공")
Jin.intro()
Jin.study()

#파이썬은 공식적으로 은폐(private)가 없다.
#그래서 getter, setter, property 함수, 데커레이터(@), __변수명 등의 방법을 이용한다
#원천적 봉쇄는 어렵다. (나중에 필요하면 그때가서 따로 알아보기

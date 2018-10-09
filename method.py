# -*- coding: cp949 -*-
class Car:
    count = 0 #class 소속 변수
    def __init__(self, name):
        self.name = name;
        Car.count+=1

    @classmethod #classmethod 데커레이터 - 클래스 전체 공유
    def outcount(cls): #cls = 클래스 변수
        print(cls.count)

    @staticmethod
    def hello():
        print("hello!! Car~")

    def __eq__(self, other): #연산자 오버로딩
        return self.name == other.name
    
    def __str__(self): #특수 메서드 __str__, __repr__, __len__ 등이 있다
        return "이름 : " + self.name

Car.outcount()
A = Car("A")
B = Car("B")
Car.outcount()


Car.hello()


C = Car("A")
if(A == B):
    print("A=B")
if(A == C):
    print("A=C")


print(str(A))

# -*- coding: cp949 -*-
class Car:
    count = 0 #class �Ҽ� ����
    def __init__(self, name):
        self.name = name;
        Car.count+=1

    @classmethod #classmethod ��Ŀ������ - Ŭ���� ��ü ����
    def outcount(cls): #cls = Ŭ���� ����
        print(cls.count)

    @staticmethod
    def hello():
        print("hello!! Car~")

    def __eq__(self, other): #������ �����ε�
        return self.name == other.name
    
    def __str__(self): #Ư�� �޼��� __str__, __repr__, __len__ ���� �ִ�
        return "�̸� : " + self.name

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

import random

count = 0
while True:
    a = random.randint(10,99)
    b = random.randint(10,99)
    op = random.choice(['+','-','*','/'])

    if op == '+':
        ans = a+b
    elif op == '-':
        if(a<b):
            a,b = b,a
        ans = a-b
    elif op == '*':
        ans = a*b
    else:
        if(a<b):
            a,b = b,a
        ans = a//b

    quiz = "%d %s %d = ?(끝낼 때는 0)" %(a, op, b)
    c = int(input(quiz))

    if c == 0:
        break
    elif c == ans:
        print("정답입니다!!")
        count+=1
    else:
        print("틀렸습니다..")
print("%d개 맞췄습니다!!" %count)
    

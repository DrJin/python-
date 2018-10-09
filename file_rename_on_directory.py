import os
import random

path = r"C:\Users\JinSH\Desktop\승현이글\프로그래밍\python\sample"
files = os.listdir(path)

first = int(files[0].title()[0:-4])
randnum = random.randint(0,1000)
for f in files:
    print(path + "\\" + str.lower(str(randnum + int(f.title()[0:-4]) - first) + f.title()[-4:]))
    os.rename(path + "\\" + f, str.lower(path + "\\" + str(randnum + int(f.title()[0:-4]) - first) + f.title()[-4:]))

import time

def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min

result = gettime()
print("it is %d : %d " %(result[0], result[1]))

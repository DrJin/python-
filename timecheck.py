import time

start = time.time()
for x in range(1,11):
    print(x, ":", x**100)
end = time.time()
print("time : " + str(end-start))

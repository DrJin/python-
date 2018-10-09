import math

N, K = input().split();
N = int(N)
K = int(K)
favor = []
favor = input().split()
for i in range(N):
    favor[i] = int(favor[i]);
fsum = math.fsum
sqrt = math.sqrt
stds = []
while(K!=N):
    pivot = 0
    std=[]
    while(pivot + K <= N):
        sum = fsum(favor[pivot:pivot+K])
        mean = sum/K
        ssum = 0
        for x in favor[pivot:pivot+K]:
            ssum = ssum + (x-mean)**2
    
        var = ssum/K
        std.append(sqrt(var))
        pivot = pivot+1
    stds.append(min(std))
    K = K + 1

print(stds)
print(min(stds))

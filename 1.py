n = int(input())
l = list(map(int, input().split()))
k = int(input())
l1 = []
l1.append(0)
for i in range(1 , k+1):
    l1.append(k + 1)
    for j in range(n):
        if i - l[j] >= 0:
            l1[i] = min(l1[i] , l1[i - l[j]] + 1)
if k < l1[k]:
    print("-1")
else:
    print(l1[k])
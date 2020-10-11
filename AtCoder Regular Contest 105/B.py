n = int(input())
p = input()
l = p.split()
num = [int(s) for s in l]

y = 0
while y < 1:
    X = max(num)
    x = min(num)
    if X == x:
        y+=1
        break
    a = num.index(X)
    num[a] = num[a] - x

print(min(num))
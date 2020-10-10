n = int(input())
p = input()
l = p.split()
m = [int(s) for s in l]

num = []
for i in range(max(m)+2):
    num.append(i)

for i in range(n):
    if m[i] in num:
        a = num.index(m[i])
        num.pop(a)
    print(min(num))
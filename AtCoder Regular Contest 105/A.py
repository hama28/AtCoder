a,b,c,d = map(int,input().split())
l = [a,b,c,d]
ans = 0

for i in range(len(l)):
    if l[i] == sum(l) - l[i]:
        ans+=1

if a+b == c+d:
    ans+=1
elif a+c == b+d:
    ans+=1
elif a+d == b+c:
    ans+=1

if ans >= 1:
    print('Yes')
else:
    print('No')
def division(n):
    ans = 0
    while n % 2 == 0:
        n /= 2
        ans += 1
    return ans

N = int(input())
num = map(int, input().split())
ans = min(map(division, num))
print(ans)
h, w = map(int, input().split())
masume = []
for i in range(h):
    s = input()
    masume.append(s)

count = 0
for i in range(h):
    for j in range(w-1):
        if masume[i][j] == '.' and masume[i][j+1] == '.':
            count+=1
for i in range(h-1):
    for j in range(w):
        if masume[i][j] == '.' and masume[i+1][j] == '.':
            count+=1

print(count)
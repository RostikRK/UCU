x, y = input().split( )
x1 = int(x)
y1 = int(y)
first = bin(x1)[2:]
second = bin(y1)[2:]

answer = 0
for i in range(0, len(first)):
    if(int(first[i]) ^ int(second[i])):
        answer += 1

print(answer)

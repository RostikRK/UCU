q = int(input())
rows = 1
inc = 2
c = 1
ch= ord("A")
while c < q:
    rows += 1
    c += inc
    inc += 1
for i in range(1,rows+1):
    print(' ' * ((rows - i)*2), end="")
    for j in range(i):
        print(chr(ch), end="")
        ch += 1
        if ch - ord("A") > q-1:
            break
        elif j< i -1:
            print(" ", end = "")
    print()
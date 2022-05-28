start_n=int(input())
rows = int(input())
for i in range(rows, 0, -1):
    for j in range(0, i ):
        if j!=(i-1):
           print(start_n+j, end=' ')
        else:
            print(start_n+j, end='')
    print()

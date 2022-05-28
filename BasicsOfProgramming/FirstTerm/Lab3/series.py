n = int(input())
l = []
for i in range(1,(n)*2,2):
    a=str(i)
    b=str(i+1)
    dil="/"
    drib=a+dil+b
    if (((i+1)%4) == 0) and (i+1) != (n)*2:
        v=(drib + ' + ')
        l.append(v)
    elif (((i+1)%4) != 0) and (i+1) != (n)*2:
        v=(drib + ' - ')
        l.append(v)
        
    else:
        v=(drib)
        l.append(v)
print(("").join(l))
    
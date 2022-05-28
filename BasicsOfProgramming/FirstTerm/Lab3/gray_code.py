x = input()
stro1 = list(x)
stro2 = ''
for i in range(0, len(stro1)):
    stro1[i] = int(stro1[i])
    if(stro1[i-1] ==1 and i != 0):
        stro2 += str(int(not stro1[i]))
    else:
        stro2 += str(stro1[i])
print(stro2)
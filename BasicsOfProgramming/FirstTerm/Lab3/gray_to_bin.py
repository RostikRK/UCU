stro2 = input("")
stro1 = ""

stro1 += stro2[0]

for i in range(1, len(stro2)):
		
    if (stro2[i] == '0'):
        stro1 += stro1[i - 1]

		
    else: 
        if((stro1[i - 1]) == '0'):
            stro1 += '1'
        else:
            stro1 += '0'



print(stro1)

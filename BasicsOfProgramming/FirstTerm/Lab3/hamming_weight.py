osnova = 5
stepin = int(input())
number1 = osnova**stepin
hamming_weight = 0
for i in range (int.bit_length(number1)+1):
    if number1 >> i & 1 :
        
        hamming_weight = hamming_weight + 1
    else:
        hamming_weight = hamming_weight + 0
if (hamming_weight % 2) == 0:
   type_hum = "evil"
else:
   type_hum = "odious"
print("Number", number1 ,"is",type_hum,"number. Its hamming weight is",hamming_weight,end=".");
print()

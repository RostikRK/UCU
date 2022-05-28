grades = []
for i in range(5):
    x=int(input())
    if not 0<=x<=100:
        print("None")
        break
    else:
        grades.append(x)
ser_ar = sum(grades)/5
h= int(5)
if ser_ar==0:
    ser_ar=int(ser_ar)
    grade = "F"
if 0<ser_ar<60:
    grade = "F"
if 60<=ser_ar<67:
    grade = "E"
if 67<=ser_ar<75:
    grade = "D"
if 75<=ser_ar<82:
    grade = "C"
if 82<=ser_ar<90:
    grade = "B"
if 90<=ser_ar<=100:
    grade = "A"
if len(grades)==h:
    print("Average grade =",ser_ar,"->",grade)

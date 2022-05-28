from array import *
commands = []
vuvid = []
for i in range(100):
    x=str(input())
    commands.append(x)
    if x==(""):
        break
for j in range(0, len(commands)-1):
    j=commands[j]
    if j==("RS"):
        vuvid.append("True")
    if j==("RR"):
        vuvid.append("False | False")
    if j==("RP"):
        vuvid.append("False")
    if j==("SP"):
        vuvid.append("True")
    if j==("SS"):
        vuvid.append("False | False")
    if j==("SR"):
        vuvid.append("False")
    if j==("PR"):
        vuvid.append("True")
    if j==("PP"):
        vuvid.append("False | False")
    if j==("PS"):
        vuvid.append("False")
for l in range(len(vuvid)):
    l=vuvid[l]
    print(l)
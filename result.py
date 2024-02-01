m1=int (input ("enter marks1:"))
m2=int (input ("enter marks2:"))
m3=int (input ("enter marks3:"))

if m1>28 and m2>28 and m3>28:
    total=m1+m2+m3
    per=total/3
    result="PASS"

    if per>80:
        grede="A"
    elif per>70:
        grede="B"
    elif per>60:
        grede="C"
    else:
        grede="d"
else:
    total=m1+m2+m3
    per="***"
    result="FALL"
    gread= "F"

print("total :",total)
print("percentage:",per)
print("result:",result)
print("grede:",grede)


print("Enter a temperature in either celsius(C) or in fahrenheit(F)")
print("Eg. 25C or 98F")
temp = input()
if (temp[-1]=='C'):
    t1 = float(temp[0:-1])
    Fah = float((9/5)*t1 + 32)
    print("Temperature in fahrenheit is {} F". format(Fah))
elif (temp[-1]=='F'):
    t2 = float(temp[0:-1])
    Cel = float((5/9)*(t2 -32))
    print("Temperature in celsius is {} C". format(Cel))

name = input("please enter user's name:")
print("hello",name)
print("please choose which conversions you would like to perform:")
num1 = input ("enter the value:")
unit1 = input ("which unit do you want to convert from:")
unit2 = input ("which unit do you want it convert to:")
if unit1=="cm" and unit2 == "m":
    ans = float(num1)/100
    print(ans)
if unit1=="g" and unit2 == "kg":
    ans = float(num1)/1000
    print(ans)  
if unit1=="f" and unit2 == "c":
    ans = float(num1)/1.8
    print(ans)  
if unit1=="ml" and unit2 == "l":
    ans = float(num1)/1000
    print(ans)  
score = int(input("enter a score between 0 and 100:"))
if score>=80:
    print(" grade A")
elif score>=70 and score <80:
        print( "grade B")
elif score>=60 and score <70:
        print(" grade C")
elif score>=50 and score <60:
        print(" grade D")
elif score>=20 and score <40:
        print("grade E")
elif score <20:
        print("grade F") 

name = input("enter user's name")
print("NICE TIME DUDE", name)

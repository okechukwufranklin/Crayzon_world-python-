Num1 = int(input("Enter Number:"))
Num2 = int(input("Enter Number:"))
Num3 = int(input("Enter Number:"))

Sum = Num1 + Num2 + Num3 
print("Sum Of All Number Is:",Sum)

Average = Num1 / Num2 / Num3 
print("Average Of All Numbers Is:",Average) 

Product = Num1 * Num2 * Num3
print("product Of All Number Is:",Product)

Sub = Num1 - Num2 - Num3 
print("Subtracation Of All Number Is:",Sub)

if Num1 > Num2:
         if Num1 > Num3:
              print("Largest Number Is:",Num1)

if Num2 > Num1:
        if Num2 > Num3:
                print("Largest Number Is:",Num2)

if Num3 > Num1:
        if Num3 > Num2:
                print("Largest Number Is:",Num3)

if Num1 < Num2: 
        if Num1 < Num3:
                 print("Smallest Number is:",Num1)

if Num2 < Num1:
         if Num2 < Num3:
                  print("Smallest Number is:",Num2)

if Num3 < Num1: 
         if Num3 < Num2:
                 print("Smallest Number is:",Num3)

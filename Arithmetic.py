number = int(input("Enter Number:"))
number2 = int(input("Enter Second Number:"))
number3 = int(input("Enter Third Number:"))

numberproduct = number * number2 * number3
print("Product Of All Number Is:",numberproduct) 

numberavarage = number / number2 / number3
print("Average Of All Number Is:",numberavarage)

numbersum = number + number2 + number3
print("Sum Of All Number Is:",numbersum)

numbersub = number - number2 - number3
print("Subtraction Of All Number Is:",numbersub)

if(number > number2 and number > number3):
 print("Largest Number is :",number)

if(number2 > number and number2 > number3):
 print("Largest Number is :",number2)

if(number3 > number and number3 > number2):
 print("Largest Number is :",number3)

if(number < number2 and number < number3):
 print("Smallest Number is :",number)

if(number2 < number and number2 < number3):
 print("Smallest Number is :",number2)

if(number3 < number and number3 < number2):
 print("Smallest Number is :",number3)
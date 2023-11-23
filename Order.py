number = int(input("Enter Number:"))
number2 = int(input("Enter Second Number:"))
number3 = int(input("Enter Third Number:"))

if(number < number2 and number < number3):
 if(number2 < number3):
   print(number,number2,number3)


if(number < number2 and number < number3):
 if(number3 < number2):
  print(number,number3,number2)


if(number2 < number and number2 < number3):
 if (number < number3):
  print(number2,number,number3)

if(number2 < number and number2 < number3):
 if (number3 < number2):
  print(number2,number3,number)


if(number3 < number and number3 < number2):
 if(number < number2):
  print(number3,number,number2)


if(number3 < number and number3 < number2):
 if(number2 < number):
  print(number3,number2,number)



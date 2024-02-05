number = input("Enter number:")
number2 = input("Enter second number:")
if type(number) and type(number2) == float:
	print(2)
if type(number) == float and type(number2) != float:
	print(1)
if type(number2) == float and (number) != float:
	print(1)
if type(number) and type(number2) != float:
	print(0)
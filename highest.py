def highest(number,number2,number3):
	

	if number > number2 and number >number3:
		return number

	if number2> number and number2 >number3:
		return number2
	
	if number3 > number and number3 >number2:
		return number3

print(highest(5,20,10))	
def square_root( number):
	square = number ** 0.5
	if number % 5 == 0:
		print("divisble by 5")
	if (number % 5 != 0):
		print("Not divisble by 5")
	
	return square

print(square_root(10))
	
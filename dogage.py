age = int(input("Enter age in human age :"))

if age <= 2:
 dogage = age * 10.5

if age > 2:
 dogage = 2 * 0.5 + ((age - 2)*4)
print(" age in dogyears is :",dogage)
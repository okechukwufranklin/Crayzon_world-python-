productType = input("Enter Type of Product Electronic or clothing or other :")
productName = input("Enter product name:")
price = int(input("enter price:"))

if productType.lower() == "electronic":
	result = price - ( price * 10/100)
	print("Price with discount of 10% for:",productName,"is :",result,'$')

elif productType.lower() == "clothing":
	result = price - (price * 5/100)
	print("Price with discount of 5% for:",productName,"is",result,'$')

if productType.lower() == "other":
	print("Price does not have discount for:",productName,"price is :",price,'$')


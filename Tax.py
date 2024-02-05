price = float(input("Enter price of Car"))

if price < 1000000:
 price = (price * 0.10)
 print(price)


if price > 1000000 and price < 3000000:
  price = (price * 0.15)
  print(price)


if price > 3000000 and price < 5000000:
   price = (price * 0.20)
   print(price)


if price > 5000000:
  price = (price * 0.25)
  print(price)
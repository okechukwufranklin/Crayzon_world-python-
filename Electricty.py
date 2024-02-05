number = int(input(' Enter Number Of unit '))

if number <= 100:
 print('No Charge')

if number > 100 and number <= 200:
 answer1 = (number - 100)* 10
 print("Charge is",answer1)

if number >= 200:
  answer3 = (number - 200)* 20 + (100 *10)
  print('Charge is',answer3) 
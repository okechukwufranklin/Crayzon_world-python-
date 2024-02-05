score = int(input('enter score'))
total = 0
count = 0
while score != 0:
       total += score        
       count += 1      
       score = int(input('enter scores:'))
        
average = total / count 
sum = total + count
print("the average is",average)
print("the sum is",sum)
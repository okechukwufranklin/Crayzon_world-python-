score = float(input('enter score'))
total = 0
count = 0
while score != 0:
       total += score        
       count += 1      
       score = float(input('enter scores:'))
        
average = total / count 
print("the average score is",average)
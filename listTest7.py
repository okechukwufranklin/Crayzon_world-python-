string = input('Enter size of list:')

lst = list(map(int,input('Enter the numbers and elements:').strip().split()))[:int]

print('the list is:',lst)
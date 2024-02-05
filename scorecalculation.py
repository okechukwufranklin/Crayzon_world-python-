Score = int(input('enter score or -1 to end:'))
passs = 0
fail = 0
while Score != -1:
	if Score >= 45:
		passs += 1
	if Score < 45:
		fail += 1
	Score = int(input('enter score or -1 to end:'))
print('total amount of pass is:',passs)
print('total amount of fail is:',fail)
print('Leave my school please:',leave)
def maximum(Value1, Value2,Value3):
	max_Value = Value1
	if Value2 > max_Value:
		max_Value = Value2
	if Value3 > max_Value:
		max_Value = Value3
	return max_Value

maximum(12,27,36)
print(maximum(12,27,36))

print(maximum(12.3,46.6,9.7))


print(maximum('yellow','red','orange'))

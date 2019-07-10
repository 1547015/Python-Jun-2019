def is_even(num):
	if(num %2 == 0):
		even.append(num)
		print("even")
	else:
		odd.append(num)
		print("odd")

print("hello")		
even = []
odd = []
x = [1,2,13,24,45,90]
for i in x:
	a = is_even(i)
print("even numbers are:",even)
print("odd numbers are:",odd)

# x = [1,2,13,24,45,90]
# for i in x:
# 	a = is_even(i)
# print("even numbers are:",even)
# print("odd numbers are:",odd)
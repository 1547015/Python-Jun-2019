
# ----------------------function without parameter with no return value-------------------------
import time
def pause_for_minute():
	time.sleep(1)
	print("pausing for 1 sec ")
x = [1,2,13,24,45,90]
for each in x:
	pause_for_minute()
	print(each)
# print(odd)


# ----------------------function with parameter no return values-------------------------
# even = []
# odd = []
# def iseven(num):
# 	if(num %2 == 0):
# 		even.append(num)
# 	else:
# 		odd.append(num)
# x = [1,2,13,24,45,90]
# for each in x:
# 	a = iseven(each)
# print("even numbers are",even)
# print(odd)
# ----------------------function with parameter one return value-------------------------
# def iseven(num):
# 	if(num %2 == 0):
# 		return True
# 	else:
# 		return False
# x = [1,2,13,24,45,90]
# for each in x:
# 	a = iseven(each)
# 	if(a):
# 		print(each ,"is even")
# 	else:
# 		print(each ,"is odd")
# ----------------------function with parameter and multiple return values-------------------------
# --method to write squre and cube of number

# def square_cube(num):
# 	return num*num,num*num*num
# x = [1,2,13,24,45,90]
# for each in x:
# 	a,b = square_cube(each)
# 	print("even numbers are",a,b)
	

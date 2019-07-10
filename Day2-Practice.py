i =int(input("entertain value:"))
ip = open("demo.txt","r")
print(ip.read())
x = ['a','e','i','o','u']

# if(i >= 10):
# 	print("i is positive number:",i)
# 	print("I am inside if condition")
# else:
# 	print("i is negative number")
# 	print("I am inside else condition")
# print("I am not in If and else")

l1 = [1,2,3]
l2 = [5,7,9]
l1.append(l2)
print(l1) #[1,2,3,[5,7,9]]
l1.extend(l2)
print(l1) #[1,2,3,[5,7,9],5,7,9]

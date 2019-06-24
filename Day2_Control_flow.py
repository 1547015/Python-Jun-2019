# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

---------------------------------------------------------------------------
# Program checks if the number is positive or negative
# And displays an appropriate message

num = 3

# Try these two variations as well. 
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:	   
	print("Negative number")	
------------------------------------------------------------------------------
# In this program, we input a number
# check if the number is positive or
# negative or zero and display
# an appropriate message
# This time we use nested if
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
---------------------------------------------------------------------------------
# python program to illustrate nested If statement 
#!/usr/bin/python 
i = 10
if (i == 10): 
    #  First if statement 
    if (i < 15): 
        print ("i is smaller than 15") 
    # Nested - if statement 
    # Will only be executed if statement above 
    # it is true 
    if (i < 12): 
        print ("i is smaller than 12 too") 
    else: 
        print ("i is greater than 15") 
----------------------------------------------------------------------------
# Python program to illustrate if-elif-else ladder 
#!/usr/bin/python 
   
i = 20
if (i == 10): 
    print ("i is 10") 
elif (i == 15): 
    print ("i is 15") 
elif (i == 20): 
    print ("i is 20") 
else: 
    print ("i is not present") 
----------------------------------------------------------------------------
answer = input("Is Python an interpreted language? Yes or No >> ").lower()

if answer == "yes" :
    print("You have cleared the test.")
else :
    print("You have failed the test.")

print("Thanks!")
------------------------------------------------------------------------------
x = 10
y = 20
z = 30

print("Start")
if x == 10:
    print(" Nested If")
    if y == 20:
        print(" End of Nested If Block ")
    else:
        print(" End of Nested If-Else Block ")
elif y == 20:
    print(" Elif block ")
else:
    print(" Nested If")
    if z == 30:
        print(" End of Nested If Block ")
    else:
        print(" End of Nested If-Else Block ")
print("Stop")
---------------------------------------------------------------------------------
a = 10
b = 20
c = 30

avg = (a + b + c) / 3
print("avg =", avg)

if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" %(avg, a, b, c))
elif avg > a and avg > b:
    print("%d is higher than %d, %d" %(avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" %(avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" %(avg, b, c))
elif avg > a:
    print("%d is just higher than %d" %(avg, a))
elif avg > b:
    print("%d is just higher than %d" %(avg, b))
elif avg > c:
    print("%d is just higher than %d" %(avg, c))
-----------------------------------------------------------------------------------

coursework = "English"
score_theory = 53
score_practical = 35

if(coursework == "Science" or coursework == "science"):
    if(score_theory > 50):
        print("Please check the input score for 'Science: Theory'.")
    elif(score_practical > 50):
            print("Please check the input score for 'Science: Practical'.")  
    else:
        print("Score validated for Science. Your total is: ",score_theory + score_practical)             
elif(coursework == "English" or coursework == "english"):
    if(score_theory > 60):
        print("Please check the input score for 'English: Theory'.")
    elif(score_practical > 40):
            print("Please check the input score for 'English: Practical'.")  
    else:
        print("Score validated for English. Your total is: ",score_theory + score_practical)
else: print("Coursework not recognised. Please enter score for either Science or English.")
----------------------------------------------------------------------------------------
coursework = "English"
score_theory = 53
score_practical = 78

if(coursework == "Science" or coursework == "science"):
    if(score_theory > 50 or score_practical > 50):
        # Can't distinguish the error in Science: theory or Science: Practical
        print("Please check the input score for Science.")
    else: print("Score validated for Science. Your total is: ",score_theory + score_practical)             
elif(coursework == "English" or coursework == "english"):
    if(score_theory > 60 or score_practical > 40):
        # Can't distinguish the error in English: theory or English: Practical
        print("Please check the input score for English.")
    else: print("Score validated for English. Your total is: ",score_theory + score_practical)
else: print("Coursework not recognised. Please enter score for either Science or English.")
---------------------------------------------------------------------------------------	
	
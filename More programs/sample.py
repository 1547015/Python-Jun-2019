# Program to show various ways to read and 
# write data in a file. 
file1 = open("myfile.txt","w") 
L = ["This is Java \n","This is Paris \n","This is London \n"]  
  
# \n is placed to indicate EOL (End of Line) 
file1.write("Hello \n") 
file1.writelines(L) 
file1.close() #to change file access modes 
  
file1 = open("myfile.txt","r+")  
  
print ("Output of Read function is ")
print (file1.read()) 

  
# seek(n) takes the file handle to the nth 
# bite from the beginning. 
 
print ("Output of Readline function is ")
print (file1.readline()) 
  
 
# To show difference between read and readline 
print ("Output of Read(9) function is ")
print (file1.read(9)) 
 
print ("Output of Readline(9) function is ")
print (file1.readline(9)) 
# readlines function 
print ("Output of Readlines function is ")
print (file1.readlines()) 
file1.close() 
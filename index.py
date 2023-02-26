#indexing and slising in python
# Mystring = "hello world" # so if you want to print hello world you can go like this
# print (Mystring) 

# If you need a single character form a string mark an index inside the string to get a specific character
# The first letter starts with [0]
# Mystring = "hello world" 
# print (Mystring[1]) 

# Now lets check on slicing in python
# Will redefine the string 
mystring = "abckefghijk"
# print (mystring)# comment this to get the slice out put
# Inorder to slice string what you need to do is
print (mystring[3:])
print (mystring[:4])# comment the upper print statement to check how this works
print (mystring[::])# this will print the whole string 
print (mystring[::2])# the string will walk in step size of two "acegik"
print (mystring[2:7:2])#start,stop, and step"ceg"
print (mystring[::-1]) #Will actully reverse the string






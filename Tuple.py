tuple1 = (1,2,3,4,5) #Tuples store data, where the data types are sapeated by commas and enclosed in paranthesis
print(type(tuple1)) #tuples are similar to lists 
tuple2 = (2,) #If comma is not present, the program understands it as an integer.
print(type(tuple2))
#tuple1.append(3) Not possible as tuples cannot be changed once it is defined. Tuples are also mutable
tuple3 = (tuple1,tuple2)
print (tuple3)
print(tuple3[0]) 
#Advantages:
  #tuples can remain fixed throught the program
  #Tuples are faster
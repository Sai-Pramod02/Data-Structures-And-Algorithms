list1 = [1,2,5,9,11] #Lists are ordered and can store data i.e numbers saperated by commas and enclosed in square brackets
list2 = [2,"Hello",2.34,'h'] #A list can store any data type and also store multiple data types
print(list1)
print(list2)
list1.append(3) #Lists are mutable 
print(list1)
del list1[0]
print(list1)
list3 = [(list1),(list2)] #Lists can be nested
list4 = [] #Lists can be empty
#Lists are dynamic
list5 = [2,"Hello",'h',2.34]
print(list1==list5) #Lists are ordered


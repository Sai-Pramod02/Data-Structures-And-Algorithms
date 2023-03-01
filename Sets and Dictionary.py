d = {"Riya" : "riyapramodh@gmail.com", "Pramod" : "saipramod@gmail.com"} #Saperated by key-value pairs and enclosed in curly braces where the key is not mutable and the value is mutable
print(d)
d1 = {} #Empty dictionary
print(d1)
d2 = {"1":"j", "2":"k"}
print(d2)
d3 = {"2":"k","1":"j"}
print(d2==d3) #Dictionary is unordered
print(d["Riya"]) #Elements in dictionary can be accessed through keys
del d2["1"]
print(d2)

#Sets consists of unique elements in it which are surrounded by curly braces.
s = set() #Empty set
s1 = {1,2,2,3,4,3,5,7,4,5,6}
print(s1) #Only prints unique characters
s1.add(9) #Sets are mutable
print(s1)
print(1 in s1) #Returns if that particular element in present in the set
# s2 = {[1,2,3], 5}  A set cannot contain mutable emelents in it
# print(s2)
s3 = {1, "Hello", 5 , 9} #A set can contain multiple data types 
print(s3) #Sets are also unordered

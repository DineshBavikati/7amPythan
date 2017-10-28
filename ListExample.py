#!/usr/bin/python
# LIST Data TypeError
# List is mutable data type i.e we can alter the values
# List representation is brackets [] 
# It holds the heterogeneous elements i.e Strings, Numbers & Special Characters we can store
# Each elements separated with  ","
# Elements can access with Index values 
# Left to Right 01234..nth - index
# Right to Left -nth ...... -3, -2, -1.

#numbers in list
list1 = [3,5,8,9,0,2,1,5]
#Strings in list
list2 = ["Dinesh", 'kiran', "chandu", " ", '''ramu''',"""jayakumar""",]
#Numbers and Strings
list3 = ["ramesh", 10, 'raju', 98, "Atp"]
#Numbers, Strings and Special Characters
list4 = [11, "dinesh", '@', '//', ' ', 1.9]

#type is a fuction 1. which class it belongs to
                 # 2. to findout Object

print(list1, type(list1), id(list1))
print(" ")
print(list2, type(list2), id(list2))
print(" ")
print(list3, type(list3), id(list3))
print(" ")
print(list4, type(list4), id(list4))
print(" ")

print(len(list1))
print(" ")
print (list3)
print(list3[-1])
print(list3[4])
print(" ")

list3[2] = 100000
print(list3,id(list3))
print(list3, len(list3))

#delete is a keyword
del list3[2]
print(list3,id(list3), len(list3))

del list3
#after deleting list3 list printing the list it is giving the error
#print(list3, len(list3))
#NameError: name 'list3' is not defined










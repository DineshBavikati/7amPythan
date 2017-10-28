#!/usr/bin/python
# DICTIONARY Data Type
# Mutable data types
# All elements are key and value pair.
# representation of elements in braces {}
# elements are separated with ,
# ":" colon separates the key and value 
# Dictionary with no key value is called empty Dictionary a={}

dict1 = { "Dinesh" : "Bavikati", 
          "jaya"   : "kumar",
	    "one" : "1",
		    2 : 'two'
            }
print(dict1, type(dict1), id(dict1)) #id = 45076528
print(" ")
print(dict1["jaya"])
print(" ")
print(dict1[2])
print("")

dict1["one"]="Number in the one"

print(dict1, type(dict1), id(dict1)) #id = 45076528





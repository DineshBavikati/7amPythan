#!/usr/bin/python
# TUPLE Data Type
# Tuple is a Immutable data type
# it holds the different type of daya
# Representation of tuple with parenthesis() or with out parenthesis
# Elements are Separated with "," 
# Adding New Value is not Possible here


#only numbers and with out parenthesis 
tup1 = 7, 9, 2, 6, 10, 3, 8
#String values
tup2 = "dinesh", "ramesh", "army", "jayakumar", "lavakusa"
#Strings and Value
tup3 = "superman", 1900, "spiderman", 1997, "batman", 2013, '//'
tup4 = ( )
tup5 = ('$', '@', 877, """dinesh""")


print(tup1, type(tup1), id(tup1))
print(" ")
print(tup2, type(tup2), id(tup2))
print(" ")
print(tup3, type(tup3), id(tup3))
print(" ")
print(tup4, type(tup4), id(tup4))
print(" ")
print(tup5, type(tup5), id(tup5))

print(" ")
print(tup1[1])

#tup1[1]=100
#TypeError: 'tuple' object does not support item assignment
#del tup1[1]
#TypeError: 'tuple' object doesn't support item deletion
print(" ")

print(tup1, type(tup1), id(tup1))



#Tuple : ordered, immutable and allows duplicate elements. It cannot be changed after its creation
# It is created with a parentheseis and within the parenthesis and each element seperated by a comma
#?The parenthesis are optional and can be left out. You have to put a comma at the end of a element in a tuple or it will be recognized as type:string
myttuple1 = ("max",)
mytuple = ("Max", 28, "Manhattan")
print(mytuple)

#You can also use the inbuilt tuple function to create a tuple function for example from a lit
mytuple2 = tuple(["Max", 90, "Colorado"])
print(mytuple2)

#? Getting an item that we want from a tuple we use the index

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
#Allow Duplicates-Since tuples are indexed, they can have items with the same value:

#Tuple Methods
#Python has two built-in methods that you can use on tuples.

#? 2. count()	Returns the number of times a specified value occurs in a tuple

mytuple = (1,3,5,3,3,8,3,9,5,4,3,6,4,8,9)
mytuple_count = mytuple.count(5)
print(mytuple_count)

#? index()	Searches the tuple for a specified value and returns the position of where it was found


mytuple = (1,2,6,8,9,3,67)
x = mytuple.index(9)
print(x)


















































































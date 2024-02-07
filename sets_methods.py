
#* 1. Add ? add()	Adds an element to the set

myset = {"JBL", "Pixel", "Samsung"}
myset.add("Lenovo")
print(myset)   #? {'Lenovo', 'JBL', 'Samsung', 'Pixel'}


#* 2. clear()	Removes all the elements from the set
plants = {"Snake Plant", "Cactus", "Monstera"}
plants.clear()
print(plants) #?set()


#* 3. copy()	Returns a copy of the set
plants = {"Snake Plant", "Cactus", "Monstera"}
plants.copy()
print(plants) #?{'Cactus', 'Snake Plant', 'Monstera'}



#* 4. difference()	Returns a set containing the difference between two or more sets

plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab"}
myset = {"JBL", "Pixel", "Samsung", "Cactus"}
set_difference = plants.difference(myset) 
print(set_difference) #? {'Monstera', 'Baobab', 'Snake Plant', 'Lilly'}

#*5. difference_update()	Removes the items in this set that are also included in another, specified set
plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab"}
myset = {"JBL", "Pixel", "Samsung", "Cactus"}
plants.difference_update(myset)
print(plants) # {'Lilly', 'Baobab', 'Monstera', 'Snake Plant'}#Remove the items that exist in both sets:

#* 6.discard()	Remove the specified item
plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab"}
plants.discard("Snake Plant")
print(plants) #{'Cactus', 'Monstera', 'Lilly', 'Baobab'}

#* 7. intersection()	Returns a set, that is the intersection of two other sets

plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab"}
myset = {"JBL", "Pixel", "Samsung", "Cactus", "Monstera"}
intersection_items = plants.intersection(myset)
print(intersection_items) #{'Monstera', 'Cactus'}


#*8. intersection_update()	Removes the items in this set that are not present in other, specified set(s)
plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab"}
myset = {"JBL", "Pixel", "Samsung", "Cactus", "Monstera"}
plants.intersection(myset)# 
print(plants) #plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab"} #{'Cactus', 'Snake Plant', 'Baobab', 'Lilly', 'Monstera'}  
#Remove the items that is not present in both plants and myset:


#*9. isdisjoint()	Returns whether two sets have a intersection or not
plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab"}
myset = {"JBL", "Pixel", "Samsung", "Cactus", "Monstera"}
#Return True if no items in set plants is present in set myset:
joint_set = plants.isdisjoint(myset)
print(joint_set) #False

#*10. issubset()	Returns whether another set contains this set or not
plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab"}
myset = {"JBL", "Pixel", "Samsung", "Cactus", "Monstera"}
plants_subset = plants.issubset(myset)
#Return True if all items in set x are present in set y:
print(plants_subset) #False

#* 11. issuperset()	Returns whether this set contains another set or not
plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab"}
myset = {"JBL", "Pixel", "Samsung", "Cactus", "Monstera"}
#Return True if all items set plants are present in set myset:
superset_plants = plants.issuperset(myset)
print(superset_plants) #False

#* 12.pop()	Removes an element from the set
plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab"}
plants.pop()
#Remove a random item from the set:
print(plants) #{'Cactus', 'Monstera', 'Lilly', 'Baobab'}


#* 13. remove()	Removes the specified element
plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab"}
plants.remove("Snake Plant")
print(plants) #{'Lilly', 'Baobab', 'Cactus', 'Monstera'}

#*14. symmetric_difference()	Returns a set with the symmetric differences of two sets
plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab"}
myset = {"JBL", "Pixel", "Samsung", "Cactus", "Monstera"}
assymetric_plant = plants.symmetric_difference(myset)
#Return a set that contains all items from both sets, except items that are present in both sets:
print(assymetric_plant)
#{'JBL', 'Samsung', 'Baobab', 'Lilly', 'Snake Plant', 'Pixel'}


#*15. symmetric_difference_update()	inserts the symmetric differences from this set and another

plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab"}
myset = {"JBL", "Pixel", "Samsung", "Cactus", "Monstera"}
plants.symmetric_difference_update(myset)
#Remove the items that are present in both sets, AND insert the items that is not present in both sets:
print(plants) #{'Snake Plant', 'Baobab', 'JBL', 'Samsung', 'Pixel', 'Lilly'}


#* 16. union()	Return a set containing the union of sets
plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab", "Rosa"}
myset = {"JBL", "Pixel", "Samsung", "Cactus", "Monstera"}
#Return a set that contains all items from both sets, duplicates are excluded:
without_duplicate = plants.union(myset)
print(without_duplicate) #{'Monstera', 'Rosa', 'JBL', 'Lilly', 'Baobab', 'Samsung', 'Pixel', 'Snake Plant', 'Cactus'}

#* 17. update()	Update the set with the union of this set and others
plants = {"Snake Plant", "Cactus", "Monstera","Lilly", "Baobab", "Rosa"}
myset = {"JBL", "Pixel", "Samsung", "Cactus", "Monstera"}
#Insert the items from set plants into set myset:
plants.update(myset)
print(plants) #{'JBL', 'Lilly', 'Rosa', 'Pixel', 'Baobab', 'Cactus', 'Monstera', 'Snake Plant', 'Samsung'}







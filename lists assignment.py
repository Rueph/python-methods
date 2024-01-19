# append() The append() method appends an element to the end of the list.

veggies = ["Broccoli", "Cauliflower", "Green Kale"]
veggies.append("red cabbage")
print(veggies) # ["Broccoli", "Cauliflower", "Green Kale", "Red Cabage"]

# List clear() The clear() method removes all the elements from a list.

cities = ["Nairobi", "Nakuru", "Manhattan"]
cities.clear()
print(cities)  #[]


#List copy() The copy() method returns a copy of the specified list.


gifts = ["Perfume", "Shoes", "Dress","watch", "necklace"]
x = gifts.copy()
print(x) #["Perfume", "Shoes", "Dress","watch", "necklace"]

# List count()  The count() method returns the number of elements with the specified value.

names = ["Maurice","Mourao", "Maurice"]
num = names.count("Maurice")
print(num) #2

# List extend() The extend() method adds the specified list elements (or any iterable) to the end of the current list.

art = ["Impressionism", "Romanticism", "Bauhaus"]
extra = ["Visual arts", "Rennaissance", "Gothic"]
art.extend(extra)
print(art) 
#? Expected output
['Impressionism', 'Romanticism', 'Bauhaus', 'Visual arts', 'Rennaissance', 'Gothic']

# List index()  The index() method returns the position at the first occurrence of the specified value.

fruit = ["Blaubere", "Edbeeren", "Himbere"]
himbere_index = fruit.index("Edbeeren")
print(himbere_index) #1

#insert()	Adds an element at the specified position

german_cultlery = ["TischGabel", "Forke","Stimmgabel"]

german_cultlery.insert(2, "Nebenfluss")
print(german_cultlery)
#expected output will be ["TischGabel", "Forke","Nebenfluss", "Stimmgabel"]

#pop()	Removes the element at the specified position

german_cultlery = ["TischGabel", "Forke","Stimmgabel"]
german_cultlery.pop(2)
print(german_cultlery) #["TischGabel", "Forke"]

#remove()	Removes the item with the specified value

german_cultlery1 = ["TischGabel", "Forke", "Stimmgabel"]
german_cultlery1.remove("Forke")
print(german_cultlery1) #["TischGabel", "Stimmgabel"]


#reverse()	Reverses the order of the list

german_cultlery1 = ["TischGabel", "Forke","Stimmgabel"]
german_cultlery1.reverse()
print(german_cultlery1) #['Stimmgabel', 'Forke', 'TischGabel'] 

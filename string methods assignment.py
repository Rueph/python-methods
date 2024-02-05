"""
#todo 
go to w3schools using  https://www.w3schools.com/python/python_ref_string.asp and attempt every  string method

*steps
1. Click on the method
2. Read about the method and its parameters
3. Do it yourself button on w3schools
4. Do it my own way in this document
"""
#? 1. capitalize:  	Converts the first character to upper case

r = "we like food"
p = r.capitalize()
print(p) #We like food


#? 2. casefold Converts string into lower case

a = "WE LIKE THE WHOLE WORLD TO BE PINK"
casefold1 = a.casefold()
print(casefold1) #we like the whole world to be pink


#? 3. center Returns a centered string(Alignment)

b = "The center method will center align the string, using a specified character space is default as the fill character."
c = b.center(500)
print(c)


#? 4. count 	Returns the number of times a specified value occurs in a string

d = "Beetroot or the red cabbage"
e = d.count("o")
print(e) #3

#? 5. encode Returns an encoded version of the string

f = "The code word is La Riviera"
g = f.encode()
print(g) #b'The code word is La Riviera'


#? 6. endswith Returns true if the string ends with the specified value

h = "The value should be false"
i = h.endswith("true")
print(i) #False


#? 7. expandtabs 	Sets the tab size of the string

j = "P\tf\tl\ta\tn\tz\te"
k = j.expandtabs(10)
print(k) #P         f         l         a         n         z         e


#? 8. find- Searches the string for a specified value and returns the position of where it was found

l =  "Hello party people!"
m = l.find("l")
print(m) #2

#? 9. format -Formats specified values in a string
txt = "This is captain {fname} speaking, I'm {age}"
print(txt.format(fname = "Kim", age = 56)) #This is captain Kim speaking, I'm 56


#? 10. format_map() 	Formats specified values in a string

# txt1 = "This is captain {fname} speaking, I'm {age}"
# print(txt1.format_map(captain))

#to be redone


#? 11. index - Searches the string for a specified value and returns the position of where it was found

txt3 = "Welcome aboard Venga Airways."
txt4 = txt3.index("Venga")
print(txt4) #15

#? 12. isalnum() when all characters are alphanumeric returns true

txt5 = "After take off we'll pump up the sound system6."
txt6 = txt5.isalnum()
print(txt6) #False

#? 13. isalpha() returns tue if all the charactes are in the aphabet

txt5 = "After"
txt6 = txt5.isalpha()
print(txt6) #True


#? 14. isascii() returns true if all characters in the string are ascii characters

txt5 = "venga134"
txt6 = txt5.isascii()
print(txt6) #True

#? 15. isdecimal() 	Returns True if all characters in the string are decimals

txt5 = "586.8"
txt6 = txt5.isdecimal()
print(txt6) #False


#? 16. isdigit() Returns True if all characters in the string are digits

m = "8972"
j = m.isdigit()
print(j) #True


#? 17. isidentifier() Returns True if the string is an identifier

k = "I_7"
l = k.isidentifier()
print(l) #True


#? 18. islower()	Returns True if all characters in the string are lower case


k = "this is my first card"
j = k.islower()
print(j) #True


#? 19. isnumeric()Returns True if all characters in the string are numeric


o = "vengaboys4"
p = o.isnumeric()
print(p) #False


#? 20. isprintable()Returns True if all characters in the string are printable

q = "?n\n65"
r = q.isprintable()
print(r) #False


#? 21. isspace()Returns True if all characters in the string are whitespaces

s = " "
t = s.isspace()
print(t) #True


#? 22. istitle() Returns True if the string follows the rules of a title


u = "gonna pack my bags and leave this town"
v = u.istitle()
print(v) #False


#? 23. isupper() 
#? 23. isupper() 	Returns True if all characters in the string are upper case

w = "THE WHOLE MEDIA SUCKS"
x = w.isupper()
print(x) #True


#? 24. join() 	Joins the elements of an iterable to the end of the string


colors = ("blau", "schwarze", "weiß", "lilla")
joined_colors = "-".join(colors)
print(joined_colors) #blau-schwarze-weiss-lilla


#? 25. ljust() left justified version of the link


text8 = "anonymous calls to stop, Grab a flight and Fly away on Venga Airways"
text9 = text8.ljust(25)
print("I recieved", text9) #I recieved anonymous calls to stop, Grab a flight and Fly away on Venga Airways 


#? 26. lower()	Converts a string into lower case


my_case ="FLY ME HIGH IBIZA SKY"
lower_case = my_case.lower()
print(lower_case) #fly me high ibiza sky


#? 27. lstrip() Returns a left trim version of the string

full = "      I look up at the sky      "
cut = full.lstrip()
print("And I see the clouds",cut, "I looked down at the ground")
#And I see the clouds I look up at the sky       I looked down at the ground


#? 28. maketrans()   	Returns a translation table to be used in translations


text = "And I see the rainbow down the drain"
t = "d"
e = "e"
mytable = str.maketrans(t,e)
print(text.translate(mytable))
#Ane I see the rainbow eown the erain


#? 29. partition()   Returns a tuple where the string is parted into three parts


txt10 = "We're going to Ibiza Back to the island"
txt11 = txt10.partition("Ibiza")
print(txt11)
#("We're going to ", 'Ibiza', ' Back to the island')



#? 30. replace()   Returns a string where a specified value is replaced with a specified value


txt12 = "We're gonna have a party"
txt13 = txt12.replace("gonna", "going to")
print(txt13)
#We're going to have a party


#? 31. rfind()  Searches the string for a specified value and returns the last position of where it was found


txt14 = "In the sea Mediterranean Sea"
txt15 = txt14.rfind("sea")
print(txt15) #7



#? 32. rindex() 	Searches the string for a specified value and returns the last position of where it was found


txt16 = "In the castle on the Mediterranean Sea castle"
txt17 = txt16.rindex("castle")
print(txt17) #39


#? 33. rjust() Returns a right justified version of the string

txt18 = "Far away from this big town"
txt19 = txt18.rjust(30)
print(txt19, "is Vengatown") # Far away from this big town is Vengatown



#? 34. rpartition() Returns a tuple where the string is parted into three parts


txt16 = "In the castle on the Mediterranean Sea castle"
txt17 = txt16.partition("castle")
print(txt17)
#("We're going to ", 'Ibiza', ' Back to the island')


#? 35. rsplit() 	Splits the string at the specified separator, and returns a list


txt20 = "In the castle on the Mediterranean Sea castle"
txt21 = txt20.rsplit("castle")
print(txt21) #('In the ', 'castle', ' on the Mediterranean Sea castle')


#? 36. rstrip() 	Returns a trimmed version of the string


txt20 = "    We are now approaching    Ibiza   airport      "
txt21 = txt20.rstrip()
print("Vengaboys on call",txt21, "be guided") ('In the ', 'castle', ' on the Mediterranean Sea castle') #Vengaboys on call     We are now approaching    Ibiza   airport be guided



#? 37. split()  	Splits the string at the specified separator, and returns a list

txt20 = "As you can see the sky is blue And the beach is waiting for you"
txt21 = txt20.split()
print(txt21) #['As', 'you', 'can', 'see', 'the', 'sky', 'is', 'blue', 'And', 'the', 'beach', 'is', 'waiting', 'for', 'you']


#? 38. splitlines() 	Splits the string at line breaks and returns a list


txt20 = "In the castle\n on the Mediterranean Sea castle"
txt21 = txt20.splitlines()
print(txt21) #['In the castle', ' on the Mediterranean Sea castle']



#? 39. startswith() 	Returns true if the string starts with the specified value


txt14 = "In the sea Mediterranean Sea"
txt15 = txt14.startswith("In")
print(txt15) #True


#? 40. strip() Returns a trimmed version of the string


txt14 = "     Thank you for flying Venga Airways     "
txt15 = txt14.strip()
print("We're gonna have a party", txt15,"We are now approaching Ibiza airport") #We're gonna have a party Thank you for flying Venga Airways We are now approaching Ibiza airport



#? 41.  swapcase() 	Swaps cases, lower case becomes upper case and vice versa


txt14 = "     Thank you for flying Venga Airways     "
txt15 = txt14.swapcase()
print(txt15)#tHANK YOU FOR FLYING vENGA aIRWAYS 


#? 42. title() Converts the first character of each word to upper case


txt14 = "     Thank you for flying Venga Airways     "
txt15 = txt14.title()
print(txt15) #Thank You For Flying Venga Airways   


#? 43. translate() Returns a translated string

#use a dictionary with ascii codes to replace letters


#mytable2 = {83, 80}
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
txt15 = "We're sorry gonna have a party"
print(txt15.translate(mydict)) #We're srry o ove o pory


#? 44. upper() Converts a string into upper case


txt14 = "And the beach is waiting for you"
txt15 = txt14.upper()
print(txt15)
#AND THE BEACH IS WAITING FOR YOU


#? 45. zfill() Fills the string with a specified number of 0 values at the beginning


filler = "60"
x = filler.zfill(20)
print(x)
#00000000000000000060





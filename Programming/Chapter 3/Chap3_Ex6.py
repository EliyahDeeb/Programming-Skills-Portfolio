#Exercise 6: Shrinking Guest List

#This is a continuation of Exercise 5.
_1=['Ryan Reynolds','Jeff Bezos','Arnold Schwarzenegger','Kevin Hart']

a=_1[0].title() 
print(f"{_1[0]}, I am inviting you to dinner.")
print(f"{_1[1]}, I am inviting you to dinner.")
print(f"{_1[2]}, I am inviting you to dinner.")

print("\nSorry, "+f"{_1[2]}","can't make it due to important reasons.\n")

print(f"{_1[0]}, I am inviting you to dinner.")
print(f"{_1[1]}, I am inviting you to dinner.")
print(f"{_1[3]}, I am inviting you to dinner.")

#Since there are only 2 spaces available for 2 guests. 
#So, 2 people must be removed using he command below:

Rname2=_1.pop(2)
Rname3=_1.pop(1)
print("I'm sorry",Rname2+",","but there are only 2 seats available so I cannot invite you.")
print("I'm sorry",Rname3+",","but there are only 2 seats available so I cannot invite you.")

print(_1[0],"and",_1[1]+",","you both are still invited to dinner at my place.")

print("Current Names: ",_1)

#The list should be empty at the end using the 'del' command.

del _1[1] 
del _1[0]

print("New Names: ",_1)
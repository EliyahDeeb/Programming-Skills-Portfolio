
#Exercise 5: Change Guest List
#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

_1=['Ryan Reynolds','Jeff Bezos','Arnold Schwarzenegger','Kevin Hart']

a=_1[0].title() 
print(f"{_1[0]}, I am inviting you to dinner.")
print(f"{_1[1]}, I am inviting you to dinner.")
print(f"{_1[2]}, I am inviting you to dinner.")

print("\nSorry, "+f"{_1[2]}","can't make it due to important reasons.\n")

print(f"{_1[0]}, I am inviting you to dinner.")
print(f"{_1[1]}, I am inviting you to dinner.")
print(f"{_1[3]}, I am inviting you to dinner.")


#Exercise 6:
#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

Rname2=_1.pop(2)
Rname3=_1.pop(1)
print("I'm sorry",Rname2+",","but there are only 2 seats available so I cannot invite you.")
print("I'm sorry",Rname3+",","but there are only 2 seats available so I cannot invite you.")

print(_1[0],"and",_1[1]+",","you both are still invited to dinner at my place.")

print("Current Names: ",_1)

del _1[1] 
del _1[0]

print("New Names: ",_1)



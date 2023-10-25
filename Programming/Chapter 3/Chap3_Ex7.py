#Exercise 7: Seeing The World (Sorting the list)
#Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.

countries=['hawaii','england','japan','dubai','america']
#Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
print("Normal Order:")
print(countries)

#Use sorted() to print your list in alphabetical order without modifying the actual list.
print("\nAlphabetical Order:")
print(sorted(countries))

#Show that your list is still in its original order by printing it.
print("\nNormal order:")
print(countries)

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print("\nReversed Alphabetical Order:")
print(sorted(countries, reverse=True))

#Show that your list is still in its original order by printing it again.
print("\nNormal Order:")
print(countries)

#Use reverse() to change the order of your list. Print the list to show that its order has changed.
print("\nReversed:")
countries.reverse()
print(countries)

#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
print("\nNormal Order:")
countries.reverse()
print(countries)

#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
print("\nAlphabetical Order:")
countries.sort()
print(countries)

#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
print("\nReversed Alphabetical Order:")
countries.sort(reverse=True)
print(countries)
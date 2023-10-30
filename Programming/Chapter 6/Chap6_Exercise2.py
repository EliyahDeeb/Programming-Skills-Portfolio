#Exercise 2: Movie Tickets

#It is the same as the pizza toppings exercise, but it acts differently.
#Tickets for the movie can have different prices for different age ranges.
#In this case, we use the 'if' and 'elif' commands so specific prices will be given depending on the age of that person.
#But just like the pizza toppings exercise, the loop breaks when you type 'Finish' in the console.
a = ("\nHow old are you?")
a += ("\nType 'Finish' when you are finished: ")

while True: 
    age = input(a)
    if age == 'Finish':
        print("All you have to do now is to pay for the tickets and enjoy the movie!")
        break
    age = int(age) 
    if age < 3: 
        print(" The ticket is free.")
    elif age < 13:
        print(" The ticket is 5$.") 
    else:
        print("The ticket is 15$.")

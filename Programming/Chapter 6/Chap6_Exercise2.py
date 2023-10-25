#Exercise 2: Movie Tickets
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
    
    
             
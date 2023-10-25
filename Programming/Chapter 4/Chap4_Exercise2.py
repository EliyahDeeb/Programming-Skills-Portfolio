#Exercise 2: Alien Colors (Part 2)
#It is the continuation of Exercise 1.

#This time, if the color is NOT Green, it will print out a different output instead of leaving it blank.

#If the color is Green, its output is "+5 Points!"
#If the color is not Green, the output will be "+10 Points!"

#Successful Version:
alien_color = ('Green')
if alien_color == 'Green':
    print("+5 Points!")
else:
    print("+10 Points!")
    
#Unsuccessful Version:
alien_color = ('Yellow')
if alien_color == 'Green':
    print("+5 Points!")
else:
    print("+10 Points!")
    
#The 'else' command will execute if the previous 'if' command's conditions aren't fulfilled.
#Exercise 1: Pizza Toppings
a = ("\nEnter your toppings.")
a += ("\nPlease type 'Finish' when you are finished: ")
#The "+" next to the variable is like a duplicate version of the same variable.

#The 'while()' command is a command that executes in a loop. It will continue to go on that loop until the condition of the while() command becomes false.

#The way this while() command works is that you can keep on adding toppings until you type 'Finish', then it will break the loop that the while() command is in.
while True: 
    topping = input(a)
    if topping != 'Finish':
        print(topping,"is added to your pizza.")
    else:
        print("Your pizza will be in the making, give us some time and it will be ready to go!")
        break
#Made a message after 'Finish' so it will give the user a message 
#instead of leaving it blank. 
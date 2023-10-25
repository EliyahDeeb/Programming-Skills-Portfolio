#Exercise 1: Pizza Toppings
a = ("\nEnter your toppings.")
a += ("\nPlease type 'Finish' when you are finished: ")
#The "+" next to the variable is like a duplicate version of the same variable.

while True:
    topping = input(a)
    if topping != 'Finish':
        print(topping,"is added to your pizza.")
    else:
        print("Your pizza will be in the making, give us some time and it is ready to go!")
        break
#Made a message after 'Finish' so it will give the user a message 
#instead of leaving it blank.
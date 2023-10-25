#Exercise 4: Stages of Life

#This exercise uses the 'if' command to determine whether the person 
#(who typed his/her age on the console)
#is either a baby, a toddler, a child, a teen, an adult, or an elder.

Age = int(input("Enter Age: "))
if Age <= 2:
    print("Baby")

elif Age <= 4:
    print("Toddler")
    #The 'elif' command acts like the 'if' command, 
    #but the command executes if another condition is met 
    #incase the previous 'if' command's condition isn't met.

elif Age <= 13:
    print("Child")

elif Age <= 20:
    print("Teenager")

elif Age <= 65:
    print("Adult")
    
else:
    print("Elder")
    
#Exercise 5: USB Shopper
#I personally made it so that the numbers must be added in the console.

#'Float' data type is used so it can determine whether you have extra cents or not

Product=float(input("Enter Price of Product: ")) #It's 6 pounds per USB.
Money=float(input("Enter Current Balance: "))

#This shows how many USBs you can buy.
AMNT=int(Money/Product) 
print("You can buy",AMNT,"pieces of this product.")

#This shows how much money will remain in your account.
RMN=float(Money-Product*AMNT)
print("You have",RMN,"remaining in your account.") 
#Exercise 5: USB Shopper
#IMPORTANT NOTE: I MADE IT UNIQUE SO YOU CAN INPUT THE NUMBERS LIKE A FUNCTIONING CALCULATOR!!!

Product=float(input("Enter Price of Product: ")) #Hint: it's 6 pounds per USB.
Money=float(input("Enter Current Balance: "))

AMNT=int(Money/Product) 
print("You can buy",AMNT,"pieces of this product.") #This shows how many USBs you can buy.

RMN=float(Money-Product*AMNT)
print("You have",RMN,"remaining in your account.") #This shows how much money will remain in your account.
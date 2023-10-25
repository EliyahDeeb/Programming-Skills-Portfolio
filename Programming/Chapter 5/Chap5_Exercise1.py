#Exercise 1: Person
#This exercise is about Dictionaries ('dict').
#The command 'dict' means Dictionary, and this command stores data
#that has been input in the console by the user. 

#Made an input so it looks like a login/sign up page.
First_Name = input("Enter First Name: ")
Last_Name = input("Enter Last Name: ")
Age = int(input("Enter Age: "))
Street = str(input("Enter Street Name: "))

info = {
        'first_name': First_Name,
        'last_name': Last_Name,
        'age': Age,
        'street_name': Street,
        }

#Now that the data has been stored, it can now be used without any problems.
print(info['first_name'])
print(info['last_name'])
print(info['age'])
print(info['street_name'])


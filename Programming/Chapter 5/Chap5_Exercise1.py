#Exercise 1: Person

#Made an input so it looks like a login/sign up page.
First_Name = input("Enter First Name: ")
Last_Name = input("Enter Last Name: ")
Age = int(input("Enter Age: "))
Street = str(input("Enter Street Name: "))

#"{}" means "dict", where it stores data that has been input by the user.
info = {
        'first_name': First_Name,
        'last_name': Last_Name,
        'age': Age,
        'street_name': Street,
        }
        
print(info['first_name'])
print(info['last_name'])
print(info['age'])
print(info['street_name'])


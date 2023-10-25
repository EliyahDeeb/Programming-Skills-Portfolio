#Exercise 5: Pets

pets = []
#LIST IS NEEDED TO STORE DATA FROM THE DICT

pet = {
    'Animal':'German Shephard',
    'Pet Name':'Fido',
    'Owner Name':'John',
    'Food':'Meats, Cheese, Vegetables'}
pets.append(pet)


pet = {
    'Animal':'British Longhair',
    'Pet Name':'Floof',
    'Owner Name':'Stacey',
    'Food':'Cooked Chicken, Cooked Fish, Steamed Peas'}
pets.append(pet)

    
pet = {
    'Animal':'Goldfish',
    'Pet Name':'Bob',
    'Owner Name':'Jesse',
    'Food':'Fish Flakes'}
pets.append(pet)


for pet in pets:
    print("\nPet Info of",pet['Pet Name'].title()+":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
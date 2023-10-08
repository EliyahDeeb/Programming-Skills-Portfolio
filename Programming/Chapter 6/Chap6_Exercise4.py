#Exercise 4: Deli

sandwich_orders = ['Seafood Sandwich','Egg Sandwich','Turkey Bacon Sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Currently making a",current_sandwich+"..")
    finished_sandwiches.append(current_sandwich)
    
print("\n")
for sandwich in finished_sandwiches:
    print(sandwich,"is finished!")
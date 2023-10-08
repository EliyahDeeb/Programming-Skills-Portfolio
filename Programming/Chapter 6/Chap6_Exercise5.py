#Exercise 5: No Pastrami
sandwich_orders = ['Seafood Sandwich','Egg Sandwich','Turkey Bacon Sandwich','Pastrami Sandwich','Pastrami Sandwich','Pastrami Sandwich']
finished_sandwiches = []

#This command will remove specific names in a list.
print("Sorry, we don't have Pastrami today.")
while 'Pastrami Sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami Sandwich')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Currently making a",current_sandwich+"..")
    finished_sandwiches.append(current_sandwich)
    
print("\n")
for sandwich in finished_sandwiches:
    print(sandwich,"is finished!")
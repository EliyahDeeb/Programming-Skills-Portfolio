#Exercise 4: Large Shirts
def make_shirt(size = 'Large',message = 'I love Python!'):
    print("\nA",size,"sized shirt will be made.")
    print('Its message will be: "'+message+'"')
    
make_shirt()
make_shirt(size = 'medium')
make_shirt('small','Programmers are loopy.')

#Exercise 5: Cities

def describe_city(name,country = 'Chile'):
    msg = name.title() + "is in" + country.title() + "."
    print(msg)
    
describe_city('chicago','america')
describe_city('valdivia')
describe_city('antofagasta')

    
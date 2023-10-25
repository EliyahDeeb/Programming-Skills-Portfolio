#Exercise 4: Rivers
#This Exercise is about Rivers, where a dictionary should be made where it
#contains information of three major rivers 
#and the country where these rivers belong in.
rivers = {
    'Nile':'Egypt',
    'Missouri':'America',
    'Yangtze':'China',
    }

#The data should be stored by now, so now it will be printed.

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())
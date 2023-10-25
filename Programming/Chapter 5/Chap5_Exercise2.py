#Exercise 2: Glossary

#Since the 'dict' command can store data, it can also store information.
#This Exercise will be about storing data in a glossary,
#so it can keep specific information about different words.
glossary = {
    'Define (def)':'Used for defining a function so you do not have to repeat it.',
    'Variables':'Variables are used for storing data.',
    'While':'Causes a loop in a command until a certain criteria is met.',
    'Integer (int)':'A whole number.',
    'Float':'A decimal number.'}

#All defenitions from the Dictionary will now be printed and shown in the console.
word = 'Define (def)'
print("\n" + word.title(),":",glossary[word])

word = 'Variables'
print("\n" + word.title(),":",glossary[word])

word = 'While'
print("\n" + word.title(),":",glossary[word])

word = 'Integer (int)'
print("\n" + word.title(),":",glossary[word])

word = 'Float'
print("\n" + word.title(),":",glossary[word])
#Exercise 3: Glossary Part 2

glossary = {
    'Define (def)':'Used for defining a function so you do not have to repeat it.',
    'Variables':'Variables are used for storing data.',
    'While':'Causes a loop in a command until a certain criteria is met.',
    'Integer (int)':'A whole number.',
    'Float':'A decimal number.',
    'Boolean':'Consists of True or False.',
    'String':'Collection of Data.',
    'Dictionary (dict)':'Collection of stored data as a set of key-value pairs.',
    'If statement':'The If command executes whenever a certain condition is met.',
    'Key':'The first pieces of data visible in a key-value pair in a dictionary.'}

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)
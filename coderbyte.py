def to_camel_case(string):#the function takes one arguement which is expected to be a string
    for characters in ['-','_']:#this loops through a list of characters
        string = string.replace(characters, '')#this line removes dashes & underscores from the string
    words = string.split()#.split() separates words whenever it finds spaces
    if not words:#checks if the list is empty
        return ''#if empty it returns an empty string
    camel_case = words[0].lower()#converts first word to lowercase
    for word in words[1:]:#loop goes through the rest of the words, starting from the second word (index 1) to the end.
        camel_case += word.capitalize()#Each word is capitalized(1st uppercase, the rest lowercase)
        #the += operator appends the result of word.capitalize() to its current value
    return camel_case

print(to_camel_case('Bob loves coding')) #output -> bobLovesCoding
        
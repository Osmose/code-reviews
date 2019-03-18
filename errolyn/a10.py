
bit_string = input("Please enter a 32-bit integer: ") # example: 10000000111111110000001100001111
# there is no input sanitization or error handling since the assignment did not ask for it,
# I would turn this into it's own function if that was a requirement.
bit_array = [] # holds the raw bit sets in an array
bit_parce =[] # holds parced values of bit_array

def split_string(string):
    while string: # this terminates when there is nothing left in "string".
        bit_array.append(string[:8]) #takes the first 8 charaters and appends to array
        string = string[8:] # removes first 8 charaters

def parce_8_bit_string():
    # what I would typlically do here is int(<string>, 2)
    # in a loop incrementing through the array of 8 bit chunks.
    # That would give me the value of the string with a base 2.
    # However it seems like the intent is to get us to do the calculation manually.
    for x in bit_array: #each element in array
        value = 0 # value of the parce
        position_value = int(len(x)) - 1 # since the first position in the the string has the highest bit value im incrementing down.
        for y in x: # each charater in string
            value += (int(y) * (2**(position_value))) # takes the current value and adds the value of y's position based on if its a 1 or a 0
            position_value -= 1 # lowers the value of the position
        bit_parce.append(str(value)) # adds value as a string to array.

def convert_array_to_string():
    return ".".join(map(str, bit_parce)) #joins the array elements with a "." and returns the string.

def handler(): # handles the program flow.
    split_string(bit_string)
    parce_8_bit_string()
    print("The dotted decimal notation is: " + convert_array_to_string())


handler()
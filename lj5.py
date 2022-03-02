prefixes = 'JKLMNOPQ'
suffix = 'ack'
special_suffix = 'uack'                     #special suffix for O and Q

for letter in prefixes:
    if (letter == 'O' or letter == 'Q'):    #if condition is true special suffix will be printed
        print(letter + special_suffix)
    else:
        print(letter + suffix)

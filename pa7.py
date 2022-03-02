#Part 1
print("PART 1\n")
alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d

def has_duplicates(str):
    hist = histogram(str)
    for letter in str:
        if hist[letter] > 1:                    #check if letter appeared more than once
            return True
    return False

for str in test_dups:                           #checking each test string for duplicates
    if has_duplicates(str):
        print(str, " has duplicates")
    else:
        print(str, " has no duplicates")


#Part 2
print("\nPART 2\n")
def missing_letters(str):
    global alphabet                             #using global variable
    miss_string = ""
    hist = histogram(str)
    for letter in alphabet:
        if letter not in hist:
            miss_string += letter               #collecting missing letters
    return miss_string

for str in test_miss:                           #checking each test string for missing letters
    m_letters = missing_letters(str)
    if m_letters != "":
        print(str, " is missing letters ", m_letters)
    else:
        print(str, " uses all the letters")








        

def invert_dict(d):                     #modified invertion function
     inverse = dict()
     for key in d:
          val = d[key]
          for list_elem in val:         #cycle for each of list elements
              if list_elem not in inverse:
                    inverse[list_elem] = key
              else:
                    inverse[list_elem].append(key)
     return inverse

def write_d_into_file(d, filename):
    fd = open(filename, 'w')
    for key in d:
        fd.write(key)                   #writing in format key:element
        fd.write(':')
        fd.write(d[key])
        fd.write('\n')
    fd.close()

def read_d_from_file(filename):
    dictionary = dict()
    try:
        fd = open(filename, 'r')
        ret = fd.readline().strip()
        while len(ret) > 0:
            #creating list of the items based on the ':' position and the delimeter
            lst = ret[ret.index(':') + 1:].split(', ')
            #placing this list into the dictionary
            dictionary[ret[:ret.index(':')]] = lst
            #reading the next line
            ret = fd.readline().strip()         
        fd.close()
        return dictionary
    except:
        print("An error has occurred.")


d = read_d_from_file("d_items.txt")
print("Dictionary from file: ", d)

d = invert_dict(d)
print("\nInverted dictionary: ", d)
write_d_into_file(d, "d_i_items.txt")


s = "ocean clinic stone cat raccoon glass macarons mail nail long sand smooth"

#using split to create a list from the string
s_list = s.split()

#removing three elements with different methods
s_list.pop(0)
s_list.remove(s_list[0])
del s_list[0]

#sorting the list
s_list.sort()

#adding three new words to the list with different methods
s_list.append("moose")
s_list.insert(0, "tsunami")
s_list.extend(["dragon"])

#join the list back to a string
s = " ".join(s_list)

print(s)


#Part 2
def filter_num_one(lst):
    tmp = []
    for elem in lst:
        if "1" in elem:
            tmp.append(elem)
    return tmp

def wrong_operation(lst):
    new_element = ["0_2"]
    lst + new_element


nested_list = ["0_0", "0_1", ["1_0", "1_1"]]    #one list inside another
print ("nested list:", nested_list)
print ("list * 2:", nested_list * 2)            #repeating the list
print ("slicing the list:", nested_list[2:])    #slicing the list only to print 3rd element
nested_list += ["0_3"]                          #adding a new element to the list
print ("with new element:", nested_list)
new_list = filter_num_one(nested_list)          #variable for filtering result
print ("filtered list:", new_list)
wrong_operation(new_list)                       #adding new value in a wrong way
print ("after wrong usage of operator + :", new_list)









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

dict_w_list = {'food': ["Yogurt", "Cheese", "Banana"], 'animals': ["Wolf", "Fox", "Cat"], 'drinks': ["Milk", "Water", "Juice"]}
print("Original dictionary = ", dict_w_list)
print("Inverted dictionary = ", invert_dict(dict_w_list))

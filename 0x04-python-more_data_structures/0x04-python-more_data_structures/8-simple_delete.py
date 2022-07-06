import print_sorted_dictionary

def print_sorted_dictionary(a_dictionary):
    a_dictionary = dict(a_dictionary)
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")


def simple_delete(a_dictionary, key=""):
    a_dictionary = dict(a_dictionary)
    for i in a_dictionary:
        if i != key:
            return
        del a_dictionary[key]
    return a_dictionary


a_dictionary = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
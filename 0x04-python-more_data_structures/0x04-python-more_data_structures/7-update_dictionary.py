#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary = dict(a_dictionary)

    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")


def update_dictionary(a_dictionary, key, value):
    a_dictionary = dict(a_dictionary)
    a_dictionary[key] = value
    return dict(a_dictionary)


a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
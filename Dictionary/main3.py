import copy
original_dict = {
    'name': 'Aryan',
    'address': {'city': 'jaipur', 'street': 'main Rd'},
    'hobbies': ['reading', 'painting', 'chess']
}
shallow_copied_dict = original_dict.copy()
shallow_copied_dict['address']['city'] = 'london'
shallow_copied_dict['hobbies'].append('coding')
print("Original Dictionary (after modification in shallow copy):")
print(original_dict)
print("\nShallow Copied Dictionary:")
print(shallow_copied_dict)
#PROBLEM:After using dict.copy(), both the original and shallow copied dictionaries point to the
# same nested objects (e.g., address and hobbies).
#DEEP COPY FIX
deep_copied_dict = copy.deepcopy(original_dict)
deep_copied_dict['address']['city'] = 'paris'
deep_copied_dict['hobbies'].append('coding')
print("Original Dictionary (after modification in deep copy):")
print(original_dict)
print("\nDeep Copied Dictionary:")
print(deep_copied_dict)

#After using copy.deepcopy(), the original and deep copied dictionaries are completely independent.
#Changes made to the deep copy (modifying the 'address' and 'hobbies') do not affect the original dictionary.
#This is because deepcopy recursively copies all the nested structures, so the original and the copy don't share references to the same objects in memory.


def merge_dicts(d1, d2):
    merged_dict = d1.copy() 
    for key, value in d2.items():
        if key in merged_dict:
            merged_dict[key] = max(merged_dict[key], value)
        else:
            merged_dict[key] = value
    return merged_dict
d1 = {'a': 5, 'b': 10}
d2 = {'b': 7, 'c': 3}
result = merge_dicts(d1, d2)
print(result)

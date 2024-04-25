supermarket_items = {'milk', 'bread', 'cheese', 'butter', 'eggs', 'yogurt', 'pepsi', 'chips', 'tide', 'soap'}

convert_to_list = list(supermarket_items)
convert_to_tuples = tuple(supermarket_items)
convert_back_to_set = set(convert_to_list)

print(f'Supermarket items {supermarket_items}')
print(f'Converted to list {convert_to_list}')
print(f'Converted to tuples {convert_to_tuples}')
print(f'Converted back to set {convert_back_to_set}')
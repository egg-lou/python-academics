supermarket_items = {'milk', 'bread', 'cheese', 'butter', 'eggs', 'yogurt', 'pepsi', 'chips', 'tide', 'soap'}

supermarket_copy = supermarket_items.copy()

to_add = {'luisa', 'mark', 'louie'}

print(f"Printing supermarket items {supermarket_items}")
supermarket_items.add('luisa')
length = len(supermarket_items)
print(f"Lenght of supermarket items {length}")
print(f"Printing supermarket items {supermarket_items}")
supermarket_items.update(to_add)
print(f"Printing supermarket items {supermarket_items}")
supermarket_items.remove('luisa')
print(f"Printing supermarket items {supermarket_items}")
supermarket_items.discard('mark')
to_add.clear()
print(f'Cleared to_add {to_add}')
print(f'Copied supermarket items {supermarket_copy}')

combined_union = supermarket_items.union(supermarket_copy)
print(f"Combined union {combined_union}")

combined_difference = supermarket_items.difference(supermarket_copy)
print(f"Combined difference {combined_difference}")

combined_intersect = supermarket_items.intersection(supermarket_copy)
print(f"Combined intersect {combined_intersect}")

exclusive = supermarket_items.symmetric_difference(supermarket_copy)
print(f"Exclusive {exclusive}")

is_disjoint = supermarket_items.isdisjoint(supermarket_copy)
print(f"Is disjoint {is_disjoint}")

is_subset = supermarket_items.issubset(supermarket_copy)
print(f"Is subset {is_subset}")

is_superset = supermarket_items.issuperset(supermarket_copy)
print(f"Is superset {is_superset}")

convert_to_list = list(supermarket_items)
convert_to_tuples = tuple(supermarket_items)

print(f"Converted to list {convert_to_list}")
print(f"Converted to tuples {convert_to_tuples}")

convert_back_to_set = set(convert_to_list)
print(f"Converted back to set {convert_back_to_set}")




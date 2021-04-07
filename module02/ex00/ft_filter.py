import string

def ft_filter(function_to_apply, list_of_inputs):
    if not list_of_inputs or not function_to_apply:
        print("ERROR")
        return ()
    result = []
    for inp in list_of_inputs:
        result.append(inp) if function_to_apply(inp) else 0
    return result

def even(x):
    return True if x % 2 == 0 else False

l = [2, 89, 57, 45, 34, 0, 15]
print(f"list before {l}")
print("list after " , ft_filter(even, l))
print("list after " , list(filter(even, l)))

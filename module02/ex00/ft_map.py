import string

def ft_map(function_to_apply, list_of_inputs):
    if not list_of_inputs or not function_to_apply:
        print("ERROR")
        return ()
    result = []
    for inp in list_of_inputs:
        result.append(function_to_apply(inp))
    return result

def funct(x):
    return x * x

l = [1, 2, 3]
print(f"list before {l}")
print("list after " , ft_map(funct, l))
print("list after " , list(map(funct, l)))

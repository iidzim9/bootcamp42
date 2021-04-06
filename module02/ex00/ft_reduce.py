from ft_map import ft_map

def ft_reduce(function_to_apply, list_of_inputs):
    if not list_of_inputs or not function_to_apply:
        print("ERROR")
        return ()
    result = []
    for inp in list_of_inputs:
        result = ft_map(function_to_apply, inp)
    return result
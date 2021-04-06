def ft_map(function_to_apply, list_of_inputs):
    if not list_of_inputs or not function_to_apply:
        print("ERROR")
        return ()
    result = []
    for inp in list_of_inputs:
        result = function_to_apply(inp).append()
    return result

# list(map(func, list_inputs))
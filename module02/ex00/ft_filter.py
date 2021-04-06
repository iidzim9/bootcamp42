def ft_filter(function_to_apply, list_of_inputs):
    if not list_of_inputs or not function_to_apply:
        print("ERROR")
        return ()
    result = []
    for inp in list_of_inputs:
        result.append(inp) if function_to_apply(inp) else 0
    return result
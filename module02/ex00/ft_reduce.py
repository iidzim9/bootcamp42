from functools import reduce

def ft_reduce(function_to_apply, list_of_inputs):
    if not list_of_inputs or not function_to_apply:
        print("ERROR")
        return ()
    result = list_of_inputs[0]
    for inp in list_of_inputs[1:]:
        result = function_to_apply(result, inp)
    return result

def fact(x, y):
    return x * y

print("hello world")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"88list before {l}")
print("list after " , reduce(fact, l))
print("list after " , ft_reduce(fact, l))

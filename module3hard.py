calculate_sum = []
def calculate_structure_sum(*args):

    for i in args:
        if isinstance(i, int) == True:
            calculate_sum.append(i)
        elif isinstance(i, str) == True:
            calculate_sum.append(len(i))
        elif isinstance(i, list) == True:
            list_= i
            calculate_structure_sum(*list_)
        elif isinstance(i, dict) == True:
            dict_ = i.items()
            calculate_structure_sum(*dict_)
        elif isinstance(i, tuple) == True:
            tuple_ = list(i)
            calculate_structure_sum(*tuple_)
        elif isinstance(i, set) == True:
            set_ = list(i)
            calculate_structure_sum(*set_)

    return sum(calculate_sum)

data_structure = [[1, 2, 3], {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}), "Hello", ((),[{(2, 'Urban', ('Urban2',35))}])]

result = calculate_structure_sum(*data_structure)
print(result)
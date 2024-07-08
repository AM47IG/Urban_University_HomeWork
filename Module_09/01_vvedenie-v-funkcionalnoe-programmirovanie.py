def apply_all_func(int_list, *functions):
    res_dict = {}
    for func in functions:
        res_dict[func.__name__] = func(int_list)
    return res_dict


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
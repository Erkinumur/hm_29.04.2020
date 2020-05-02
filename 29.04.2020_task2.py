num_list = [int(i) for i in input('Введите числа через пробел: ').split()]
max_num = max(num_list)
min_num = min(num_list)
if max_num <= 0 or min_num > 1:
    print(1)
elif max_num == 1:
    print(2)
else:
    one_to_max = set(range(1, max_num + 1))
    if one_to_max == set(num_list):
        print(max_num + 1)
    else:
        print(min(one_to_max - set(num_list)))
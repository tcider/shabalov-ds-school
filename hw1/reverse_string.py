def reverse_string(str):
    str_list = list(str)
    str_len = len(str)
    for i in range (str_len // 2):
        str_list[i], str_list[str_len - i - 1] = \
            str_list[str_len -i - 1], str_list[i]
    return ''.join(str_list)


str = input()
print(reverse_string(str))

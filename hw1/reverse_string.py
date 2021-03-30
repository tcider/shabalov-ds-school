from typing import List


def reverse_string(str_arg: str) -> str:
    str_list: List[str] = list(str_arg)
    str_len: int = len(str_arg)
    for i in range(str_len // 2):
        str_list[i], str_list[str_len - i - 1] = str_list[str_len - i - 1], str_list[i]
    return "".join(str_list)


str_inp = input()
print(reverse_string(str_inp))

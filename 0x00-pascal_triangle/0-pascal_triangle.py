#!/usr/bin/python3
"""Pascal's triangle module"""


def get_next_triangle(old_list):
    """gets next trianlge"""
    initial_list = old_list
    new_list = []
    for i in range(len(initial_list)):
        if (i == len(initial_list) - 1):
            new_list.insert(0, 1)
            new_list.append(1)
            break
        new_list.append(initial_list[i] + initial_list[i + 1])
    return new_list


def pascal_triangle(n):
    """returns a pascal's triangle list"""
    overall_list = []
    if n < 1:
        return []

    if n >= 1:
        overall_list.append([1])

    new_list = [1]
    list_extension = []

    for i in range(n):
        if (len(list_extension) != 0):
            overall_list.append(list_extension)
        list_extension = get_next_triangle(new_list)
        new_list = list_extension

    return overall_list

#!/usr/bin/python3
"""Utf-8 validation module"""


def get_significant_bits(num):
    """get significant bits"""
    set_bits = 0
    one_two_eight = 128
    while one_two_eight & num:
        set_bits += 1
        one_two_eight = one_two_eight >> 1
    return set_bits


def check_next_valid_bytes(num_set_bit, char_list, curr_index):
    """check next valid bytes"""
    num_bytes_to_check = num_set_bit - 1
    if (curr_index + num_bytes_to_check) < len(char_list):
        count = 1
        for _ in range(num_bytes_to_check):
            byte_to_check = char_list[curr_index + count]
            count += 1
            if (byte_to_check & 1 << 7) and not (byte_to_check & 1 << 6):
                continue
            else:
                return -1
    else:
        return -1
    return curr_index + num_set_bit


def validUTF8(data):
    """check valid utf8"""
    for index in range(len(data)):
        set_bits = get_significant_bits(data[index])
        if set_bits == 1 or set_bits > 4:
            return False
        if set_bits == 0:
            continue
        next_index = check_next_valid_bytes(set_bits, data, index)
        if next_index == -1:
            return False
        index = next_index
    return True

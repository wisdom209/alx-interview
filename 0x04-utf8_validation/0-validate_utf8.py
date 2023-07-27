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


def check_continuation_bytes(num_set_bits, index, data):
    """
    Check if the continuation bytes of a multi-byte UTF-8 sequence are valid,
    given the number of set bits.
    """
    for i in range(index + 1, index + num_set_bits):
        if i >= len(data):
            return False
        if (data[i] & 0b11000000) != 0b10000000:
            return False
    return True


def validUTF8(data):
    """check valid utf8"""
    i = 0
    while i < len(data):
        num_set_bits = get_significant_bits(data[i])
        if num_set_bits == 1 or num_set_bits > 4:
            return False
        if not check_continuation_bytes(num_set_bits, i, data):
            return False
        if num_set_bits == 0:
            i += 1
        else:
            i += num_set_bits
    return True

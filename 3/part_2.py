from collections import Counter
from enum import Enum

from utils import read_bits


class Significance(Enum):
    MOST_COMMON = 1
    LEAST_COMMON = 2


def run_part_two():
    print("--------------------------------")
    print("Advent of Code 2021 - 3 - Part 2")
    bits = read_bits('input.txt')
    most_common_indexes = list(range(len(bits)))
    least_common_indexes = list(range(len(bits)))

    for x in range(len(bits[0])):
        most_common_indexes = _get_common_items(Significance.MOST_COMMON, most_common_indexes, x, bits)
        least_common_indexes = _get_common_items(Significance.LEAST_COMMON, least_common_indexes, x, bits)

    oxygen_rating = "".join(bits[most_common_indexes[0]])
    co2_scrubber_rating = "".join(bits[least_common_indexes[0]])

    print('Power consumption: {0}'.format(int(oxygen_rating, 2) * int(co2_scrubber_rating, 2)))


def _get_common_items(significance: Significance, common_bits, column: int, bits):
    temp_bits = []
    temp_tuples = []
    if len(common_bits) == 1:
        return common_bits

    for y in common_bits:
        temp_bits.append(bits[y][column])
        temp_tuples.append((y, bits[y][column]))

    number_of_bits = dict(Counter(temp_bits))
    most_significant_bit = _get_bit_significance(significance, number_of_bits)
    return list(
        map(lambda x: x[0], list(filter(lambda tup: tup[1] == most_significant_bit, temp_tuples))))


def _get_most_common_significance(bits):
    if bits['0'] == bits['1']:
        return '1'
    return '0' if bits['0'] > bits['1'] else '1'


def _get_least_common_significance(bits):
    if bits['0'] == bits['1']:
        return '0'
    return '1' if bits['0'] > bits['1'] else '0'


def _get_bit_significance(significance: Significance, bits):
    if significance == Significance.MOST_COMMON:
        return _get_most_common_significance(bits)
    return _get_least_common_significance(bits)

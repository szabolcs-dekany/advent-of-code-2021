from collections import Counter

from utils import read_bits


def run_part_one():
    print("--------------------------------")
    print("Advent of Code 2021 - 3 - Part 1")
    bits = read_bits('input.txt')
    gamma_rate = ""
    epsilon_rate = ""
    for x in range(len(bits[0])):
        relevant_bits = get_relevant_bits_for_row(bits, x)
        gamma_rate += relevant_bits[0]
        epsilon_rate += relevant_bits[1]

    print('Binary - Gamma rate: {0}, Epsilon rate: {1}'.format(gamma_rate, epsilon_rate))
    print('Decimal - Gamma rate: {0}, Epsilon rate: {1}'.format(int(gamma_rate, 2), int(epsilon_rate, 2)))
    print('Power consumption: {0}'.format(int(gamma_rate, 2) * int(epsilon_rate, 2)))


def get_relevant_bits_for_row(bits: [[str]], row: int):
    row_bits = []
    for x in range(len(bits)):
        row_bits.append(bits[x][row])
    number_of_bits = dict(Counter(row_bits))
    most_significant_bit = '0' if number_of_bits['0'] > number_of_bits['1'] else '1'
    least_significant_bit = '0' if most_significant_bit == '1' else '1'

    return most_significant_bit, least_significant_bit

# Uses python3
# Given an integer n, compute the minimum number of operations needed to obtain the number n starting from the number 1
# Allowed operations:
#    - add 1
#    - multiply by 2
#    - multiply by 3
# Input: single integer from 1 to 10^6
# ie.
# 96234
# Output:
#    14
#    1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234


import sys


def main():
    input_data = sys.stdin.read()
    n = int(input_data)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')


def optimal_sequence(n):
    sequence, minimal_operation_numbers = init_seq()
    fill_sequence_of_minimal_operations(minimal_operation_numbers, n)
    fill_sequence_of_digit_to_compute_n(minimal_operation_numbers, n, sequence)
    return reversed(sequence)


def fill_sequence_of_digit_to_compute_n(minimal_operation_numbers, n, sequence):
    sequence.append(n)
    while n > 1:
        n = append_optimal_number(minimal_operation_numbers, n, sequence)


def append_optimal_number(minimal_operation_numbers, n, sequence):
    a = b = c = minimal_operation_numbers[n] - 1
    if n % 2 == 0:
        a = minimal_operation_numbers[(n // 2)]
    if n % 3 == 0:
        b = minimal_operation_numbers[(n // 3)]
    e = min(a, b, c)
    if n % 2 == 0 and e == a:
        n //= 2
    elif n % 3 == 0 and e == b:
        n //= 3
    else:
        n -= 1
    sequence.append(n)
    return n


def fill_sequence_of_minimal_operations(minimal_operation_numbers, n):
    for i in range(2, n + 1):
        append_optimal_result(i, minimal_operation_numbers)


def append_optimal_result(i, minimal_operation_numbers):
    a = b = c = minimal_operation_numbers[i - 1] + 1
    if i % 2 == 0:
        a = minimal_operation_numbers[(i // 2)] + 1
    if i % 3 == 0:
        b = minimal_operation_numbers[(i // 3)] + 1
    e = min(a, b, c)
    minimal_operation_numbers.append(e)


def init_seq():
    sequence = []
    minimal_operation_numbers = [0, 0]
    return sequence, minimal_operation_numbers


if __name__ == '__main__':
    main()

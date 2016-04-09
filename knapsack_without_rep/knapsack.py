# Uses python3
# Knapsack without repetitions with weight of elements proportional to their values ie. gold bars

# Input
# The first line of the input contains the capacity W of a knapsack and the number n of elements
# The next line contains n integers w0, w1, . . . , wn−1 defining the weights of the elements.

# Example:
# 10 3
# 1 4 8
# Output: 9

import sys


def optimal_weight(knapsack_capacity, elements_weights):
    knapsack, number_of_all_elements = initialize_knapsack(elements_weights, knapsack_capacity)
    pack_knapsack(knapsack, knapsack_capacity, number_of_all_elements, elements_weights)
    optimal_knapsack_weight = knapsack[len(elements_weights)][knapsack_capacity]
    return optimal_knapsack_weight


def initialize_knapsack(elements_weights, knapsack_capacity):
    number_of_all_elements = len(elements_weights)
    knapsack = [[0 for x in range(knapsack_capacity + 2)] for x in range(number_of_all_elements + 1)]
    return knapsack, number_of_all_elements


def pack_knapsack(knapsack, knapsack_capacity, number_of_all_elements, elements_weights):
    for element_number in range(1, number_of_all_elements + 1):
        pack_element(element_number, elements_weights, knapsack, knapsack_capacity)


def pack_element(element_number, elements_weights, knapsack, knapsack_capacity):
    for weight in range(1, knapsack_capacity + 2):
        pack_to_weight_cells(element_number, elements_weights, knapsack, weight)


def pack_to_weight_cells(element_number, elements_weights, knapsack, weight):
    knapsack[element_number][weight] = knapsack[element_number - 1][weight]
    if elements_weights[element_number - 1] <= weight:
        pack_optimal_element(element_number, elements_weights, knapsack, weight)


def pack_optimal_element(element_number, elements_weights, knapsack, weight):
    val = (knapsack[element_number - 1][weight - elements_weights[element_number - 1]]) + elements_weights[
        element_number - 1]
    if knapsack[element_number][weight] < val:
        knapsack[element_number][weight] = val


def main():
    input_data = sys.stdin.read()
    knapsack_capacity, n, *elements_weights = list(map(int, input_data.split()))
    print(optimal_weight(knapsack_capacity, elements_weights))


if __name__ == '__main__':
    main()

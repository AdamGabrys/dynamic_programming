# Uses python3
# Maximize the Value of an Arithmetic Expression
# Find the maximum value of an arithmetic expression by specifying the order of applying its arithmetic
# operations using additional parentheses.
#
# Input
# arithmetic expression
# ie.
# 5-8+7*4-8+9
# Output: 200


def evaluate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        assert False


def get_operands_and_operators_from_expression(expression, operators, operands):
    for i in range(len(expression)):
        separate_operands_and_operators(expression, i, operands, operators)


def separate_operands_and_operators(expression, i, operands, operators):
    if expression[i] == '+' or expression[i] == '*' or expression[i] == '-':
        operators.append(expression[i])
    else:
        operands.append(int(expression[i]))


def get_maximum_value(expression):
    operands, operators = init_operands_and_operators(expression)
    maximums_of_all_subexpressions, minimums_of_all_subexpressions = init_max_and_min_matrices_of_all_subexpressions(
        operands)
    fill_max_and_min_matrices(maximums_of_all_subexpressions, minimums_of_all_subexpressions, operands, operators)
    return maximums_of_all_subexpressions[len(operands)][1]


def fill_max_and_min_matrices(maximums_of_all_subexpressions, minimums_of_all_subexpressions, operands, operators):
    for s in range(1, len(operands)):               # Goes trough all possible pairs
        for i in range(1, len(operands) + 1 - s):   # ------------------------------
            insert_optimal_solution(i, maximums_of_all_subexpressions, minimums_of_all_subexpressions, operators, s)


def insert_optimal_solution(i, maximums_of_all_subexpressions, minimums_of_all_subexpressions, operators, s):
    j = i + s
    minimums_of_all_subexpressions[j][i], maximums_of_all_subexpressions[j][i] = \
        get_min_and_max_of_subexpression(i, j, minimums_of_all_subexpressions, maximums_of_all_subexpressions,
                                         operators)


def init_max_and_min_matrices_of_all_subexpressions(operands):
    minimums_of_all_subexpressions = [[0 for x in range(len(operands) + 1)] for x in range(len(operands) + 1)]
    maximums_of_all_subexpressions = [[0 for x in range(len(operands) + 1)] for x in range(len(operands) + 1)]
    for i in range(1, len(operands) + 1):
        minimums_of_all_subexpressions[i][i] = maximums_of_all_subexpressions[i][i] = operands[i - 1]
    return maximums_of_all_subexpressions, minimums_of_all_subexpressions


def init_operands_and_operators(expression):
    operators = []
    operands = []
    get_operands_and_operators_from_expression(expression, operators, operands)
    return operands, operators


def get_min_and_max_of_subexpression(i, j, minimums_of_all_subexpressions, maximums_of_all_subexpressions, operators):
    minimum = float('inf')
    maximum = float('-inf')
    for k in range(i, j):
        a = evaluate(maximums_of_all_subexpressions[k][i], maximums_of_all_subexpressions[j][k+1], operators[k-1])
        b = evaluate(maximums_of_all_subexpressions[k][i], minimums_of_all_subexpressions[j][k+1], operators[k-1])
        c = evaluate(minimums_of_all_subexpressions[k][i], maximums_of_all_subexpressions[j][k+1], operators[k-1])
        operands = evaluate(minimums_of_all_subexpressions[k][i], minimums_of_all_subexpressions[j][k+1], operators[k-1])
        minimum = min(a, b, c, operands, minimum)
        maximum = max(a, b, c, operands, maximum)
    return minimum, maximum


if __name__ == "__main__":
    print(get_maximum_value(input()))

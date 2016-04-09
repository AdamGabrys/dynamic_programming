# Uses python3
# Computes the edit distance between two strings that is the minimum number of insertions, deletions, and mismatches
# in an alignment of two strings.
# Input:
#    first_string
#    second_string
# Example:
#   editing
#   distance
#   Output: 5
#
# e d i − t i n g −
# − d i s t a n c e


def edit_distance(first_string, second_string, indel_cost, mismatch_cost):
    edit_distance_matrix = initialize_edit_distance_matrix(first_string, second_string)
    fill_edit_distance_matrix(edit_distance_matrix, first_string, indel_cost, mismatch_cost, second_string)
    best_edit_distance = edit_distance_matrix[len(second_string)][len(first_string)]
    return best_edit_distance


def initialize_edit_distance_matrix(first_string, second_string):
    edit_distance_matrix = [[0 for x in range(len(first_string) + 1)] for x in range(len(second_string) + 1)]
    for fir_str_char_index in range(0, len(first_string) + 1):
        edit_distance_matrix[0][fir_str_char_index] = fir_str_char_index
    for fir_str_char_index in range(len(second_string) + 1):
        edit_distance_matrix[fir_str_char_index][0] = fir_str_char_index
    return edit_distance_matrix


def fill_edit_distance_matrix(edit_distance_matrix, first_string, indel_cost, mismatch_cost, second_string):
    for sec_str_char_index in range(1, len(second_string) + 1):
        fill_matrix_edit_distances_for_fir_str_to_sec_str_char_index(edit_distance_matrix, first_string, indel_cost,
                                                                     mismatch_cost, sec_str_char_index, second_string)


def fill_matrix_edit_distances_for_fir_str_to_sec_str_char_index(edit_distance_matrix, first_string, indel_cost,
                                                                 mismatch_cost, sec_str_char_index, second_string):
    for fir_str_char_index in range(1, len(first_string) + 1):
        compute_edit_distance_beetwean_first_str_char_ind_and_sec_str_char_ind(edit_distance_matrix, fir_str_char_index,
                                                                              first_string, indel_cost, mismatch_cost,
                                                                              sec_str_char_index, second_string)


def compute_edit_distance_beetwean_first_str_char_ind_and_sec_str_char_ind(edit_distance_matrix, fir_str_char_index,
                                                                          first_string, indel_cost, mismatch_cost,
                                                                          sec_str_char_index, second_string):
    insertion = edit_distance_matrix[sec_str_char_index - 1][fir_str_char_index] + indel_cost
    deletion = edit_distance_matrix[sec_str_char_index][fir_str_char_index - 1] + indel_cost
    match = edit_distance_matrix[sec_str_char_index - 1][fir_str_char_index - 1]
    mismatch = edit_distance_matrix[sec_str_char_index - 1][fir_str_char_index - 1] + mismatch_cost
    chose_and_insert_optimal_edit_distance(deletion, edit_distance_matrix, fir_str_char_index, first_string, insertion,
                                           match, mismatch, sec_str_char_index, second_string)


def chose_and_insert_optimal_edit_distance(deletion, edit_distance_matrix, fir_str_char_index, first_string, insertion,
                                           match, mismatch, sec_str_char_index, second_string):
    if first_string[fir_str_char_index - 1] == second_string[sec_str_char_index - 1]:
        edit_distance_matrix[sec_str_char_index][fir_str_char_index] = min(insertion, deletion, match)
    else:
        edit_distance_matrix[sec_str_char_index][fir_str_char_index] = min(insertion, deletion, mismatch)


if __name__ == "__main__":
    print(edit_distance(input(), input(), 1, 1))

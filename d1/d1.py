import numpy as np
from collections import Counter


def read_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    split_lists = [[int(x.strip().split('   ')[0].strip()),
                    int(x.strip().split('   ')[1].strip())] for x in lines]
    left = [x[0] for x in split_lists]
    right = [x[1] for x in split_lists]
    return left, right


def compute_distance_sum(left: np.array, right: np.array):
    differences = left - right
    abs_differences = [abs(difference) for difference in differences]
    return sum(abs_differences)


def solve_part_one(left_list, right_list):
    left_list_sorted = np.array(sorted(left_list))
    right_list_sorted = np.array(sorted(right_list))
    distance_sum = compute_distance_sum(left_list_sorted, right_list_sorted)
    print(distance_sum)


def solve_part_two(left_list, right_list):
    counter = Counter(right_list)
    similarity_score = [counter[x] * x for x in left_list]
    return sum(similarity_score)


if __name__ == '__main__':
    example = 'example.txt'
    real = 'input.txt'
    left_read, right_read = read_file(real)
    res = solve_part_two(left_read, right_read)
    print(res)

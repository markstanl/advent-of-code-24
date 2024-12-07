"""
--- Day 7: Bridge Repair ---
Honestly not too bad of a day. We solve this problem recursively, by
considering all possibilities of operations on the numbers. Even if there is a
cool algorithm to figure out which operations to use, I think that this is not
too bad of a solution! I'm happy with it.
"""

def read_file(file_path):
    """
    Converts the file into a list of pairs of integers and lists of number to
    operate on.
    e.g.
    [
        [1, [2, 3, 4]],
        [2, [3, 4, 5]],
        ...
    ]
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [[int(line.split(':')[0]),
             [int(num) for num in line.split(':')[1].strip().split(' ')]] for
            line in lines]


def perform_math(original_nums, operations):
    """
    Returns the result of the operations on the numbers.
    """
    nums = original_nums[:]
    count = nums.pop(0)
    while len(operations) > 0:
        operation = operations.pop(0)
        num = nums.pop(0)
        if operation == '+':
            count += num
        elif operation == '*':
            count *= num
    return count


def determine_validity(num, nums, operations):
    """
    Determines if the operations on the numbers will result in the given
    number. Does so recursively without any specific logic.
    """
    if len(operations) == len(nums) - 1:
        if perform_math(nums, operations) == num:
            return True
    else:
        if determine_validity(num, nums, operations[:] + ['*']):
            return True
        if determine_validity(num, nums, operations[:] + ['+']):
            return True


def solve_part_one(file):
    """
    Solves part one of the problem.
    """
    count = 0
    for line in file:
        if determine_validity(line[0], line[1], []):
            count += line[0]

    print(count)


def perform_two_math(original_nums, operations):
    """
    Returns the result of the operations on the numbers, including the
    || operator.
    """
    nums = original_nums[:]
    count = nums.pop(0)
    while len(operations) > 0:
        operation = operations.pop(0)
        num = nums.pop(0)
        if operation == '+':
            count += num
        elif operation == '*':
            count *= num
        elif operation == '||':
            count = int(str(count) + str(num))
    return count


def determine_two_validity(num, nums, operations):
    """
    Recursively tests all possibilities of operations on the numbers to see if
    the result is the given number, using the helper method
    """
    if len(operations) == len(nums) - 1:
        if perform_two_math(nums, operations) == num:
            return True
    else:
        if determine_two_validity(num, nums, operations[:] + ['*']):
            return True
        if determine_two_validity(num, nums, operations[:] + ['+']):
            return True
        if determine_two_validity(num, nums, operations[:] + ['||']):
            return True


def solve_part_two(file):
    """
    Solves part two of the problem.
    """
    count = 0
    for line in file:
        if determine_two_validity(line[0], line[1], []):
            count += line[0]

    print(count)


if __name__ == '__main__':
    example = 'example.txt'
    real = 'input.txt'

    file = read_file(real)
    # solve_part_one(file)
    solve_part_two(file)

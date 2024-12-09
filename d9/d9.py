"""
--- Day 9: Disk Fragmenter ---
This little guy took me a while. My first solution seems pretty darn optimal.
I am well aware in the second one there are some unnecessary checks but I am
happy with the solution.
"""


def read_file(file_path):
    """
    Reads the file. As it is a single line we just read the first line and
    strip it.
    """
    with open(file_path, 'r') as f:
        return f.read().strip()


def generate_list(num_map):
    """
    Generates a list of numbers and dots based on the input. Follows the weird
    rules they have in place. Alternating between numbers and dots.
    """
    new_list = []
    current_id = 0
    even = True
    for num in num_map:
        if even:
            even = False
            new_list += [str(current_id)] * int(num)
            current_id += 1
        else:
            even = True
            new_list += ['.'] * int(num)
    return new_list


def compress_list(num_list):
    """
    Compresses the list by switching the numbers and dots. Uses a two pointer
    solution to the problem. Seems optimal in my mind.
    """
    left = 0
    right = len(num_list) - 1
    while left < right:
        if num_list[left] == '.' and num_list[right] != '.':
            # case where we want to make a switch
            num_list[left], num_list[right] = num_list[right], num_list[left]
            left += 1
            right -= 1
        elif num_list[left] != '.' and num_list[right] != '.':
            # when we only want left to move
            left += 1
        elif num_list[left] == '.' and num_list[right] == '.':
            # when we only want right to move
            right -= 1
        else:
            # we want both to move
            left += 1
            right -= 1
    return num_list


def solve_part_one(file):
    """
    Solves part one and prints the output
    """
    num_list = generate_list(file)
    compressed_list = compress_list(num_list)
    checksum_list = [int(num) * i for i, num in enumerate(compressed_list) if
                     num != '.']
    print(sum(checksum_list))


def compute_size(num_list, index):
    """
    Computes the number of dots or numbers in a row. We first check if the
    content is a dot or a number. If it is a dot, we check how many more dots
    exist to the right, and vice verse for the number. We assume that the index
    is specifically chosen knowing that one of the two will be true.
    """
    if num_list[index] == '.':
        # left checking
        new_index = index
        while new_index < len(num_list) and num_list[new_index] == '.':
            new_index += 1
        return new_index - index
    else:
        # right checking
        new_index = index
        original_value = num_list[index]
        while new_index > 0 and num_list[new_index] == original_value:
            new_index -= 1
        return index - new_index


def find_left(num_list, left, size):
    """
    Finds the left index where we can place the right number. We find so by
    iterating over all left indexes and checking if the length of the dots is
    enough to fit the right number. If it is we return the index, if not we
    return -1
    """
    while left < len(num_list):
        if num_list[left] == '.':
            left_dot_length = compute_size(num_list, left)
            if left_dot_length >= size:
                return left
        left += 1
    return -1


def compress_list_two(num_list):
    """
    Compresses the list by switching the numbers and dots. Roughly uses a
    two pointer solution to the problem. Seems decent.
    Iterates the left pointer until it finds a dot and then it stays there
    until that space has been found. When we notice a new number to check, we
    iterate through all index values to find the left index where we can place
    the string of numbers. At this point we switch it if a match is found, or
    move to the next right index. Uses a list to ensure that a switched number
    does not get switched again.
    """
    left = 0
    right = len(num_list) - 1
    checked_nums = []

    while left < right:

        while num_list[left] != '.':
            # finds the first dot in the list always
            left += 1

        if num_list[right] != '.' and num_list[right] not in checked_nums:
            # the case where we want to check if we can make a switch
            checked_nums.append(num_list[right])
            right_num_length = compute_size(num_list,
                                            right)  # check how many n
            left_return = find_left(num_list, left, right_num_length)

            if left_return == -1:
                # there is no room on the left for right
                right -= right_num_length

            elif left_return > right:
                # there is room on the right but we don't switch those
                right -= right_num_length

            else:
                # there is room on the left for right to switch
                num_list[left_return:left_return + right_num_length] =\
                    num_list[right - right_num_length + 1: right + 1]

                num_list[right - right_num_length + 1: right + 1] =\
                    ['.'] * right_num_length
                # switch left and right
                right -= right_num_length
        else:
            right -= 1

    return num_list


def solve_part_two(file):
    """
    Solves part two and prints the output
    """
    num_list = generate_list(file)

    compressed_list = compress_list_two(num_list)
    checksum_list = [int(num) * i if num != '.' else 0 for i, num in
                     enumerate(compressed_list)]
    print(sum(checksum_list))


if __name__ == '__main__':
    example = 'example.txt'
    real = 'input.txt'

    file = read_file(real)
    # solve_part_one(file)
    solve_part_two(file)

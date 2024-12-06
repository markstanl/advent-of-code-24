"""
--- Day 5: Print Queue ---
Honestly this one probably isn't that inefficient. Everything here is relatively
optimized. The largets glaring issue would likely be the check validity method,
which is O(n^2) in the worst case. But especially the fixing invalid lines,
which I solved recursively to handle some edge cases. Other than that I am
happy with my solution.
"""

def read_file(file_path):
    """
    Converts the file into a list.
    [
        [first_section], # List of pairs [[1, 2], [3, 4], ...]
        [second_section] # List of lines with numbers [[1, 2, 3], [4, 5], [7, 12, 2], ...]
    ]
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    first_section = [
        [int(line.strip().split('|')[0]), int(line.strip().split('|')[1])] for
        line in lines if '|' in line]
    second_section = [[int(num) for num in line.strip().split(',')] for line in
                      lines if
                      '|' not in line and ',' in line]
    return [first_section, second_section]


def populate_dict(first_section):
    """
    Creates a dictionary where the key is the first number in the pair with
    value the list of numbers that should come after it.
    e.g.
    1|2, 1|3, 2|3
    makes
    {
        1: [2, 3],
        2: [3]
    }
    """
    pair_maps = {}
    for pair in first_section:
        if pair[0] not in pair_maps:
            pair_maps[pair[0]] = [pair[1]]
        else:
            pair_maps[pair[0]].append(pair[1])
    return pair_maps


def check_validity(line, map):
    """
    Checks if the line is valid by ensuring no numbers before the current
    number are supposed to come after don't.
    """
    for i, num in enumerate(line):
        if num not in map:
            continue
        after_numbers = map[num]
        for prior_numbers in line[:i]:
            if prior_numbers in after_numbers:
                return False
    return True


def get_center_number(arr):
    """
    prolly didn't need a whole method
    """
    return arr[len(arr) // 2]


def solve_part_one(file):
    """
    Solves the first part and prints the answer
    """
    first_section = file[0]
    second_section = file[1]
    pair_map = populate_dict(first_section)

    valid_lines = []
    for line in second_section:
        if check_validity(line, pair_map):
            valid_lines.append(line)
    print(sum([get_center_number(line) for line in valid_lines]))

def move_value_to_end(arr, value):
    """
    it looks nicer to have these as methods :)
    """
    arr.remove(value)
    arr.append(value)
    return arr


def make_valid(line, map):
    """
    Recursively fixes the line by moving numbers that are in the wrong place to
    the end of the line. This is done until the line is valid. The bubble sort
    of fixing invalid lines. We need to check the line again after moving a
    number to the end because it could have been in the wrong place for OTHER
    numbers.
    """
    any_changes = False
    for i, num in enumerate(line):
        if num not in map:
            continue
        after_numbers = map[num]
        for prior_numbers in line[:i]:
            if prior_numbers in after_numbers:
                line = move_value_to_end(line, prior_numbers)
                any_changes = True
    # wittle recursive case :)
    if any_changes:
        make_valid(line, map)




def solve_part_two(file):
    """
    Solves the second part and prints the answer
    """
    first_section = file[0]
    second_section = file[1]
    pair_map = populate_dict(first_section)

    invalid_fixed_lines = []
    for line in second_section:
        if not check_validity(line, pair_map):
            make_valid(line, pair_map)
            invalid_fixed_lines.append(line)

    print(sum([get_center_number(line) for line in invalid_fixed_lines]))


if __name__ == '__main__':
    example = 'example.txt'
    real = 'input.txt'

    file = read_file(real)
    # solve_part_one(file)
    solve_part_two(file)

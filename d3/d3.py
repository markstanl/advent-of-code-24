def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


def solve_part_one(lines):
    """
    This function solves part one of the problem. I'm sure there is a more 
    elegant way to do this, but I just forcefully find instances of mult(
    and then go from there
    """
    numbers = []
    for line in lines:
        for i in range(3, len(line)):
            if line[i-3:i+1] == 'mul(':
                # populate first number
                first_number = ''
                j = i + 1
                next_char = line[j]
                while next_char.isdigit():
                    first_number += next_char
                    j += 1
                    next_char = line[j]

                # check that the next non-digit character is a comma
                if next_char != ',':
                    continue

                # populate second number
                second_number = ''
                next_char = line[j + 1]
                while next_char.isdigit():
                    second_number += next_char
                    j += 1
                    next_char = line[j + 1]
                if next_char != ')':
                    continue

                numbers.append(int(first_number) * int(second_number))

    print(sum(numbers))


def solve_part_two(lines):
    numbers = []
    do = True
    for line in lines:
        for i in range(3, len(line)):
            if do and i > 2 and line[i-3:i+1] == 'mul(':

                # populate first number
                first_number = ''
                j = i + 1
                next_char = line[j]
                while next_char.isdigit():
                    first_number += next_char
                    j += 1
                    next_char = line[j]

                # check that the next non-digit character is a comma
                if next_char != ',':
                    continue

                # populate second number
                second_number = ''
                next_char = line[j + 1]
                while next_char.isdigit():
                    second_number += next_char
                    j += 1
                    next_char = line[j + 1]
                if next_char != ')':
                    continue

                numbers.append(int(first_number) * int(second_number))
            elif i > 2 and line[i-3:i+1] == 'do()':
                do = True
            elif i > 5 and line[i-6:i+1] == "don't()":
                do = False
    print(sum(numbers))


if __name__ == '__main__':
    real = 'input.txt'
    test = 'example.txt'
    test2 = 'example_two.txt'
    res = read_file(real)
    # solve_part_one(res)
    solve_part_two(res)

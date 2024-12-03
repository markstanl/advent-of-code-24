def read_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    split_lists = [[int(num) for num in line.split()] for line in lines]
    return split_lists


def check_ascend(line):
    for i in range(len(line) - 1):
        if line[i] > line[i + 1]:
            return False
        else:
            if abs(line[i + 1] - line[i]) == 0 or abs(
                    line[i + 1] - line[i]) > 3:
                return False
    return True


def check_descend(line):
    for i in range(len(line) - 1):
        if line[i] < line[i + 1]:
            return False
        else:
            if abs(line[i + 1] - line[i]) == 0 or abs(
                    line[i + 1] - line[i]) > 3:
                return False
    return True


def solve_part_one(split_lists):
    safe_count = 0
    for line in split_lists:
        if line[0] < line[1]:
            safe = check_ascend(line)
            if safe:
                safe_count += 1
            # no need to check equivalent case
        else:
            safe = check_descend(line)
            if safe:
                safe_count += 1
    print(safe_count)


def solve_part_two(split_lists):
    safe_count = 0
    for line in split_lists:
        if line[0] < line[1]:
            safe = check_ascend(line)
            if safe:
                safe_count += 1
            else:
                for i in range(len(line)):
                    new_list = line[:]
                    new_list.pop(i)
                    safe = check_ascend(new_list)
                    if not safe:
                        safe = check_descend(new_list)
                    if safe:
                        safe_count += 1
                        break
            # no need to check equivalent case
        else:
            safe = check_descend(line)
            if safe:
                safe_count += 1
            else:
                for i in range(len(line)):
                    new_list = line[:]
                    new_list.pop(i)
                    safe = check_descend(new_list)
                    if not safe:
                        safe = check_ascend(new_list)
                    if safe:
                        safe_count += 1
                        break
    print(safe_count)


if __name__ == '__main__':
    example = 'example.txt'
    real = 'input.txt'

    res = read_file(real)
    solve_part_one(res)
    solve_part_two(res)

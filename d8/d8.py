def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def solve_part_one(file):
    print('Part one')

def solve_part_two(file):
    print('Part two')


if __name__ == '__main__':
    example = 'example.txt'
    real = 'input.txt'

    file = read_file(example)
    solve_part_one(file)
    solve_part_two(file)
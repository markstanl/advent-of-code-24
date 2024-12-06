"""
--- Day 6: Guard Gallivant ---
You know how every day I say that my solution is a little brute force.
Boy-oh-boy do I have no such exception. The solution to part two is the
LEAST-EFFICIENT-BRUTE-FORCE-SLOW-BLOCK-OF-CODE that I have EVER had the
misfortune of writing. It took 5 MINUTES TO RUN. Nonetheless it works, and we
are here for a good time not a long time amirite?
"""


def read_file(file_path):
    """
    Populates an array
    [
        [grid],
        [guard_coordinates] # (1, 2)
    ]
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    guard_coordinates = ()
    grid = []
    for i, line in enumerate(lines):
        char_line = []
        for j, char in enumerate(line.strip()):
            if char == '^':
                guard_coordinates = (i, j)
            char_line.append(char)
        grid.append(char_line)
    return [grid, guard_coordinates]


def turn_right(direction):
    """
    Gives you the new direction once you turn
    """
    directions = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^'
    }
    return directions[direction]


def print_grid(grid):
    """
    Is this probably a built in python function? Probably. Did I not want to
    look it up? absolutely not
    """
    for line in grid:
        print(''.join(line))


def move_guard(grid, guard_coordinates, direction):
    """
    This method moves the little guy, deals with direction changes, and Xs
    out the space he was once in
    """
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    next_guard_coordinates = (guard_coordinates[0] + directions[direction][0],
                              guard_coordinates[1] + directions[direction][1])

    while (0 <= next_guard_coordinates[0] < len(grid) and
           0 <= next_guard_coordinates[1] < len(grid[0]) and
           # ensures we can check if the next spot is a #
           grid[next_guard_coordinates[0]][next_guard_coordinates[1]] == '#'):
        # checks if the next spot is a hashtag, and deals with the turn
        # has to be in a while loop in case the turn results in another #
        direction = turn_right(direction)
        next_guard_coordinates = (
            guard_coordinates[0] + directions[direction][0],
            guard_coordinates[1] + directions[direction][1])

    # makes the old spot an X
    grid[guard_coordinates[0]][guard_coordinates[1]] = 'X'

    if (0 <= next_guard_coordinates[0] < len(grid) and 0 <=
            next_guard_coordinates[1] < len(grid[0])):
        # checks if the next spot is in the grid and makes it an arrow
        # probably an unnecessary step for anything other than visualizing
        grid[next_guard_coordinates[0]][next_guard_coordinates[1]] = '^'

    return grid, next_guard_coordinates, direction


def count_x(grid):
    """
    Counts the number of Xs in a grid
    """
    x_count = 0
    for line in grid:
        x_count += line.count('X')
    return x_count


def solve_part_one(file):
    """
    Solves and prints the solution to part one
    """
    grid = file[0]
    guard_coordinates = file[1]
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }
    direction = '^'

    while True:
        grid, guard_coordinates, direction = move_guard(grid,
                                                        guard_coordinates,
                                                        direction)
        # moves the gaurd, and saves all new information such as updated
        # direction, coordinates, and grid

        # checks if the gaurd has left
        if len(grid) <= guard_coordinates[0] or guard_coordinates[0] < 0:
            break
        if len(grid[0]) <= guard_coordinates[1] or guard_coordinates[1] < 0:
            break

    print_grid(grid)  # the completed grid for your viewing pleasure
    x_count = count_x(grid)
    print(x_count)


def move_guard_check_for_dupes(grid, guard_coordinates, direction, cor_dir):
    """
    Moves the guard but ALSO checks for any cycles in the pathing. Does so
    through the corr_dir, which is a dict as follows
    {
        (1, 2): ['>', '^'],
        (2, 3): ['<']
    }
    It stores the coordinates of wherever the guard is, and the directions
    it has historically been. If the guard tries to go in a direction it has
    already been, it is in a cycle, and will return true
    """
    if guard_coordinates in cor_dir:
        if direction in cor_dir[guard_coordinates]:
            return grid, guard_coordinates, direction, cor_dir, True
        else:
            cor_dir[guard_coordinates].append(direction)
    else:
        cor_dir[guard_coordinates] = [direction]
    # logic for checking for cycles and updating the coordinate directions dict

    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }
    next_guard_coordinates = (guard_coordinates[0] + directions[direction][0],
                              guard_coordinates[1] + directions[direction][1])

    while (0 <= next_guard_coordinates[0] < len(grid) and
           0 <= next_guard_coordinates[1] < len(grid[0]) and
           grid[next_guard_coordinates[0]][next_guard_coordinates[1]] == '#'):
        # turns the guard right
        direction = turn_right(direction)
        next_guard_coordinates = (
            guard_coordinates[0] + directions[direction][0],
            guard_coordinates[1] + directions[direction][1])

    grid[guard_coordinates[0]][guard_coordinates[1]] = 'X'

    if (0 <= next_guard_coordinates[0] < len(grid) and 0 <=
            next_guard_coordinates[1] < len(grid[0])):
        grid[next_guard_coordinates[0]][next_guard_coordinates[1]] = '^'

    return grid, next_guard_coordinates, direction, cor_dir, False


def solve_part_two(file):
    """
    Solves and prints the solution to part two. Super efficiently, it takes
    negative a million years to run.
    """
    grid = file[0]
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }
    dupe_count = 0

    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            # this iterates through the grid, replaces the . with a wall, and
            # checks if there are duplicates. This makes it like
            # O(n^2 * m^2) which is not ideal

            if char == '.':
                direction = '^'
                guard_coordinates = file[1]
                test_grid = [x[:] for x in grid]
                test_grid[i][j] = '#'
                corr_dir = {}

                while True:
                    test_grid, guard_coordinates, direction, corr_dir, dupe = move_guard_check_for_dupes(
                        test_grid,
                        guard_coordinates,
                        direction,
                        corr_dir)
                    # moves the guard and checks for cycles

                    if dupe:
                        # if there is a cycle, break and add to the dupe count
                        dupe_count += 1
                        break

                    if len(grid) <= guard_coordinates[0] or guard_coordinates[
                        0] < 0:
                        break

                    if len(grid[0]) <= guard_coordinates[1] or \
                            guard_coordinates[1] < 0:
                        break
                    # logic to break out if the guard leaves the grid

    print(dupe_count)


if __name__ == '__main__':
    example = 'example.txt'
    real = 'input.txt'

    file = read_file(example)
    # solve_part_one(file)
    solve_part_two(file)

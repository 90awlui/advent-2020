with open('day01/input.txt','r') as f:
    puzzle_input = f.read().split()
    puzzle_input = [int(n) for n in puzzle_input]

    for num1_index, num1 in enumerate(puzzle_input):
        for num2_index, num2 in enumerate(puzzle_input[num1_index:]):
            if num1 + num2 == 2020: 
                print(f'part1 - num1 {num1}, num2 {num2}, num1*num2 = {num1 * num2}')

    for num1_index, num1 in enumerate(puzzle_input):
        for num2_index, num2 in enumerate(puzzle_input[num1_index:]):
            for num3_index, num3 in enumerate(puzzle_input[num2_index:]):
                if num1 + num2 + num3 == 2020:
                    print(f'part2 - num1 {num1}, num2 {num2}, num3 {num3}, num1*num2*num3 = {num1 * num2 * num3}')

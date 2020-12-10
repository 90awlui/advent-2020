with open('day03/input.txt','r') as f:
    input_list = f.read().split()
    input_dict = {}
    for row_num, row in enumerate(input_list):
        input_dict[row_num+1] = row

    # starting positions
    col_step = int(input("right: "))
    row_step = int(input("down: "))

    # row is 1 index, col is 0 index, confusing, but it works.
    col_index = 0
    row_index = 1
    tree_counter = 0 
    print(len(input_list))
    while row_index < len(input_list):
        row_index += row_step
        col_index += col_step
        print(f"row: {row_index}, column: {col_index%31}, {input_dict[row_index][col_index%31]}")
        if input_dict[row_index][col_index%31] == '#':
            tree_counter += 1    
    
    print(tree_counter)

# Right 1, down 1. - 86
# Right 3, down 1. - 232 
# Right 5, down 1. - 90
# Right 7, down 1. - 71
# Right 1, down 2. - 31
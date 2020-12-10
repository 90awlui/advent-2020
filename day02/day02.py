import re

with open('day02/input.txt','r') as f:
    puzzle_input = f.read().split('\n')
    # part 1 
    valid_pwd = 0
    for row in puzzle_input:
        result = re.findall(r'(\d*)-(\d*)\s(.):\s(.*)',row)[0]
        min_num = int(result[0])
        max_num = int(result[1])
        letter = result[2]
        pwd = result[3]
        
        if pwd.count(letter) >= min_num and pwd.count(letter) <= max_num:
            valid_pwd += 1

    print(f"part 1 - num valid pwd: {valid_pwd}")

    #part 2 
    valid_pwd = 0
    for row in puzzle_input:
        result = re.findall(r'(\d*)-(\d*)\s(.):\s(.*)',row)[0]
        position_1 = int(result[0]) - 1
        position_2 = int(result[1]) - 1
        letter = result[2]
        pwd = result[3]

        if (pwd[position_1] == letter and pwd[position_2] != letter) or (pwd[position_1] != letter and pwd[position_2] == letter):
            valid_pwd += 1

    print(f"part 2 - num valid pwd: {valid_pwd}")
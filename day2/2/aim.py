
with open('input.txt') as f:
    data = []
    for line in f:
        op, num = line.split()
        num = int(num)
        data.append((op.lower(), num))

horizontal_pos = 0
vertical_pos = 0
aim = 0
for movement in data:
    op, num = movement
    match op:
        case 'forward':
            horizontal_pos += num
            vertical_pos += aim * num
        case 'up':
            aim -= num
        case 'down':
            aim += num
        case _: 
            continue

print(horizontal_pos, vertical_pos, horizontal_pos * vertical_pos)

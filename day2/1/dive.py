
with open('input.txt') as f:
    data = []
    for line in f:
        op, num = line.split()
        num = int(num)
        data.append((op.lower(), num))

horizontal_pos = 0
vertical_pos = 0
for movement in data:
    op, num = movement
    match op:
        case 'forward':
            horizontal_pos += num
        case 'up':
            vertical_pos -= num
        case 'down':
            vertical_pos += num
        case _: 
            continue

print(horizontal_pos, vertical_pos, horizontal_pos * vertical_pos)

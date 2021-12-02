with open('input.txt') as f:
    data = [int(line[:-1]) for line in f]

increased_amount = 0
last_value = 1000000000
for entry in data:
    if entry > last_value:
        increased_amount += 1
    last_value = entry

print(increased_amount)

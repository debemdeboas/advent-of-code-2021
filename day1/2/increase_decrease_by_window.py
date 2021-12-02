with open('input.txt') as f:
    data = [int(line[:-1]) for line in f]

entries = []
for index, entry in enumerate(data):
    try:
        entries.append(entry + data[index+1] + data[index+2])
    except:
        break

increased_amount = 0
last_value = 1000000000
for entry in entries:
    if entry > last_value:
        increased_amount += 1
    last_value = entry

print(increased_amount)

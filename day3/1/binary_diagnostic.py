
with open('input.txt') as f:
    data = []
    data = f.readlines()

dic = {}
for i in range(len(data[0]) - 1):
    dic[i] = [0, 0]

for entry in data:
    for i, b in enumerate(entry.strip()):
        dic[i][int(b)] += 1

gamma = ''
epsilon = ''
for _, l in dic.items():
    if l[0] > l[1]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma, epsilon, gamma * epsilon)


with open('input.txt') as f:
    data = []
    data = f.readlines()

def calculate_rating(condition_func, dataset):
    rating = dataset
    for i in range(len(dataset[0]) - 1):
        l = [0, 0]
        for entry in rating:
            if entry[i] == '1':
                l[1] += 1
            else:
                l[0] += 1

        if condition_func(l[0], l[1]):
            rating = list(filter(lambda x: x[i] == '0', rating))
        else:
            rating = list(filter(lambda x: x[i] == '1', rating))

        if len(rating) == 1:
            break

    return rating


# Oxygen
oxygen_rating = calculate_rating(lambda x, y: x > y, data)

# CO2
co2_rating = calculate_rating(lambda x, y: x <= y, data)

oxygen_rating = int(oxygen_rating[0], 2)
co2_rating = int(co2_rating[0], 2)
print(oxygen_rating * co2_rating)

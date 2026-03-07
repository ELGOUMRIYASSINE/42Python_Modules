numbers = [1, 2, 3, 4, 5]


def multi_2(number):
    return number * 2

doubles = list(map(multi_2, numbers))
print(doubles)
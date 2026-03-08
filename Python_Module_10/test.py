numbers = [1, 2, 3, 4, 5]

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]

def multi_2(number):
    return number * 2

# doubles = list(map(lambda x: x * 2, numbers))
# doubles = list(filter(lambda x: x % 2 != 0, numbers))
doubles = list(sorted(students, key=lambda x: x[1]))
print(doubles)
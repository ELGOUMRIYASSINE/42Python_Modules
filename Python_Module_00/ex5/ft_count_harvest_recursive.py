def count_recursive(days, remain):
    if remain <= days:
        print(f"Day {remain}")
        remain += 1
        if remain > days:
            print("Harvest time!")
        count_recursive(days, remain)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    remain = 1
    count_recursive(days, remain)

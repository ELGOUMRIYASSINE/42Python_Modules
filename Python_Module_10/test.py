def show(name, index):
    print(name[index - 1], end="")
    if index == 1:
        return
    show(name, index - 1)

show("Yassine", len("Yassine"))

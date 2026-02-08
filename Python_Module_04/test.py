import os

name = "yassine.txt"
f = open(name, "r")

# fd = f.fileno()

# os.write(fd,b"yassine")
# os.close(fd)
# print(os.name)
# # print("yassine", file=fd)



# print("\nthe file discriptor of %s is %s" % (name, f.fileno))
# print(f"the file discriptor of {name} is {f.fileno()}")

# for i in f:
#     print(i)

v = f.read(0)
print(v)
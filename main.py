def add_color(color_set, num):
    for i in range(num):
        color_set.add(input("Enter colour to add: "))
    return color_set


col_set = {"orange", "yellow", "blue", "purple", "teal"}
print("Current colour set: {}".format(col_set))
x = int(input("Number of colours to be added: "))
add_color(col_set, x)
print("")
print("Items in new colour set: ")
for n in col_set:
    print(n)

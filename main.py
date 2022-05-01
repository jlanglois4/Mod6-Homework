def part_one():
    shopping_list = []

    boolean = True

    while boolean:
        item = input("Enter an item to purchase (NA to end): ")

        if item.upper() != "NA":
            shopping_list.append(item)
        else:
            break

    shopping_list.reverse()
    for item in shopping_list:
        print(item)


def part_two():
    name_list = ["Bob", "Sue", "Craig", "Eric", "Lisa", "Jennifer"]
    boolean = True
    while boolean:
        name = input("Enter a name (NA to stop): ")
        if name.upper() != "NA":
            if name_list.__contains__(name):
                print(f"{name} is in the list.")
            elif not name_list.__contains__(name):
                print(f"{name} is not in the list.")
        else:
            break


check = input("Enter 1 for part one:\n"
              "Enter 2 for part two: ")
if check == '1':
    part_one()
elif check == '2':
    part_two()

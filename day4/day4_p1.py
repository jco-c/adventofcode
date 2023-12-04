from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)


def open_file():
    with open("day4/input.txt") as f:
        return f.readlines()


lines = open_file()

total_points = 0
for line in lines:
    card, numbers = line.split(":")
    winning, own = numbers.split("|")
    winning_list = [int(num) for num in winning.split()]
    own_list = [int(num) for num in own.split()]
    winning_numbers = [num for num in own_list if num in winning_list]
    if winning_numbers:
        total_points += 2 ** (len(winning_numbers) - 1)

print(total_points)

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)


def open_file():
    with open("day4/input.txt") as f:
        return f.readlines()


lines = open_file()

num_of_wins = {}
instances = {}
total_points = 0
for line in lines:
    card, numbers = line.split(":")
    winning, own = numbers.split("|")
    winning_list = [int(num) for num in winning.split()]
    own_list = [int(num) for num in own.split()]
    winning_numbers = [num for num in own_list if num in winning_list]
    card_num = card.split()[1]
    num_of_wins[int(card_num)] = len(winning_numbers)
    instances[int(card_num)] = 1

pp.pprint(num_of_wins)

for card, wins in num_of_wins.items():
    for num_of_instances in range(instances[card]):
        for i in range(wins):
            try:
                instances[card + i + 1] += 1
            except KeyError:
                continue


print(sum(instances.values()))

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)


def read_file():
    with open("day2/input.txt") as f:
        return f.readlines()


lines = read_file()
games = {}
for line in lines:
    (game, content) = line.rstrip().split(":")
    rounds = content.split(";")
    rounds = [round.split(",") for round in rounds]
    colors_in_rounds = []
    for round in rounds:
        colors = {}
        for dices in round:
            (value, color) = dices.lstrip().split(" ")
            colors[color] = int(value)
        colors_in_rounds.append(colors)
    game = int(game.rstrip().lstrip().split()[-1])
    games[game] = colors_in_rounds
pp.pprint(games)

power_of_games = []
for game, rounds in games.items():
    blue_values = (round.get("blue", 0) for round in rounds)
    red_values = (round.get("red", 0) for round in rounds)
    green_values = (round.get("green", 0) for round in rounds)
    blue_max = max(blue_values)
    red_max = max(red_values)
    green_max = max(green_values)
    power_of_games.append(blue_max * red_max * green_max)

print(f"The power of all games is: {sum(power_of_games)}")


def check_colors(round: dict):
    if round.get("blue", 0) > 14:
        return False
    if round.get("green", 0) > 13:
        return False
    if round.get("red", 0) > 12:
        return False
    return True


valid_games = 0
for game, rounds in games.items():
    rounds_bool = []
    for round in rounds:
        rounds_bool.append(check_colors(round))
    if all(rounds_bool):
        valid_games += game
        # print(game)

# print(valid_games)

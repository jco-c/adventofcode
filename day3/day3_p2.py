from dataclasses import dataclass


def load_txt():
    with open("day3/input.txt") as f:
        return f.readlines()


lines = load_txt()

for row, line in enumerate(lines):
    line = "." + line.rstrip() + ".\n"
    lines[row] = line

dots = len(lines) * "." + "\n"
lines.insert(0, dots)
lines.append(dots)


@dataclass
class Number:
    num_str: str
    char_nearby = False
    star = False
    star_row = None
    star_column = None

    def __repr__(self) -> str:
        return f"Number({self.num_str}, {self.star}, row: {self.star_row}, col: {self.star_column})"


def check_neighbors(row, column, lines):
    rel_pos = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    for rel_row, rel_col in rel_pos:
        try:
            char = lines[row + rel_row][column + rel_col]
            if char == "*":
                return (True, row + rel_row, column + rel_col)
        except IndexError:
            continue
    return (False, 0, 0)


numbers: list[Number] = []
for row, line in enumerate(lines):
    for column, char in enumerate(line):
        if char.isdigit():
            if line[column - 1].isdigit():
                numbers[-1].num_str += char
            else:
                numbers.append(Number(char))
            is_star, star_row, star_col = check_neighbors(row, column, lines)
            if is_star:
                numbers[-1].star = True
                numbers[-1].star_row = star_row
                numbers[-1].star_column = star_col

calculated_gears = []
sum_of_ratios = 0
gears = [number for number in numbers if number.star]
print(gears)
for number in gears:
    for number2 in gears:
        if (
            number.star_column == number2.star_column
            and number.star_row == number2.star_row
            and number is not number2
        ):
            if (number, number2) not in calculated_gears:
                print(int(number.num_str) * int(number2.num_str))
                sum_of_ratios += int(number.num_str) * int(number2.num_str)
            calculated_gears.append((number, number2))
            calculated_gears.append((number2, number))

            # gears.remove(number)
            # gears.remove(number2)


print(sum_of_ratios)

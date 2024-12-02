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

    def __repr__(self) -> str:
        return f"Number({self.num_str}, {self.char_nearby})"


def check_neighbors(row, column, lines):
    rel_pos = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    for rel_row, rel_col in rel_pos:
        try:
            char = lines[row + rel_row][column + rel_col]
            if not char.isdigit() and char != ".":
                return True
        except IndexError:
            continue
    return False


numbers: list[Number] = []
for row, line in enumerate(lines):
    for column, char in enumerate(line):
        if char.isdigit():
            if line[column - 1].isdigit():
                numbers[-1].num_str += char
            else:
                numbers.append(Number(char))
            if check_neighbors(row, column, lines):
                numbers[-1].char_nearby = True

numbers_sel = [number for number in numbers if number.char_nearby]
print(sum([int(number.num_str) for number in numbers_sel]))

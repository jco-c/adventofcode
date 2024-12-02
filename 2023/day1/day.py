import re


def get_text():
    with open("day1/input.txt", "r") as f:
        lines = f.readlines()
    return lines


char_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

char_list = list(char_map.keys())

r = re.compile(r"\b(?:%s)\b" % "|".join(char_list))

calibration_values = []
for line in get_text():
    chars = []
    print(r.search(line))

    # for key, val in char_map.items():  # does things in wrong order
    #     if key in line:
    #         chars.append(str(val))
    # for char in line:
    #     try:
    #         int(char)
    #         chars.append(char)
    #     except Exception:
    #         pass

    print(chars)
    calibration_values.append(int("".join([chars[0], chars[-1]])))

print(sum(calibration_values))

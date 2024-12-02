with open("2024/day1/input.txt") as f:
    lines = f.readlines()


def get_nums(line: str) -> tuple[int, int]:
    num1, num2 = line.split()
    return int(num1), int(num2)


def create_new_lists(lines: list[str]) -> tuple[list, list]:
    list_1 = list()
    list_2 = list()

    for line in lines:
        num1, num2 = get_nums(line)
        list_1.append(num1)
        list_2.append(num2)

    list_1.sort()
    list_2.sort()

    return list_1, list_2


def calculate_diffs(list_1: list[int], list_2: list[int]) -> int:
    total_diff = 0
    for num1, num2 in zip(list_1, list_2):
        diff = abs(num2 - num1)
        total_diff += diff

    return total_diff


list1, list2 = create_new_lists(lines)
print(calculate_diffs(list1, list2))

with open("2024/day2/input.txt") as f:
    lines = f.readlines()


def to_num(lines: list[str]) -> list[list[int]]:
    lines_new = []
    for line in lines:
        nums = line.split()
        nums_new = list()
        for num in nums:
            nums_new.append(int(num))
        lines_new.append(nums_new)
    return lines_new


def get_diffs(report: list[int]) -> list[int]:
    diffs = []
    for id, _ in enumerate(report):
        if id != len(report) - 1:
            diffs.append(report[id + 1] - report[id])

    return diffs


def is_safe(diffs: list[int]) -> bool:
    neg = False
    pos = False
    for item in diffs:
        if item == 0:
            return False
        if abs(item) > 3:
            return False
        if item < 0:
            neg = True
        if item > 0:
            pos = True

    if neg and pos:
        return False

    return True


lines_new = to_num(lines)
safe_reports = 0
for line in lines_new:
    if is_safe(get_diffs(line)):
        safe_reports += 1

print(safe_reports)

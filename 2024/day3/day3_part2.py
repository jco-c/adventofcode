import re

f = open("2024/day3/input.txt")
lines = f.readlines()
text = "".join(lines)
match = r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"
test = r"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

results = re.findall(match, text)

print(results)


def filter(expression: list[tuple[str, str, str]]) -> list[str]:
    enabled = True
    enabled_muls = []
    for mul, do, dont in expression:
        if do:
            enabled = True

        if dont:
            enabled = False

        if mul and enabled:
            enabled_muls.append(mul)

    return enabled_muls


def mul(expression: str) -> int:
    num1, num2 = expression.split(sep=",")
    num1 = int(num1[4:])
    num2 = int(num2[:-1])

    return num1 * num2


total = 0
for result in filter(results):
    total += mul(result)

print(total)

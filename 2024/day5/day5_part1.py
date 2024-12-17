from dataclasses import dataclass, field

with open("2024/day5/input.txt") as f:
    lines = f.readlines()


@dataclass
class Rule:
    current_number: int
    numbers_before: list[int] = field(default_factory=list)
    numbers_after: list[int] = field(default_factory=list)


@dataclass
class PrintJob:
    _middle_page: int | None = None
    page_numbers: list[int] = field(default_factory=list)
    is_correct: bool = False

    @property
    def middle_page(self):
        if self._middle_page is None:
            self._middle_page = self.page_numbers[int((len(self.page_numbers) - 1) / 2)]
        return self._middle_page

    def check_if_correct(self, rules: dict[int, Rule]) -> bool:
        is_correct: list[bool] = []

        for idx, page_number in enumerate(self.page_numbers):
            current_rule = rules.get(page_number)
            if not current_rule:
                is_correct.append(True)
                continue
            is_disjoint_before = set(current_rule.numbers_before).isdisjoint(
                set(self.page_numbers[idx:])
            )
            is_disjoint_after = set(current_rule.numbers_after).isdisjoint(
                set(self.page_numbers[:idx])
            )
            if is_disjoint_before and is_disjoint_after:
                is_correct.append(True)
            else:
                is_correct.append(False)

        if all(is_correct):
            self.is_correct = True
            return True
        else:
            self.is_correct = False
            return False


rules: dict[int, Rule] = {}
printjobs: list[PrintJob] = []


def add_rule(text_input: str):
    first_number, second_number = text_input.split(sep="|")
    first_number = int(first_number)
    second_number = int(second_number)

    if first_number not in rules:
        rules[first_number] = Rule(current_number=first_number)
    rules[first_number].numbers_after.append(second_number)

    if second_number not in rules:
        rules[second_number] = Rule(current_number=second_number)
    rules[second_number].numbers_before.append(first_number)


def add_print_job(text_input: str):
    pages = text_input.split(",")
    printjobs.append(
        PrintJob(
            page_numbers=[int(page_num) for page_num in pages],
        )
    )


for line in lines:
    if "|" in line:
        add_rule(line)
    elif "," in line:
        add_print_job(line)

sum_middle_pages = 0

for printjob in printjobs:
    if printjob.check_if_correct(rules):
        sum_middle_pages += printjob.middle_page

print(sum_middle_pages)
print(len(rules))

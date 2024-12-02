from dataclasses import dataclass


def read_txt():
    with open("day8/input.txt", "r") as f:
        return f.readlines()


@dataclass
class Node:
    name: str
    L: str
    R: str


def get_next_node(current_node: Node, direction):
    if direction == "L":
        return current_node.L
    if direction == "R":
        return current_node.R


def find_zzz(
    nodes: dict[str, Node],
    direction_generator,
):
    node = nodes["AAA"]
    steps = 0
    while node.name != "ZZZ":
        direction = next(direction_generator)
        node = nodes[get_next_node(node, direction)]
        steps += 1
    return steps


def get_direction(direction_sequence: str):
    for direction in direction_sequence.rstrip() * 100:
        yield direction
        direction_sequence += direction


def main():
    lines = read_txt()
    instructions = lines[0].rstrip()
    gen = get_direction(instructions)
    nodes = {}
    for line in lines[2:]:
        name, lr = line.split("=")
        left, right = lr.replace("(", "").replace(")", "").split(",")
        nodes[name.strip()] = Node(name.strip(), left.strip(), right.strip())
    print(find_zzz(nodes, gen))


if __name__ == "__main__":
    main()

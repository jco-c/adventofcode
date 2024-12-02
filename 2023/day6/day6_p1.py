def get_text():
    with open("day6/input.txt") as f:
        return f.readlines()


# distance = (time_total - time_charging) * 1 m * time_charging / s


def calc_distance(total_time, charging_time):
    return (total_time - charging_time) * charging_time


def get_valid_runs(total_time, record_distance):
    valid_runs = []
    for charging_time in range(total_time):
        distance = calc_distance(total_time, charging_time)
        if distance > record_distance:
            valid_runs.append(charging_time)
        if valid_runs and distance <= record_distance:
            break

    return valid_runs


def get_input_from_text(lines):
    total_times = [int(num) for num in lines[0].rstrip().split()[1:]]
    record_distances = [int(num) for num in lines[1].rstrip().split()[1:]]
    return (total_times, record_distances)


def main():
    lines = get_text()
    total_times, record_distances = get_input_from_text(lines)
    possible_runs = []
    for total_time, record_distance in zip(total_times, record_distances):
        valid_runs = get_valid_runs(total_time, record_distance)
        possible_runs.append(len(valid_runs))

    combinations = 1
    for run in possible_runs:
        combinations *= run

    print(combinations)


if __name__ == "__main__":
    main()

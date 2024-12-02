def get_differences_line(input: list[int]) -> list[int]:
    output = []
    for idx, item in enumerate(input):
        # print(item)
        if idx == len(input) - 1:
            break
        output.append(input[idx + 1] - item)
    return output


def get_all_differences(source_line: list[int]) -> list[list[int]]:
    differences = [source_line]
    while any(differences[-1]):
        differences.append(get_differences_line(differences[-1]))
    return differences


def get_prediction(differences: list[list[int]]):
    predicted = []
    differences.reverse()
    for idx, row in enumerate(differences):
        # print(row)
        if idx == 0:
            row.append(0)
            predicted.append(row)
        else:
            row.append(row[-1] + predicted[-1][-1])
            predicted.append(row)

    predicted.reverse()
    return predicted


def main():
    lines = open("day9/input.txt").readlines()
    measurements = []
    for line in lines:
        numbers = [int(num) for num in line.split()]
        measurements.append(get_all_differences(numbers))
    # print(measurements)
    predictions = []
    for measurement in measurements:
        predictions.append(get_prediction(measurement))
    prediction_sum = 0
    for prediction in predictions:
        prediction_sum += prediction[0][-1]

    print(prediction_sum)


if __name__ == "__main__":
    main()

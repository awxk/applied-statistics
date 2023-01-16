import matplotlib.pyplot as plt

def calculate_relative_frequency(numbers=None):
    if numbers is None:
        numbers = list(
            map(int, input("Enter numbers separated by commas: ").split(",")))

    total_numbers = sum(numbers)

    precision = int(input("Enter the desired precision: "))

    relative_frequencies = {}
    for number in numbers:
        relative_frequency = round(number / total_numbers, precision)
        relative_frequencies[number] = relative_frequency

    # Generate pie chart of relative frequencies
    plt.pie(list(relative_frequencies.values()),
            labels=list(relative_frequencies.keys()))
    plt.show()

    return relative_frequencies

print(calculate_relative_frequency())

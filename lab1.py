import random
import statistics
import numpy as np
from numpy.linalg import matrix_power


# Q1
def find_pairs_sum_ten(values):
    count = 0
    n = len(values)
    for i in range(n):
        for j in range(i + 1, n):
            if values[i] + values[j] == 10:
                count += 1
    return count


# Q2
def compute_range_real_list():
    while True:
        try:
            n = int(input("Enter size of list (>3): "))
            if n <= 3:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Size must be greater than 3.")

    numbers = []
    for i in range(n):
        while True:
            try:
                num = float(input(f"Enter element {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Enter a real number.")

    return max(numbers) - min(numbers)


# Q3
def calculate_matrix_power(mat, power_val):
    while True:
        try:
            if power_val <= 0:
                raise ValueError
            return matrix_power(mat, power_val)
        except ValueError:
            power_val = int(input("Enter a positive power: "))


# Q4
def most_frequent_character(text):
    if text == "":
        return None, 0

    characters = set(text)
    highest_count = 0
    highest_char = ""

    for ch in characters:
        cnt = text.count(ch)
        if cnt > highest_count:
            highest_count = cnt
            highest_char = ch

    return highest_char, highest_count


# Q5
def generate_random_statistics():
    size = 25
    min_val = 1
    max_val = 10

    numbers = [random.randint(min_val, max_val) for _ in range(size)]
    numbers.sort()

    mean = sum(numbers) / size
    median = statistics.median(numbers)
    mode = statistics.multimode(numbers)

    return numbers, mean, median, mode


def run_lab_program():


    lst = list(map(int, input("Enter integers separated by space: ").split()))
    print("Pairs with sum 10:", find_pairs_sum_ten(lst))

    print("\nRange of real numbers:", compute_range_real_list())

    A = np.array([[1, 2], [3, 4]])
    power = int(input("\nEnter power for matrix: "))
    print("Matrix result:\n", calculate_matrix_power(A, power))

    s = input("\nEnter a string: ")
    ch, cnt = most_frequent_character(s)
    if ch is not None:
        print(f"Highest occurring character: '{ch}' ({cnt} times)")
    else:
        print("Empty string entered.")

    nums, mean, median, mode = generate_random_statistics()
    print("\nRandom Numbers:", nums)
    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)


if _name_ == "_main_":
    run_lab_program()

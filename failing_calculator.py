def average_ratios(numbers):
    total = 0
    for i in range(len(numbers)):
        total += 100 / numbers[i] 
    return total / len(numbers)

print(average_ratios([10, 5, 0]))
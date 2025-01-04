def find_missing_numbers(arr):
    missing_numbers = []
    for number in range (max(arr)):
        if number not in arr:
            missing_numbers.append(number)
            
    return missing_numbers

numbers = [1, 2, 3, 5, 6, 7, 8, 10, 12]
print(find_missing_numbers(numbers))
            
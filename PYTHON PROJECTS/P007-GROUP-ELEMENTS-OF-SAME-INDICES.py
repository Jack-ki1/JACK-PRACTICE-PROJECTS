def group_same_indices(arr):
    result = []
    
    for element in range (len(arr[0])):
        result.append([])
        for number in range (len(arr)):
            result[element].append(arr[number][element])
            
    return result

numbers = [[10,20,30], [40,50,60], [70,80,90]]
print(*group_same_indices(numbers))
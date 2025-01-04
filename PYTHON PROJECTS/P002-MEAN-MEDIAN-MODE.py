from collections import defaultdict
#class defaultdict is used to create a dictionary_like object that returns a default value when a key is not found
dataset = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

mean = sum(dataset) / len(dataset)#len() function gikves the length of the list (number of items in the list)
print(f"Mean is: {mean}")

sorted_dataset = sorted(dataset)#the sorted() function returns a new list the items arranged in ascending order

if len(dataset) % 2 == 0:#checks if the length of dataset list(number of elements) is even. If remainder is 0 then the length of list is even 
    middle = len(sorted_dataset) // 2#calculates the middle  index of the sorted_dataset list
    left_number = sorted_dataset[middle - 1]#assigns the value at the middle index (minus 1 to account for 0-based indexing )
    right_number = sorted_dataset[middle]#assigns the value  at the middle index to the variable right_nuumber 
    total = (left_number + right_number) // 2 #calculates average of the two and stores it in the variable total
    print(f"Even number of elements median: {total}") 
else:#executes length of dataset if list  has an odd number of elements 
    median = len(sorted_dataset) // 2 #calculates the middle index of the sorted_dataset similar to the case in the even number 
    print(f"Odd number of elements median: {sorted_dataset[median]}")
    
result = defaultdict(lambda: 1)#creates a dictionary named result using the defaultdict class.In this case, the default value is set to 1
for num in dataset:#iterates through each number in dataset list 
    result[num] += 1# increments the count of each number
    
print(f"Mode is: {[k for k in result if result[k] == max(result.values())][0]}")
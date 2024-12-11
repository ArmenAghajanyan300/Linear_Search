def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1


# Example usage
array = [10, 20, 30, 40, 50]
target = int(input("Enter the number to search: "))

index = linear_search(array, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")

def binary_search(sorted_list, target):
    """
    Perform binary search on a sorted list
    Returns the index if found, -1 if not found
    """
    left = 0
    right = len(sorted_list) - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        if sorted_list[middle] == target:
            return middle
        elif sorted_list[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    
    return -1  # Target not found

# Example usage
if __name__ == "__main__":
    numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = int(input("Enter number to search: "))
    
    result = binary_search(numbers, target)
    
    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found in the list")
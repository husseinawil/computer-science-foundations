# Searching Algorithms: Linear Search vs. Binary Search

def linear_search(arr, target):
    """O(n) time complexity - Unsorted array search."""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    """O(log n) time complexity - Requires sorted array input."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    dataset = [12, 24, 32, 45, 57, 68, 79, 91, 105]
    target_val = 68

    print(f"Dataset (Sorted): {dataset}")
    print(f"Target Value: {target_val}\n")

    lin_idx = linear_search(dataset, target_val)
    print(f"Linear Search Index: {lin_idx} | Complexity: O(n)")

    bin_idx = binary_search(dataset, target_val)
    print(f"Binary Search Index: {bin_idx} | Complexity: O(log n)")

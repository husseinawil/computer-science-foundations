# Sorting Algorithms: Bubble Sort vs. Quick Sort

def bubble_sort(arr):
    """O(n^2) Quadratic Time Complexity - Comparison-based swap."""
    data = arr.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def quick_sort(arr):
    """O(n log n) Average Time Complexity - Divide and Conquer."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    unsorted = [64, 34, 25, 12, 22, 11, 90]
    print(f"Unsorted Input: {unsorted}\n")
    
    bubble_res = bubble_sort(unsorted)
    print(f"Bubble Sort O(n^2): {bubble_res}")
    
    quick_res = quick_sort(unsorted)
    print(f"Quick Sort O(n log n): {quick_res}")

# Array & Linear Memory Operations Demonstration

def demonstrate_array_operations():
    # Contiguous memory block simulation
    arr = [10, 20, 30, 40, 50]
    print(f"Initial Array: {arr}")

    # O(1) Index Lookup
    first_element = arr[0]
    print(f"O(1) Access at Index 0: {first_element}")

    # O(n) Linear Search
    target = 40
    found_idx = -1
    for i in range(len(arr)):
        if arr[i] == target:
            found_idx = i
            break
    print(f"O(n) Search for value {target}: Found at Index {found_idx}")

    # O(n) Insertion (Shifting elements)
    arr.insert(2, 25)
    print(f"O(n) Insert 25 at Index 2 (Shifting): {arr}")

    # O(1) Append (Amortized)
    arr.append(60)
    print(f"O(1) Append 60 at End: {arr}")

if __name__ == "__main__":
    demonstrate_array_operations()

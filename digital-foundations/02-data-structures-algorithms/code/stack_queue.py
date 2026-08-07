# Stack (LIFO) and Queue (FIFO) Implementation

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

if __name__ == "__main__":
    # Stack Execution (LIFO)
    s = Stack()
    s.push("Page 1")
    s.push("Page 2")
    s.push("Page 3")
    print(f"Stack Pop (LIFO - expect Page 3): {s.pop()}")

    # Queue Execution (FIFO)
    q = Queue()
    q.enqueue("Task 1")
    q.enqueue("Task 2")
    q.enqueue("Task 3")
    print(f"Queue Dequeue (FIFO - expect Task 1): {q.dequeue()}")

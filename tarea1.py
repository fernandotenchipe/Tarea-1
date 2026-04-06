from collections import deque

# ===== STACK (LIFO) =====
class Stack:
    def __init__(self):
        self.data = deque()

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop() if self.data else None

    def peek(self):
        return self.data[-1] if self.data else None

    def isEmpty(self):
        return len(self.data) == 0


# ===== QUEUE (FIFO) =====
class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, x):
        self.data.append(x)

    def dequeue(self):
        return self.data.popleft() if self.data else None

    def front(self):
        return self.data[0] if self.data else None

    def isEmpty(self):
        return len(self.data) == 0


# ===== HASH / DICTIONARY =====
class HashTable:
    def __init__(self):
        self.data = {}

    def put(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key, None)

    def delete(self, key):
        if key in self.data:
            del self.data[key]

    def contains(self, key):
        return key in self.data


# ===== PROGRAMA DE PRUEBA =====
def main():
    print("=== STACK ===")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Pop:", stack.pop())      # 30
    print("Peek:", stack.peek())    # 20

    print("\n=== QUEUE ===")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Dequeue:", queue.dequeue())  # 1
    print("Front:", queue.front())      # 2

    print("\n=== HASH ===")
    hash_table = HashTable()
    hash_table.put("a", 100)
    hash_table.put("b", 200)
    print("Get a:", hash_table.get("a"))     # 100
    print("Contains b:", hash_table.contains("b"))  # True
    hash_table.delete("b")
    print("Contains b:", hash_table.contains("b"))  # False


if __name__ == "__main__":
    main()
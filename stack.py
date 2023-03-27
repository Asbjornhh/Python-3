class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def is_full(self):
        return len(self.items) != 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __str__(self):
        return str(self.items)


if __name__== "__main__":

    s = Stack()
    print(s.is_empty())
    s.push(1)
    s.push(2)
    print(s)
    print(s.pop())
    print(s)
    print(s.is_full())
    print(s.is_empty())

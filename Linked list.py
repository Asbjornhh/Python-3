class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_infront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove_from_beginning(self):
        if self.head is None:
            print("Cannot remove because the list is empty")
            return
        self.head = self.head.next

    def remove_from_end(self):
        if self.head is None:
            print("Cannot remove because the list is empty")
            return
        if self.head.next is None:
            self.head = None
            return



    def display_list(self):
        if self.head is None:
            print("The list is empty, please add to the list")
        else:
            values = []
            current = self.head
            while current is not None:
                values.append(current.data)
                current = current.next
            print("Current list: ", values)


my_list = LinkedList()

while True:
    print("\nLinked List Operations")
    print("1. Add to beginning")
    print("2. Add to end")
    print("3. Remove from beginning")
    print("4. Remove from end")
    print("5. Display list")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data to add to beginning: "))
        my_list.add_infront(data)
    elif choice == 2:
        data = int(input("Enter data to add to end: "))
        my_list.add_end(data)
    elif choice == 3:
        my_list.remove_from_beginning()
    elif choice == 4:
        my_list.remove_from_end()
    elif choice == 5:
        my_list.display_list()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Try again.")

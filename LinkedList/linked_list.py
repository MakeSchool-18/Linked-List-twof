
class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linked_List:
    def __init__(self, arr=None):
        self.count = 0
        self.head = None
        self.tail = None

        if arr is not None:
            for item in arr:
                self.append(item)

    def append(self, data):
        new_node = Node(data, None)
        if self.count == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def prepend(self, data):
        new_node = Node(data, None)
        if self.count == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.count += 1

    # This is really dirty and needs to be cleaned up
    def delete(self, data):
        found = False

        if self.count == 0:
            raise ValueError
        else:
            current_node = self.head

            while current_node.next is not None:
                if current_node.data == data:
                    found = True
                    break
                elif current_node.next.data == data:
                    found = True
                    break
                else:
                    current_node = current_node.next
                    continue

            if found and current_node.next == self.tail:
                self.tail = current_node
                self.count -= 1
            elif found and current_node == self.head:
                self.head = current_node.next
                self.count -= 1
            elif found:
                self.count -= 1

            if self.count == 0:
                self.head = None
                self.tail = None
                return

            if not found:
                raise ValueError
            elif current_node.next.next is not None:
                current_node.next = current_node.next.next
                print("not none")
            elif current_node.next.next is None:
                self.tail = current_node
                print("none")

    def find(self, filter_func):
        if self.count == 0:
            return None
        else:
            current_node = self.head

        while current_node.next is not None:
            if filter_func(current_node.data):
                return current_node.data
            elif filter_func(current_node.next.data):
                return current_node.next.data
            else:
                current_node = current_node.next
                continue

        return None

    def as_list(self):
        listed = []
        if self.count == 0:
            return listed
        else:
            current_node = self.head
            listed += current_node.data
            while current_node.next is not None:
                listed += current_node.next.data
                current_node = current_node.next
            return listed

    def print_list(self):
        if self.count == 0:
            return
        else:
            print(self.head.data)
            current_node = self.head
            while current_node.next is not None:
                print(current_node.next.data)
                current_node = current_node.next

    def length(self):
        return self.count

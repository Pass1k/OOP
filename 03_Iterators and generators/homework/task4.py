class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        current = self.head
        for i in range(index):
            if current.next:
                current = current.next
            else:
                raise IndexError('Index out of range')
        return current.data

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                if current.next:
                    current = current.next
                else:
                    raise IndexError('Index out of range')
            if current.next:
                current.next = current.next.next
            else:
                raise IndexError('Index out of range')

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return '[' + ' '.join(result) + ']'

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)


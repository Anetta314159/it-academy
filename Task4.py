'''
Задача 4:
Реализуйте двусвязный список используя синтаксис языка Python.
Вам необходимо создать класс (либо несколько классов),
который (которые) будет (будут) представлять структуру данных - связный список.
Связный список — это набор элементов данных, называемых узлами.
В односвязном списке каждый узел содержит значение и ссылку на следующий узел.
В двусвязном списке каждый узел также содержит ссылку на предыдущий узел.
Реализуйте узел для хранения значения и указателей на следующий и предыдущий узлы.
Затем реализуйте список, который содержит ссылки на первый и последний узел
и предлагает интерфейс, подобный массиву, для добавления и удаления элементов,
какие методы должны быть реализованы:
push() - записывает значение в конец списка
pop() - удаляет значение с конца списка
shift() - удаляет значение в начале списка
unshift() - записывает значение в начало списка
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        '''
        записывает значение в конец списка
        '''
        temp = Node(data)
        if self.head is None:
            self.head = self.tail = temp
        else:
            temp.previous = self.tail
            self.tail.next = temp
            self.tail = temp

    def pop(self):
        '''
        удаляет значение с конца списка
        '''
        if self.head is None:
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        return data

    def shift(self):
        '''
        удаляет значение в начале списка
        '''
        if self.head is None:
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        return data

    def unshift(self, data):
        '''
        записывает значение в начало списка
        '''
        temp = Node(data)
        if self.head is None:
            self.head = self.tail = temp
        else:
            temp.next = self.head
            self.head.previous = temp
            self.head = temp

    def show(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

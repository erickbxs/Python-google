from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila está vazia")
        return self.queue.pop(0)

    def search(self, index):
        if 0 <= index < len(self.queue):
            return self.queue[index]
        raise IndexError("Índice Inválido ou Inexistente")

    def is_empty(self):
        return len(self.queue) == 0

from node import Node
# sequencial = []
# sequencial.append(7)


class ListaEncadeada:
    def __init__(self):
        self.head = None # cabeça
        self._size = 0 # conta elementos


    def append(self, data):
        novo_node = Node(data)
        if not self.head:  # Lista vazia
            self.head = novo_node
        else:              # Lista com elementos
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = novo_node
        self._size += 1
        
        def __len__(self):
            # retorna o tamanho da lista
            return self._size
        
        def get(self, index):
            pass

        def set(self, index, data):
            pass
        def __getitem__(self, index):
            pointer = self.head
            for i in range(index):
                if pointer:
                    pointer = pointer.next
                else:
                    raise IndexError("list index out of range")
            if pointer:
                return pointer.data
            else:
                raise IndexError("list index out of range")        
        def __setitem__(self, index, data):
            # lista[6] = 10
            pointer = self.head
            for i in range(index):
                if pointer:
                    pointer = pointer.next
                else:
                    raise IndexError("list index out of range")
            if pointer:
                pointer.data = novo_node
            else:
                raise IndexError("list index out of range") 


lista = ListaEncadeada()
lista.append(10) # adiconar um elemento
print ("elementos na sua lista:", lista._size ) # Teste


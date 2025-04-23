from node import Node
# sequencial = []
# sequencial.append(7)
# Criando uma Classe para a lista encadeada
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
            # lista.get (6)
            pass
            
        def set(self, index, data):
            # lista.set(6, 10)
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
                pointer.data = data
            else:
                raise IndexError("list index out of range")
        
        # Busca linear
        def index(self, data):
            """Retona o indice do elemento na lista"""
            # lista.index(10)
            pointer = self.head
            i = 0
            while (pointer):
                if pointer.data == data:
                    return i
                pointer = pointer.next
            raise ValueError(f"{data} is not in list")


lista = ListaEncadeada()
lista.append(10) # adiconar um elemento
print ("elementos na sua lista:", lista._size ) # Teste

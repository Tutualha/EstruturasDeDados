from node import Node
# sequencial = []
# sequencial.append(7)


class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.size = 0


    def append(self, element):
        if self.head:
            # inserção de quando a lista ja tem elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            # primeira inserção
            self.head = Node(element)
        self.size = self.size + 1 

lista = ListaEncadeada()
lista.append(7)


# Feito com IA para entendimento do que estou fazendo
"""from node import Node

class ListaEncadeada:
    def __init__(self):  # Corrigido o nome do método (faltava um '_')
        self.head = None
        self.size = 0

    def append(self, element):
        # Inserção quando a lista está vazia
        if self.head is None:
            self.head = Node(element)
        else:
            # Percorre a lista até o último elemento
            pointer = self.head
            while pointer.next:  # Parenteses desnecessários removidos
                pointer = pointer.next
            pointer.next = Node(element)
        self.size += 1  # Forma simplificada de incremento

    def __repr__(self):
        items = []
        pointer = self.head
        while pointer:
            items.append(str(pointer.data))
            pointer = pointer.next
        return "[" + " -> ".join(items) + "]"

# Teste da lista
if __name__ == "__main__":
    lista = ListaEncadeada()
    lista.append(7)
    lista.append(12)
    lista.append(5)
    print(lista)  # Saída: [7 -> 12 -> 5]
    print("Tamanho da lista:", lista.size)  # Deve mostrar 3"""

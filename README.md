# EstruturasDeDados
Repositório para estudo de listas encadeadas, listas ordenadas e árvores binárias em Python e C+

Para Começar precisamos entender o que é uma lista ordenadas, encadeada e uma arvore binaria.


apostila para comandos de lista e manipulação de dados em python:
[Apostila Collab com Comando de python](https://colab.research.google.com/drive/1OPTb05wEx_ZismDnQayHkC3HCFNdMw1K?usp=sharing) 



## Listas Encadeadas (Linked Lists)
**O que é uma lista encadeada?**

Uma estrutura de dados linear onde cada elemento (chamado nó) contém:
Um valor (dado)
Um ponteiro para o próximo nó na sequência

Analogia:
Imagine uma corrente formada por elos individuais, onde cada elo sabe apenas onde está o próximo elo, mas não conhece toda a cadeia.

Este tipo de lista normalmente é usado em:

* Gerenciamento de histórico de comandos em editores de texto

* Sistemas de cache em navegadores web

* Implementação de filas e pilhas dinâmicas

## Como funciona a lista encadeda em python
Primeiro temos que montar sua estrutura com o seguintes codigos.


Primeiro vamos criar o node.py que é exatamente o nó:
~~~
class Node:
    def __init__(self, data):
        # Armazenar dados
        self.data = data
        # Aponta o proximo nó (ponteiro)
        self.next = None
~~~
Depois vamos criar a parte principal da estrutura da lista encadeada:
~~~
class ListaEncadeada:
    def __init__(self):
        self.head = None # cabeça
        self.size = 0 # conta elementos
~~~~
Essa parte do codigo cria um novo nó e caso a lista esteja vazia esse novo nó se torna a cabeça:
```
    novo_node = Node(data)
    if not self.head:  # Lista vazia
        self.head = novo_node
...
```

caso nao esteja vazia:

```
...
 else:              # Lista com elementos
        atual = self.head
        while atual.next:
            atual = atual.next
        atual.next = novo_node
    self.size += 1
```

ela vai percorrer o ultimo nó ate que next seja None
e faz a ligação do novo no com o ultimo
e o `self.size` incrementa no contador



# Referencia
[![Estrutura de Dados - Construindo uma Lista Encadedada](https://i.ytimg.com/an_webp/jIM87UqOq3g/mqdefault_6s.webp?du=3000&sqp=CPig574G&rs=AOn4CLD4hrvb8MdNcjbjbp02hNSBzhr_UA)](https://www.youtube.com/embed/jIM87UqOq3g?si=h5vkES8pPcrSLjCB)

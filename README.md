# Estruturas de Dados  

Repositório para estudo de listas encadeadas, listas ordenadas e árvores binárias em **Python** e **JavaScript**.

Para começar, precisamos entender o conceito de cada estrutura que vamos trabalhar.

---

## 📋 Listas Ordenadas  

Lista ordenada é uma estrutura de dados que armazena elementos em uma ordem definida, que pode ser alfabética (de A a Z), crescente, decrescente, entre outras.  
A forma de ordenação depende de como você deseja organizar os elementos e dos critérios estabelecidos para essa ordenação.

### ✅ Como criar uma lista?  

No Python, é bem simples. Você pode tanto usar a função `list()`:

```python
list(("elemento", "elemento1", "elemento2", ...))
```

Ou usar colchetes `[]`:

```python
lista = ["elemento", "elemento1", "elemento2", ...]
```

Assim se cria uma lista de dados em Python.

### 🔃 E pra **ordenar** essa lista?

Confira uma apostila com comandos úteis para manipulação de listas em Python:  
📘 [Apostila Collab com comandos de Python](https://colab.research.google.com/drive/1OPTb05wEx_ZismDnQayHkC3HCFNdMw1K?usp=sharing)

---

## 🔗 Listas Encadeadas (Linked Lists)  

### O que é uma lista encadeada?

Uma estrutura de dados linear onde cada elemento (chamado **nó**) contém:  
- Um valor (dado)  
- Um ponteiro para o próximo nó na sequência  

**💡 Analogia:**  
Imagine uma corrente formada por elos individuais. Cada elo sabe apenas onde está o próximo, mas não conhece a cadeia toda.

Listas encadeadas são comumente usadas em:  
- Gerenciamento de histórico em editores de texto  
- Sistemas de cache de navegadores  
- Implementação de filas e pilhas dinâmicas  

---

## 🛠 Como funciona a lista encadeada em Python?

### 1️⃣ Criando o nó (`node.py`):

```python
class Node:
    def __init__(self, data):
        # Armazena o dado
        self.data = data
        # Aponta para o próximo nó
        self.next = None
```

### 2️⃣ Criando a estrutura da lista encadeada:

```python
class ListaEncadeada:
    def __init__(self):
        self.head = None  # Cabeça da lista
        self.size = 0     # Conta os elementos
```

### 3️⃣ Inserindo elementos:

```python
novo_node = Node(data)
if not self.head:  # Lista vazia
    self.head = novo_node
else:  # Lista com elementos
    atual = self.head
    while atual.next:
        atual = atual.next
    atual.next = novo_node

self.size += 1  # Incrementa o contador
```

Esse código percorre até o último nó (onde `next` é `None`), faz a ligação com o novo nó e atualiza o tamanho da lista.

---

## 🎥 Referência em vídeo  

[Clique para assistir no YouTube](https://www.youtube.com/embed/jIM87UqOq3g?si=h5vkES8pPcrSLjCB)  
[![Estrutura de Dados - Construindo uma Lista Encadeada](https://i.ytimg.com/an_webp/jIM87UqOq3g/mqdefault_6s.webp?du=3000&sqp=CPig574G&rs=AOn4CLD4hrvb8MdNcjbjbp02hNSBzhr_UA)](https://www.youtube.com/embed/jIM87UqOq3g?si=h5vkES8pPcrSLjCB)

---

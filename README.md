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
Ordenar uma lista em Python é muito simples graças às funções nativas `sort()` e `sorted()`, porém, o correto para se ORDENAR é `sort()`.

---

## 📌 Diferença entre `sort()` e `sorted()`

| Função     | Tipo de ordenação     | Modifica a lista original? | Retorna nova lista? |
|------------|------------------------|-----------------------------|----------------------|
| `sort()`   | Ordenação **in-place** | ✅ Sim                      | ❌ Não               |
| `sorted()` | Ordenação pura         | ❌ Não                      | ✅ Sim               |

---

## ✅ Usando `sort()`

A função `sort()` **ordena a própria lista**, ou seja, modifica o conteúdo original.
```python
lista = [5, 2, 9, 1]
lista.sort()
print(lista)  # Saída: [1, 2, 5, 9]
```
tambem é possível ordenar em ordem decrescente:
```python
lista = [5, 2, 9, 1]
lista.sort(reverse=True)
print(lista)  # Saída: [9, 5, 2, 1]
```
---
## ✅ Usando `sorted()`
A função `sorted()` **não modifica a lista original**, mas retorna uma nova lista ordenada.
```python
lista = [5, 2, 9, 1]
lista_ordenada = sorted(lista)
print(lista_ordenada)  # Saída: [1, 2, 5, 9]
print(lista)  # Saída: [5, 2, 9, 1]
```
tambem é possível ordenar em ordem decrescente:
```python
lista = [5, 2, 9, 1]
lista_ordenada = sorted(lista, reverse=True)
print(lista_ordenada)  # Saída: [9, 5, 2, 1]
print(lista)  # Saída: [5, 2, 9, 1]
```

Por fim, você deve entender que nem sempre a lista vai ser ordenada de forma correta, em alguns casos você tera que criar funções situacionais. Por exemplo ordernar uma lista de datas no padrão brasileiro (dd/mm/aaaa) ou americano (mm/dd/aaaa).
```python
from datetime import datetime
lista = ["01/02/2023", "03/04/2022", "05/06/2021"]

lista_ordenada = sorted(lista, key=lambda x: 

datetime.strptime(x, "%d/%m/%Y"))

print(lista_ordenada)  # Saída: ['05/06/2021', '03/04/2022', '01/02/2023']
```


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

let lista = ['Olá', 'Mundo', 'Ola Mundo', 1, 2, 3, 'Javascript', 'lista', 'ordenada', 'elemento'];
lista.sort();


let lista_de_dados = [{ nome: 'Lucas', idade: 20, cidade: 'São Paulo' },
{ nome: 'Ana', idade: 25, cidade: 'Rio de Janeiro' },
{ nome: 'Carlos', idade: 30, cidade: 'Belo Horizonte' },
{ nome: 'Julius', idade: 46, cidade: 'Brasilia' },
{ nome: 'Charles', idade: 22, cidade: 'Pernambuco' },];

lista_de_dados.sort(function (a, b) {
    if (a.nome > b.nome) {
        return 1;
    }
    if (a.nome < b.nome) {
        return -1;
    }
    return 0;
});

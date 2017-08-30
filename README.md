# Sistemas de equações lineares:
Programas para resolver sistemas de equações lineares, conteúdo:

* Gauss Jordan
O processo é realizado em algumas etapas, sendo elas:
 * Criação do arquivo com o comando _touch_;
 * Inicialização da matriz:
 1  1  0  3  4
 2  1 -1  1  1
 3 -1 -1  2 -3
-1  2  3 -1  4
 * Impressão da matriz
 * Ordenação da matriz, colocando a linha com 0 em uma n-1, onde n é a coluna que o 0 está presente
 * A primeira coluna é zerada utilizando a primeira linha, para isso, pegamos o primeiro elemento da segunda linha, dividimos pelo primeiro elemento da primeira linha, então subtraimos toda a segunda linha pela primeira multiplicada por esse valor
 * De uma maneira geral, tendo a matriz exemplo:
 
 a1,1 a1,2 a1,3 a1,4 ... a1,n Linha 1
 a2,1 a2,2 a2,3 a2,4 ... a2,n Linha 2
 a3,1 a3,2 a3,3 a3,4 ... a3,n Linha 3
 .   .   .   .   ... .
 .   .   .   .   ... .
 .   .   .   .   ... .
 an,1 an,2 an,3 an,4 ... an,n Linha n
 
 Temos então:
 Linha n = Linha n - an,1/an,n-1 * Linha n-1
 Repetindo isso para todas as linhas que tem abaixo da linha n-1, então da linha 1, o processo é repetido n-1 vezes, para linha 2 n-2, etc.
 
 * No final é calculado os valores dos coeficientes, fazendo uma multiplicação pelos elementos depois uma subtração pelos elementos da coluna k=n+1,
 xk=ak,5 - soma de k-1 a 1 dos valores ak,i     onde o i é o indice do somatório
 
 

'''
Lista 03 - Operadores Lógicos e Relacionais

Q5. Comparando Múltiplos Valores: Proponha que os alunos escrevam um programa que verifica se um número (por exemplo, 5) é menor que 10 e maior que 3, usando operadores relacionais combinados com operadores lógicos, e imprima o resultado.

'''

numero = int(input("Digite um número: "));

print(numero, "é menor que 10 e maior que 3?");

if numero < 10 and numero > 3 :
    print("Sim!", numero, "está dentro do intervalo de 4 a 9.");
else :
    print("Não!", numero, "não está dentro do intervalo de 4 a 9.");





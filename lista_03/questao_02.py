'''
Lista 03 - Operadores Lógicos e Relacionais

Q2. Maior ou Menor?: Solicite a criação de um script que compare dois números (como 15 e 30) usando os operadores > e <, imprimindo os resultados dessas comparações.

'''

numero1 = int(input("Digite um número: "));

numero2 = int(input("Digite outro número: "));

if numero1 > numero2 :
    print(numero1, "é maior que ", numero2);
elif numero1 < numero2 :
    print(numero1, "é menor que ", numero2);
else :
    print(numero1, "é igual a ", numero2);
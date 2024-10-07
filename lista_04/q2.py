"""Lista 04 - Condicional Simples

Q2. Faça um algoritmo que lê dois números, e verifica se o primeiro número é maior ou igual ao segundo número. Se for, escrever "O número {valor do número 1} é maior ou igual ao número {valor do número 2}". Se não, escrever "O número {valor do número 1} é menor ou igual ao número {valor do número 2}".

"""

numero1 = int(input("Digite um número: "));

numero2 = int(input("Digite outro número: "));

if numero1 >= numero2:
    print(f"O número {numero1} é maior ou igual ao número {numero2}.");

else:
    print(f"O número {numero1} é menor que o número {numero2}."); 

# Não coloquei "O número {valor do número 1} é menor ou igual ao número {valor do número 2}" no else conforme o enunciado, porque não faria sentido. Se na primeira proposição já foi feita a comparação de igualdade, seria inútil e ambíguo refazê-la na segunda proposição.
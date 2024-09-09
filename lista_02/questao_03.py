"""
LISTA 02 - Variáveis e Operações Matemáticas

Q3.  Faça um programa que leia o nome de uma pessoa e a sua idade. Imprima uma mensagem que diga "Olá, [nome]. Você terá  [idade] anos daqui a 10 anos". Os dados de entrada devem ser armazenados em variáveis distintas.

"""

nome = input("Qual o seu nome? ");

idade = int(input("Qual a sua idade? "));

idade_futura = idade + 10;

print("Olá,", nome + ". Você terá", idade_futura, "anos daqui a 10 anos.");
# coloquei o + no lugar da vírgula para evitar que fique um espaço entre Andrezza e o ponto no texto impresso.
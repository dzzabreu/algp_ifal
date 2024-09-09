"""
LISTA 02 - Variáveis e Operações Matemáticas

Q10. Área de um Triângulo: Escreva um algoritmo que solicita ao usuário a base e a altura de um triângulo, depois calcula e exibe a área do triângulo. A fórmula para calcular a área de um triângulo é: área = (base x altura) / 2.

"""

base_triangulo = int(input("Digite o comprimento da base do triângulo: "));

altura_triangulo = int(input("Digite o comprimento da altura do triângulo: "));

area_triangulo = (base_triangulo * altura_triangulo) / 2;

print("A área do triângulo de base", base_triangulo, "e altura", altura_triangulo,"é:", area_triangulo);
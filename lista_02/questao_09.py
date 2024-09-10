"""
LISTA 02 - Variáveis e Operações Matemáticas

Q9. Área de um Círculo: Escreva um algoritmo que solicita ao usuário o raio de um círculo, depois calcula e exibe a área do círculo. A fórmula para calcular a área de um círculo é área = π x raio^2. Você pode usar a aproximação de 3.1416 para π.

"""

raio_circulo = float(input("Digite o raio do círculo: "));

pi = 3.1416; #também poderia usar o math.pi

area_circulo = pi * (raio_circulo ** 2);

print("A área do círculo de raio", raio_circulo, "é:", area_circulo);
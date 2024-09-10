"""
LISTA 02 - Variáveis e Operações Matemáticas

Q7. Escreva um algoritmo que solicita ao usuário uma temperatura em graus Celsius e a converte para graus Fahrenheit e Kelvin. Use as fórmulas Fahrenheit = Celsius * 1.8 + 32 e Kelvin = Celsius + 273.15 para realizar as conversões.

"""

temperatura_Celsius = float(input("Digite a temperatura em graus Celsius: "));

conversor_Fahrenheit = temperatura_Celsius * 1.8 + 32;

conversor_Kelvin = temperatura_Celsius + 273.15;

print("A temperatura", temperatura_Celsius, "graus Celsius equivale a", conversor_Fahrenheit, "graus Fahrenheit e", conversor_Kelvin, "Kelvin.");
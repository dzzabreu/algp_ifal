"""
LISTA 02 - Variáveis e Operações Matemáticas

Q6. Escreva um algoritmo que solicita ao usuário uma quantidade de tempo em segundos e então a converte para horas. Por exemplo, se o usuário inserir 3666 segundos, o programa deve imprimir "1 hora", sem considerar os segundos restantes.

"""

segundos_entrada = int(input("Digite quantos segundos você quer converter em horas: "));

conversor_hora = segundos_entrada // 3600;

print(segundos_entrada, "segundos equivale aproximadamente a", conversor_hora, "hora(s).");


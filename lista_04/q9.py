"""Lista 04 - Condicional Simples

Q9. Elabore um algoritmo para que só possa autorizar a entrada na loja àqueles que estão com a anuidade de associação em dia ou pagar o valor de 25 reais na entrada.

"""

print("Olá, bem-vindo(a) à nossa loja!");

print("ATENÇÃO: Loja exclusiva para membros associados. Por favor, comprove que sua anuidade está em dia ou pague o valor de R$ 25,00 na entrada.");

anuidade = input("A sua anuidade está atualizada? (Digite 'Sim' ou 'Não'): ");

if anuidade == "Sim" or anuidade == "sim":
    print("Ótimo! Vou te encaminhar a nossa lista de produtos.");

elif anuidade == "Não" or anuidade == "não":
    pagar_anuidade = input("Deseja pagar a taxa de entrada de R$ 25,00? (Digite 'Sim' ou 'Não'): ");

    if pagar_anuidade == "Sim" or pagar_anuidade == "sim":
        print("Ótimo! Vou te encaminhar a nossa lista de produtos.");
    
    elif pagar_anuidade == "Não" or pagar_anuidade == "não":
        print("Infelizmente não poderemos te ajudar. Você precisa estar com a sua anuidade em dia ou pagar a taxa de entrada!");
    
    else:
        print("Não entendi. Por favor, digite uma resposta válida.");

else:
    print("Não entendi. Por favor, digite uma resposta válida.");
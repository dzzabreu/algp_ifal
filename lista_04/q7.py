"""Lista 04 - Condicional Simples

Q7. Elabore um algoritmo para representar um sistema de compra de produtos agrícolas de uma feira, mas que só permite realizar a compra, se a pessoa tiver dinheiro para pagar à vista e se estiver com a anuidade de associação de produtor rural em dia. 

"""

print("Olá, bem-vindo(a) à nossa loja de produtos agrícolas!");

print("ATENÇÃO: Não fazemos parcelamento, só aceitamos pagamentos à vista.");

aceita_condicao = input("Você pretende pagar à vista? (Digite 'Sim' ou 'Não'): ");

anuidade = input("A sua anuidade de associação de produtor rural está atualizada? (Digite 'Sim' ou 'Não'): ");

if (aceita_condicao == "Sim" or aceita_condicao == "sim") and (anuidade == "Sim" or anuidade == "sim"):
    print("Ótimo! Vou te encaminhar a nossa lista de produtos.");

elif (aceita_condicao == "Não" or aceita_condicao == "não") and (anuidade == "Sim" or anuidade == "sim"):
    print("Infelizmente não poderemos te ajudar. Só aceitamos pagamentos à vista!");

elif (aceita_condicao == "Sim" or aceita_condicao == "sim") and (anuidade == "Não" or anuidade == "não"):
    print("Infelizmente não poderemos te ajudar. Você precisa estar com a sua anuidade em dia!");

elif (aceita_condicao == "Não" or aceita_condicao == "não") and (anuidade == "Não" or anuidade == "não"):
    print("Infelizmente não poderemos te ajudar. Você precisa atualizar a sua anuidade e aceitar as nossas condições de pagamento!");

else:
    print("Não entendi. Por favor, digite uma resposta válida.");
"""Lista 04 - Condicional Simples

Q6. Elabore um algoritmo para representar um sistema de compra de produtos agrícolas de uma feira, mas que só permite compras à vista.

"""

print("Olá, bem-vindo(a) à nossa loja de produtos agrícolas!");

print("ATENÇÃO: Não fazemos parcelamento, só aceitamos pagamentos à vista.");

aceita_condicao = input("Você pretende pagar à vista? (Digite 'Sim' ou 'Não'): ");

if aceita_condicao == "Sim" or aceita_condicao == "sim":
    print("Ótimo! Vou te encaminhar a nossa lista de produtos.");

elif aceita_condicao == "Não" or aceita_condicao == "não":
    print("Infelizmente não poderemos te ajudar. Só aceitamos pagamentos à vista!");

else:
    print("Não entendi. Por favor, digite uma resposta válida.");

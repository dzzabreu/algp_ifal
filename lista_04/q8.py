"""Lista 04 - Condicional Simples

Q8. Elabore um algoritmo que solicita duas informações do usuário. A primeira, pergunta se possui bolsa família (S ou N), e a segunda, se possui mais de três filhos (S ou N). Se for contemplado pelo bolsa família e possuir mais de três filhos, deverá retornar Verdadeiro, significando que pode acessar à vaga de cotista.

"""

bolsa_familia = input("Você possui Bolsa Família? (Digite 'Sim' ou 'Não'.) ");

filhos = int(input("Quantos filhos você tem? "));

if (bolsa_familia == "Sim" or bolsa_familia =="sim") and (filhos > 3):
    print("Você tem acesso à vaga de cotista.");

elif (bolsa_familia == "Não" or bolsa_familia =="não") and (filhos <= 3):
    print("Você não tem acesso à vaga de cotista.");

else:
    print("Não entendi. Tente novamente.");

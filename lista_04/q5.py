"""Lista 04 - Condicional Simples

Q5. Faça um algoritmo que irá fazer o cadastro de usuário. Para isso, solicita o nome do usuário, e a senha. Depois, pede que o usuário confirme novamente a senha. O sistema deverá verificar se as senhas digitadas são iguais. Se forem iguais, informar que o cadastro está correto. Se não forem iguais, informar que o cadastro não foi realizado porque as senhas não conferem.

"""

print("CADASTRO DE USUÁRIO");

nome_usuario = input("Digite o seu nome de usuário: ");

senha = input("Digite a sua senha: ");

senha_confirmacao = input("Digite a sua senha novamente: ");

if senha == senha_confirmacao:
    print("O cadastro está correto. Usuário criado!");

else:
    print("O cadastro não pôde ser realizado, pois as senhas digitadas não conferem.");
# Crie um código onde é solicitado para o usuário inserir dois valores: o ano atual, e o ano de nascimento.
# O sistema deve calcular quantos anos ele tem de acordo com essas informações e exibir no console.

ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_idade = ano_atual - ano_nascimento
print(f"De acordo com o ano atual {ano_atual} e com o ano de nascimento {ano_nascimento}, a idade é {ano_idade}")
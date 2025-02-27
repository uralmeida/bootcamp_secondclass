## Refatorar o projeto da aula anterior evitando Bugs!

    # Realizar o tratamento de entradas inválidas que não podem convertidas para um número de ponto flutuante e prevenção de 
# valores negativos para salário e bônus, você pode modificar o código diretamente. Isso envolve adicionar verificações adicionais após 
# a tentativa de conversão para garantir que os valores sejam positivos.

# Solicita ao usuário que digite seu nome


try:
    nome_usuário = input("Digite o seu nome: ")

# Verifica se o nome está vazio

    if len(nome_usuário) == 0:
        raise ValueError("O nome de usuário está vazio.")

# Verifica se há números no nome

    elif any(char.isdigit() for char in nome_usuário):
        raise ValueError("O nome de usuário não deve conter números.")
    else:
        print("Nome válido:", nome_usuário)
except ValueError as e:
    print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float

try:
    salário = float(input("Digite valor do seu salário: "))
    if salário <= 0:
        print("Por favor, digite um valor do salário.")
except ValueError:
    print("Digite um número válido para o salário.")

# Solicita ao usuário que digite o valor do bônus recebido e converte para float

try:
    valor_bonus = float(input("Digite o valor do bônus recebido: "))
    if valor_bonus <0:
        print("Digite um valor válido.")
except ValueError:
    print("Digite um número válido para o bônus.")

# Assumindo uma lógica de cálculo para o bônus final e KPI

bonus = valor_bonus * 1.2
kpi = (salário + bonus) / 1000

# Imprime as informações para o usuário

print(f"Seu KPI é: {kpi:.2f}")
print(f"{nome_usuário}, valor do seu sálario é R${salário:.2f} e seu bônus total é R${bonus:.2f}.")
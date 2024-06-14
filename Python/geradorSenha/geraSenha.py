import random
from datetime import datetime, timedelta

# Função para gerar senhas de diferentes tipos
def gerar_senha(tamanho, tipo):
    if tipo == 1:
        caracteres = '0123456789'
    elif tipo == 2:
        caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    elif tipo == 3:
        caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]}{|;:,.<>?'
    else:
        raise ValueError("Tipo de senha não suportado. Use 1 (numérica), 2 (alfanumérica) ou 3 (com caracteres especiais).")
    
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

# Solicita o tamanho da senha
while True:
    tam = input('Qual o tamanho da senha? ')
    if tam.isnumeric():
        tam = int(tam)
        break
    else:
        print("Por favor, insira um número válido.")

# Solicita o tipo de senha
while True:
    try:
        tipo = int(input("Digite o código do tipo de senha (1 para numérica, 2 para alfanumérica, 3 para com caracteres especiais): "))
        if tipo in [1, 2, 3]:
            break
        else:
            print("Por favor, insira um código válido (1, 2 ou 3).")
    except ValueError:
        print("Por favor, insira um código válido (1, 2 ou 3).")

# Gera a senha com base no tamanho e tipo fornecidos
senha = gerar_senha(tam, tipo)
data_geracao = datetime.now()
data_geracao_str = data_geracao.strftime('%Y-%m-%d %H:%M:%S')

# Adiciona 90 dias à data de geração
data_expiracao = data_geracao + timedelta(days=90)
data_expiracao_str = data_expiracao.strftime('%Y-%m-%d %H:%M:%S')

# Salva a senha e a data no arquivo
with open('senhas.txt', 'a') as f:
    f.write(f'{data_geracao_str}, {senha}\n')

print(f'Senha {senha} salva com sucesso no arquivo senhas.txt na data {data_geracao_str}.')
print(f'Validade 90 dias, trocar antes de {data_expiracao_str}.')

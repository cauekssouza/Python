# Data e Horário 
from datetime import datetime, timedelta
data_atual =  datetime.now() 
data_futura = data_atual + timedelta(2) 
print(data_futura)

# Data Atual
from datetime import datetime

data_atual = datetime.now()
print(data_atual.date())

# Olá Mundo No dicionario
mensagem = {'m1': {'m2': 'Olá Mundo'}}
print(mensagem['m1']['m2'])


# Desenvolva um programa que leia o seu nome completo e que apresente somente o seu primeiro e último nomes
nome_completo = str(input('Informe o seu nome completo: '))
primeiro_nome = lambda nome: nome.split()[0]
ultimo_nome = lambda nome: nome.split()[-1]

print(f'Seu primeiro nome é {primeiro_nome(nome_completo)} '
      f'e o seu último nome é {ultimo_nome(nome_completo)}')
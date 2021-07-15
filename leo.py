### ATIVIDADE 22.03 ###

nome = input('Qual seu nome?:')
idade = int(input('Qual sua idade?:'))
genero = input('Genero?:')

print("Classifique suas proximas respostas como, sim ou nao!")

comorbidades = input('Voce possui alguma doença?:')
vacina = input('Já tomou a vacina do COVID?:')
sintomas = input('Esta sentindo algum sintoma?:')
contato = input("Esteve em contato com alguem que pegou a doença?:")


#condicionais   

if contato == 'sim':
    print('Siga ate a sala 1:')
    if contato == 'nao':
        print('Siga ate a sala 2')
if  idade <= 14:
    if comorbidades and sintomas == 'sim':
        print('Amarelo, tome remedios e fique de 40tena')
    else: 
        print('partiu games!')
elif idade > 14 and idade < 60:
    if sintomas and comorbidades == 'sim':
        print('Amarelo, tome remedios e fique de 40tena')
    elif sintomas and vacina == 'sim':
        print('Amarelo, tome remedios e fique de 40tena')

if contato and sintomas == 'sim':
    print ('laranja, tratamento hospitalar!')

elif sintomas and comorbidades == 'sim':
    print ('vermelho, tratamento direto na UTI!')

# CONDICAO NAO
else:
    if sintomas and comorbidades and contato == 'nao':
        print('branco, pode voltar para casa')
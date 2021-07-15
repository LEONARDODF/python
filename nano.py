### codigo pro meu amor!

nome = []
idade = []
peso = []
telefone = []
objetivo = []

resposta = 'S'
while resposta == 'S':
    nome.append(input('Qual seu nome?:'))
    idade.append(input('Quantos anos você tem?:'))
    peso.append(input('Qual o seu peso atual:'))
    telefone.append(input('Qual seu telefone de contato?:'))
    objetivo.append(input('Qual seu objetivo?:'))
    resposta = input('Digite \'Sim\' para refazer o formulario!:').upper()

for relatorio in range(0,len(nome)):
    input('Suas informações estão corretas:?')
    print ('\nNome......:',nome[relatorio])
    print ('Idade.....:',idade[relatorio])   
    print ('Peso......:',peso[relatorio])
    print ('Telefone..:',telefone[relatorio])
    print ('Objetivo..:',objetivo[relatorio])

busca = input('\nQual paciente deseja rever as informações?:')
for relatorio in range (0,len(nome)):
    if busca==nome[relatorio]:
        print ('\nNome......:',nome[relatorio])
        print ('Idade.....:',idade[relatorio])   
        print ('Peso......:',peso[relatorio])
        print ('Objetivo..:',objetivo[relatorio])
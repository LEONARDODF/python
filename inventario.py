# code para inventario e equipamentos

def cadastroEquipamento(equipamento, preço, data, departamento):
    resp = 'S'
while resp == 'S':
 equipamento.append(input("Entre um nome do Equipamento: "))
 preço.append(input("Preço: "))
 data.append(input("Data da compra: "))
 departamento.append(input("Entre o Departamento: "))
 resp = input("Deseja inserir mais um cadastro? ").upper()
#Relatorio
def relatorioEquipamento(equipamento, preço, data, departamento):
    for elemento in range(0, len(equipamento)):
        print("\nEquipamento: ", equipamento[elemento])
print("\npreço: ", preço[elemento])
print("\ndata: ", data[elemento])
print("\ndepartamento: ", departamento[elemento])
#Busca
def buscaEquipamento(equipamento, preço, data, departamento):
 busca = input("Qual o equipamento que deseja buscar: ").title()
for elemento in range(0, len(equipamento)):
    if busca == equipamento[elemento]:
        print("\nEquipamento: ", equipamento[elemento])
        print("\npreço: ", preço[elemento])
        print("\ndata: ", data[elemento])
        print("\ndepartamento: ", departamento[elemento])
#Alterar
def alteraEquipamento(equipamento, preço, data, departamento): #tentei colocar a lista, mas n consegui ;(
 alterar = input("Qual o equipamento que deseja alterar : ").title()
for elemento in range(0, len(equipamento)):
    if alterar == equipamento[elemento]:
        preço[elemento] = input("Digite o preço novo: ")
        print("\nEquipamento: ", equipamento[elemento])
        print("\npreço: ", preço[elemento])
        print("\ndata: ", data[elemento])
        print("\ndepartamento: ", departamento[elemento])
#Remover
def removeEquipamento(equipamento, preço, data, departamento):
 remover = input("Qual o equipamento que deseja alterar : ").title()
for elemento in range(0, len(equipamento)):
    if remover == equipamento[elemento]:
        del equipamento[elemento]
        del preço[elemento]
        del data[elemento]
        del departamento[elemento]
    break
 
#EQUIPAMENTOS 
from funcoes import*
equipamento = ["Ps3", "Pc1", "Pc2"]
preço = ["1200", "4000", "5555"]
data = ["Dia 20", "Dia 20", "Dia 20"]
departamento = ["Eletronicos", "Eletronicos", "Eletronicos"]
resp = "SIM"
while resp == "SIM":
 opcao = int(input("Bem vindo a Quintino Corp" + "\nEntre 1 para Cadastrar" + "\nEntre 2 para Relatorio" + "\nEntre 3 para Busca" + "\nEntre 4 para Alterar" + "\nEntre 5 para Remover" + "\nEntre 6 para Sair \n"))
while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
    print("Opção invalida, entre um uma opção: ")
if opcao == 1:
 cadastroEquipamento(equipamento, preço, data, departamento)
elif opcao == 2:
 relatorioEquipamento(equipamento, preço, data, departamento)
elif opcao == 3:
 buscaEquipamento(equipamento, preço, data, departamento)
elif opcao == 4:
 alteraEquipamento(equipamento, preço, data, departamento)
elif opcao == 5:
 removeEquipamento(equipamento, preço, data, departamento)
elif opcao == 6:
 resp = "NAO"




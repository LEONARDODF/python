from funcoes import *inventario = {}
carregarDados(inventario)
opcao = chamarMenu()
while opcao>0 and opcao <5:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        exibir(inventario)
    elif opcao == 4:
        carregarDados(inventario)
    opcao=chamarMenu()
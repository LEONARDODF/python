def chamarMenu():
    escolha = int(input("Digite: "    "\n<1> para registrar ativo"    "\n<2> para persistir arquivo"    "\n<3> para exibir Inventario"    "\n<4> para carragar dados salvos"    "\nSua Opção: "))
    return escolha 
def registrar(dicionario):
        resp = "SIM" 
        while resp == "SIM":
            dicionario[input("Entre com a TAG: ")] = [input("Nome do equipamento: "), 
            input("Valor do Equipamento: "),
            input("Data da Compra: "),
            input("Departamento: ")]
            resp = input("deseja repetir? ").upper()
def persistir(dicionario):
    with open("inventario.csv", "w") as inv:
        for tag, lista in dicionario.items():
            inv.write(tag + ";" + lista[0] + ";" + lista[1] + ";" + lista[2] + ";" + lista[3])
    return "Dado persistido com sucesso!"
def exibir(dicionario):
      for tag, lista in dicionario.items():
        print("\nTag.............. ", tag)
        print("Nome............. ", lista[0])
        print("Preço............ ", lista[1])
        print("Data............. ", lista[2])
        print("Departamento..... ", lista[3])        
def carregarDados(dicionario):
    with open("inventario.csv", "r") as inv:
        linhas = inv.readlines()
        for linha in linhas:
            lista = linha.split(";")
            dicionario[lista[0]] = [lista[1], lista[2], lista[3], lista[4]]
    print("\nDados Carregados com Sucesso!!!")
import getpass
resp="SIM"
while resp == "SIM":

    user = input("Entre um usuario: ").upper()
    senha = getpass.getpass("Entre uma senha: ").upper()
    if user == "ADM" and senha =="1234":
        print("Bem Vindo Administrador(a)!")
    elif user == "USER" and senha =="123456" :
        print("Bem vindo Usuario(a)!")
    else:
        resposta = input("Login invalido, deseja logar como convidado?")
        if resposta == "SIM":
            print("Bem Vindo Convidado(a)!")
        else:
            print("Tente novamente!")
    resp= input("Deseja repetir?").upper()
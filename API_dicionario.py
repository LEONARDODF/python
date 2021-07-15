emails = {}
opcao = input ('O que deseja realizar?\n' +
            '<A> - Para editar um email\n' +
            '<B> - Para pesquisar um email\n' +
            '<C> - Para exportar um email\n' +
            '<D> - Para importar um email:').upper()
while opcao== 'A' or opcao== 'B' or opcao== 'C' or opcao== 'D':
    if opcao =='A':
        chave = input ('Digite seu loguin:').upper()
        nome = input ('Digite seu nome:').upper()
        data = input ('Qual ultima data de acesso?:').upper()
        estacao = input ('Qual a ultima estacao acessada?:').upper()
        emails[chave]=[nome, data, estacao]
    opcao = input ('O que deseja realizar?\n' +
            '<A> - Para editar um email\n' +
            '<B> - Para pesquisar um email\n' +
            '<C> - Para exportar um email\n' +
            '<D> - Para importar um email:').upper()
            
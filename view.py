from controller import PessoaController

while True:
    decisao = int(input('Digite 1 para salvar uma pessoa, digite 2 para ver a pessoa salva ou 3 para sair.'))
    print (decisao)

    if decisao == 3:
        break
    if decisao == 1:
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        cpf = input('Digite seu cpf: ')

        if PessoaController.cadastrar(nome, idade, cpf):
            print('Usuario cadastrado com sucesso.')
        else:
            print('Digite valores validos.')
    
from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)

    @classmethod
    def ler(cls):
        nome = 'Ésley'
        idade = 28
        cpf = '00000000012'
        return Pessoa(nome, idade, cpf)


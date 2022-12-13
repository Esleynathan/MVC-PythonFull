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
        cpf = '000.000.000-12'
        return Pessoa(nome, idade, cpf)

p1 = Pessoa('Ésley', 20, '000.000.000-12')
PessoaDal.salvar(p1)
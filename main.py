class Transacao:
    def __init__(self, valor, data, categoria, tipo):
        self.valor = valor
        self.data = data
        self.categoria = categoria
        self.tipo = tipo

    def __str__(self):
        return f'R${self.valor}, {self.data}, {self.categoria}, {self.tipo}'

class Conta:
    def __init__(self):
        self.saldo = 0
        self.transacoes = []

    def calcular_saldo(self):
        for transacao in self.transacoes:
            if transacao.tipo in ['Receita', 'Despeza']:
                if transacao.tipo == 'Despeza':
                    self.saldo -= int(transacao.valor)
                else:
                    self.saldo += int(transacao.valor)

    def listar_transacoes(self):
        for transacao in self.transacoes:
            print(transacao)

    def adicionar_transacao(self):
        nome = input('Valor: ')
        data = input('Data: ')
        categoria = input('Categoria: ')
        tipo = input('Tipo: ')
        transacao = Transacao(nome, data, categoria, tipo)
        self.transacoes.append(transacao)

    def remover_transacao(self):
        transacao_encontrada = False
        categoria = input('Insira o nome da categoria da transação ser removida: ')
        for transacao in self.transacoes:
            if transacao.categoria == categoria:
                self.transacoes.remove(transacao)
                transacao_encontrada = True
        if not transacao_encontrada:
            print('ERRO! Transação não encontrada!')

conta = Conta()
conta.adicionar_transacao()
conta.listar_transacoes()
print(conta.saldo)
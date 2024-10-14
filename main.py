from random import randint



def valida_int(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('Informe um número inteiro válido!')
        else:
            return n

def gera_id():
    while True:
        id_gerado = randint(1000, 5000)
        if id_gerado not in conta.lista_de_id:
            return id_gerado

class Transacao:
    def __init__(self, valor, data, categoria, tipo):
        self.valor = valor
        self.data = data
        self.categoria = categoria
        self.tipo = tipo
        self.id_da_transacao = gera_id()

    def __str__(self):
        return f'R${self.valor}, {self.data}, {self.categoria}, {self.tipo}, {self.id_da_transacao}'

    def modificar_valor(self):
        novo_valor = input('Insira o novo valor: ')
        self.valor = novo_valor
        print('Valor atualizado com sucesso!')

    def modificar_data(self):
        nova_data = input('Insira o novo valor: R$')
        self.data = nova_data
        print('Data atualizada com sucess')

    def modificar_categoria(self):
        nova_categoria = input('Insira a nova categoria: ')
        self.categoria = nova_categoria
        print('Valor atualizado com sucess')

    def modificar_tipo(self):
        novo_tipo = input('Insira o novo valor: ')
        self.tipo = novo_tipo
        print('Valor atualizado com sucess')

class Conta:
    def __init__(self):
        self.saldo = 0
        self.transacoes = []
        self.lista_de_id = []
        self.lista_de_categorias = []

    def calcular_saldo(self):
        for transacao in self.transacoes:
            if transacao.tipo in ['Receita', 'Despeza']:
                if transacao.tipo == 'Despeza':
                    self.saldo -= transacao.valor
                else:
                    self.saldo += transacao.valor

    def vizualizar_saldo(self):
        print(self.saldo)

    def listar_transacoes(self):
        for transacao in self.transacoes:
            print(transacao)

    def filtrar_transacoes(self):
        categoria_encontrada = False
        categoria_filtrada = input('informe a categora a ser filtrada: ').strip().capitalize()
        for transacao in self.transacoes:
            if transacao.categoria == categoria_filtrada:
                print(transacao)
                categoria_encontrada = True
        if not categoria_encontrada:
            print('ERRO! Categoria não encontrada.')

    def adicionar_transacao(self):
        valor = int(input('Valor: '))
        data = input('Data: ')
        categoria = input('Categoria: ')
        tipo = input('Tipo: ')
        transacao = Transacao(valor, data, categoria, tipo)
        self.transacoes.append(transacao)
        self.lista_de_id.append(transacao.id_da_transacao)
        self.lista_de_categorias.append(transacao.categoria)

    def remover_transacao(self):
        transacao_encontrada = False
        categoria = input('Insira o nome da categoria da transação ser removida: ')
        for transacao in self.transacoes:
            if transacao.categoria == categoria:
                self.saldo -= transacao.valor
                self.transacoes.remove(transacao)
                transacao_encontrada = True
        if not transacao_encontrada:
            print('ERRO! Transação não encontrada!')

conta = Conta()
while True:
    opcao = valida_int('''MENU
[1] NOVA TRANSAÇÃO
[2] VER TRANSAÇÕES
[3] GERAR RELATORIOS
[4] VER SALDO
[5] EDITAR OU REMOVER TRANSAÇÕES
[6] SAIR
> ''')
    if opcao == 1:
        conta.adicionar_transacao()
    elif opcao == 2:
        conta.listar_transacoes()
    elif opcao == 3:
        conta.filtrar_transacoes()
    elif opcao == 4:
        while True:
            opacao_de_relatorio = valida_int('''[1] FILTRAGEM
[2] AGRUPAMENTO
[3] COMPARAÇÃO 
[4] SAIR
> ''')



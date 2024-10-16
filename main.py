import sys
from random import randint
from datetime import datetime



def valida_int(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('Informe um número inteiro válido!')
        else:
            return n

def valida_tipo(msg):
    tipos_de_transacao = ['Receita', 'Despesa']
    while True:
        t = input(msg).strip().capitalize()
        if t in tipos_de_transacao:
            return t
        else:
            print('Informe um tipo válido!')

def valida_data(msg):
    while True:
        try:
            data = input(msg)
            datetime.strptime(data, '%d/%m/%Y')
        except:
            print('ERRO! Formato de data inválido!')
        else:
            return data



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
        while True:
            novo_valor = valida_int('Insira o novo valor: ')
            if novo_valor == self.valor:
                print('ERRO! Novo valor igual ao atual.')
            else:
                self.valor = novo_valor
                print('Valor atualizado com sucesso!')
                break


    def modificar_data(self):
        while True:
            nova_data = valida_data('Insira a nova data: ')
            if nova_data == self.data:
                print('ERRO! Nova data igual a atual.')
            else:
                self.data = nova_data
                print('Data atualizada com sucess')
                break

    def modificar_categoria(self):
        while True:
            nova_categoria = input('Insira a nova categoria: ')
            if nova_categoria == self.categoria:
                print('ERRO! Nova categoria igual a atual.')
            else:
                self.categoria = nova_categoria
                print('Categoria atualizada com sucesso!')
                break

    def modificar_tipo(self):
        while True:
            novo_tipo = valida_tipo('Insira o novo tipo: ')
            if novo_tipo == self.tipo:
                print('ERRO! Novo tipo igual a atual.')
            else:
                self.tipo = novo_tipo
                print('Valor atualizado com sucesso!')
                break

class Conta:
    def __init__(self):
        self.saldo = 0
        self.transacoes = []
        self.lista_de_id = []
        self.lista_de_categorias = []

    def calcular_saldo(self):
        for transacao in self.transacoes:
            if transacao.tipo in ['Receita', 'Despesa']:
                if transacao.tipo == 'Despesa':
                    self.saldo -= transacao.valor
                else:
                    self.saldo += transacao.valor

    def vizualizar_saldo(self):
        saldo_provisorio = 0
        for transacao in self.transacoes:
            if transacao.tipo == 'Receita':
                saldo_provisorio += transacao.valor
            else:
                saldo_provisorio -= transacao.valor
        self.saldo = saldo_provisorio
        print(f'SALDO: {self.saldo}')

    def listar_transacoes(self):
        if len(self.transacoes) == 0:
            print('Nenhuma transação registrada!')
        else:
            for transacao in self.transacoes:
                print(transacao)

    def filtrar_categoria(self):
        lista_de_receitas = []
        lista_de_despesas = []
        categoria_filtrada = ''
        while categoria_filtrada not in self.lista_de_categorias:
            categoria_filtrada = input('informe a categora a ser filtrada: ').strip().title()
            if categoria_filtrada in self.lista_de_categorias:
                for transacao in self.transacoes:
                    if transacao.categoria == categoria_filtrada:
                        if transacao.tipo == 'Despesa':
                            lista_de_despesas.append(transacao)
                        else:
                            lista_de_receitas.append(transacao)
                for transaco in lista_de_receitas:
                    print(transaco)
                for transacao in lista_de_despesas:
                    print(transacao)
            else:
                print('ERRO! Categoria não encontrada.')

    def filtrar_tipo(self):
        tipo_buscado = ''
        while tipo_buscado not in ['R', 'D']:
            tipo_buscado = input('Deseja exibir todas as (R)eceitas ou (D)espezas? ').strip().upper()[0]
        if tipo_buscado == 'R':
            tipo_buscado = 'Receita'
        elif tipo_buscado == 'D':
            tipo_buscado = 'Despesa'
        else:
            print('ERRO! Informe um tipo válido.')
        for transacao in self.transacoes:
            if transacao.tipo == tipo_buscado:
                print(transacao)

    def adicionar_transacao(self):
        valor = valida_int('Valor: ')
        data = valida_data('Data: ')
        categoria = input('Categoria: ').strip().capitalize()
        tipo = valida_tipo('Tipo: ')
        transacao = Transacao(valor, data, categoria, tipo)
        self.transacoes.append(transacao)
        self.lista_de_id.append(transacao.id_da_transacao)
        self.lista_de_categorias.append(transacao.categoria)
        print('Transação adicioanada com sucesso!')

    def remover_transacao(self):
        id_transacao = 0
        while id_transacao not in self.lista_de_id:
            id_transacao = valida_int('Informe o ID da trasção que deseja remove: ')
            if id_transacao in self.lista_de_id:
                for transacao in self.transacoes:
                    if transacao.id_da_transacao == id_transacao:
                        self.saldo -= transacao.valor
                        self.transacoes.remove(transacao)
                        print('Transação removida com sucesso!')
            else:
                print('ERRO! Informe um ID válido.')

def main():
    while True:
        opcao = valida_int('''MENU
[1] LISTAR TRANSAÇÕES
[2] NOVA TRANSAÇÃO
[3] EDITAR TRANSAÇÃO
[4] REMOVER TRANSAÇÃO
[5] FILTRAR
[6] VER SALDO
[7] SAIR
> ''')

        if opcao == 1:
            conta.listar_transacoes()

        elif opcao == 2:
            conta.adicionar_transacao()

        elif opcao == 3:
            while True:
                id_buscado = valida_int('Informe o ID da transação que deseja modificar: ')
                if id_buscado not in conta.lista_de_id:
                    print('ERRO! ID não encontrado.')
                else:
                    break

            for transacao in conta.transacoes:
                if transacao.id_da_transacao == id_buscado:
                    opcao_editar = 0
                    while opcao_editar not in range(1, 5):
                        opcao_editar = valida_int('''O QUE DESEJA MODIFICAR?
[1] VALOR
[2] DATA
[3] CATEGORIA
[4] TIPO
> ''')
                        if opcao_editar == 1:
                            transacao.modificar_valor()
                        elif opcao_editar == 2:
                            transacao.modificar_data()
                        elif opcao_editar == 3:
                            transacao.modificar_categoria()
                        elif opcao_editar == 4:
                            transacao.modificar_tipo()
                        else:
                            print('ERRO! Infor uma opção entre 1 e 4.')

        elif opcao == 4:
            conta.remover_transacao()

        elif opcao == 5:
            modo_de_filtragem = 0
            while modo_de_filtragem not in range(1, 3):
                modo_de_filtragem = valida_int('''QUAL SERÁ O MODO DE FILTRAGEM?
[1] POR TIPO
[2] POR CATEGORIA
> ''')
                if modo_de_filtragem == 1:
                    conta.filtrar_tipo()
                elif modo_de_filtragem == 2:
                    conta.filtrar_categoria()
                else:
                    print('ERRO! Informe uma opção válida.')

        elif opcao == 6:
            conta.vizualizar_saldo()

        elif opcao == 7:
            print('Até logo!')
            sys.exit()

        else:
            print('ERRO! Informe uma opção válida(tente um número entre 1 e 6).')

if __name__ == '__main__':
    conta = Conta()
    transacao1 = Transacao(1500, '15/10', 'Salário', 'Receita')
    transacao2 = Transacao(300, '16/10', 'Alimentação', 'Despesa')
    transacao3 = Transacao(500, '20/10', 'Aluguel', 'Despesa')
    transacao4 = Transacao(100, '20/10', 'Alimentação', 'Despesa')
    conta.transacoes.extend([transacao1, transacao2, transacao3, transacao4])
    conta.lista_de_categorias.extend([transacao.categoria for transacao in conta.transacoes])
    conta.lista_de_id.extend([transacao.id_da_transacao for transacao in conta.transacoes])
    main()
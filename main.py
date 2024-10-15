import sys
from random import randint



tipos_de_transacao = ['Receita', 'Despeza']

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
        while True:
            novo_valor = input('Insira o novo valor: ')
            if novo_valor == self.valor:
                print('ERRO! Novo valor igual ao atual.')
            else:
                self.valor = novo_valor
                print('Valor atualizado com sucesso!')
                break


    def modificar_data(self):
        while True:
            nova_data = input('Insira a nova data: ')
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
            novo_tipo = input('Insira o novo tipo: ')
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
            if transacao.tipo in ['Receita', 'Despeza']:
                if transacao.tipo == 'Despeza':
                    self.saldo -= transacao.valor
                else:
                    self.saldo += transacao.valor

    def vizualizar_saldo(self):
        print(self.saldo)

    def listar_transacoes(self):
        if len(self.transacoes) == 0:
            print('Nenhuma transação registrada!')
        else:
            for transacao in self.transacoes:
                print(transacao)

    def filtrar_categoria(self):
        lista_de_receitas = []
        lista_de_despezas = []
        categoria_filtrada = input('informe a categora a ser filtrada: ').strip().title()
        if categoria_filtrada in self.lista_de_categorias:
            for transacao in self.transacoes:
                if transacao.categoria == categoria_filtrada:
                    if transacao.tipo == 'Despeza':
                        lista_de_despezas.append(transacao)
                    else:
                        lista_de_receitas.append(transacao)
            for transaco in lista_de_receitas:
                print(transaco)
            for transacao in lista_de_despezas:
                print(transacao)
        else:
            print('ERRO! Categoria não encontrada.')

    def filtrar_tipo(self):
        tipo_buscado = input('Deseja exibir todas as Receitas ou Despezas? ').strip().capitalize()
        for transacao in self.transacoes:
            if transacao.tipo == tipo_buscado:
                print(transacao)

    def adicionar_transacao(self):
        valor = int(input('Valor: '))
        data = input('Data: ')
        categoria = input('Categoria: ')
        tipo = input('Tipo: ')
        transacao = Transacao(valor, data, categoria, tipo)
        self.transacoes.append(transacao)
        self.lista_de_id.append(transacao.id_da_transacao)
        self.lista_de_categorias.append(transacao.categoria)

    def remover_transacao(self, transacao):
        self.saldo -= transacao.valor
        self.transacoes.remove(transacao)
        print('Transação removida com sucesso!')

def main():
    while True:
        opcao = valida_int('''MENU
[1] LISTAR TRANSAÇÕES
[2] NOVA TRANSAÇÃO
[3] EDITAR OU REMOVER TRANSAÇÃO
[4] FILTRAR
[5] VER SALDO
[6] SAIR
> ''')

        if opcao == 1:
            conta.listar_transacoes()
        elif opcao == 2:
            conta.adicionar_transacao()
        elif opcao == 3:
            while True:
                opcao3_resp = input('Deseja (e)ditar ou (r)emover transação?').strip().lower()[0]
                if opcao3_resp in 'er':
                    break
                else:
                    print('Infomer uma opção válida!')
            while True:
                id_buscado = valida_int('Informe o ID da transação que deseja modificar: ')
                if id_buscado in conta.lista_de_id:
                    break
                else:
                    print('Infomer uma opção válida!')

            if id_buscado in conta.lista_de_id:
                for transacao in conta.transacoes:
                    if transacao.id_da_transacao == id_buscado:
                        if opcao3_resp == 'e':
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
                                print('ERRO! Informe uma opção válida.')

                        elif opcao3_resp == 'r':
                            conta.remover_transacao(transacao)
            else:
                print('ERRO! ID não encontrado.')

        elif opcao == 4:
            metodo_de_filtro = input('Deseja filtrar por Categoria ou Tipo? ').strip().lower()
            if metodo_de_filtro == 'categoria':
                conta.filtrar_categoria()
            elif metodo_de_filtro == 'tipo':
                conta.filtrar_tipo()

        elif opcao == 6:
            print('Até logo!')
            sys.exit()

        else:
            print('ERRO! Informe uma opção válida(tente um número entre 1 e 6).')

if __name__ == '__main__':
    conta = Conta()
    transacao1 = Transacao(1500, '15/10', 'Salário', 'Receita')
    transacao2 = Transacao(300, '16/10', 'Alimentação', 'Despeza')
    transacao3 = Transacao(500, '20/10', 'Alimentação', 'Despeza')
    conta.transacoes.extend([transacao1, transacao2, transacao3])
    main()
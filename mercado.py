from typing import List, Dict
from time import sleep

from models.produtos import Produto
from uteis.help import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:

    print('==================================')
    print('========== BEM VINDO(A) ==========')
    print('==========   WEB SHOP   ==========')

    print('Selecione uma opção a baixo: ')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar Produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Produto')
    print('6 - Sair do Sistema')

    opcao: int = int(input('Opção: '))


    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte Sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção Invalida!')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print(v := 'Cadastro de Produto')
    print('=' * len(v))

    nome: str = input('Informe o nome do Produto: ')

    preco: float = float(input('Informe o Preço do Produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print(v := 'Listagem de Produto')
        print('=' * len(v))
        for produto in produtos:
            print(produto)
            print('=' * 15)
            sleep(1)

    else:
        print('Produto ainda não existe')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print(v := 'Informe o código do produto que deseja adicionar ao carrinho')
        print('-' * len(v))
        print('===================== PRODUTOS DISPONIVEIS =======================')
        for produto in produtos:
            print(produto)
            print('-' * 20)
            sleep(1)

        codigo: int = int(input('Código: '))

        produto: Produto = pegar_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)

                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho ')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com o codigo {codigo} não foi encontrado')
            sleep(1)
            menu()
    else:
        print('Produto ainda Não existe')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos do Carrinho')

        for item in carrinho:
            for dado in item.items():
                print(dado[0])
                print(f'Quantidade: {dado[1]}')
                print('-' * 20)
                sleep(1)

    else:
        print('Ainda não existe produto no carrinho')
        sleep(2)
        menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do Carrinho')
        for item in carrinho:
            for dado in item.items():
                print(dado[0])
                print(f'Quantidade {dado[1]}')
                valor_total += dado[0].preco * dado[1]
        print(f'Sua fatura: {formata_float_str_moeda(valor_total)}')
        carrinho.clear()
        sleep(5)
        print('Volte sempre!')
    else:
        print('Ainda não existe produto no Carrinho')
        sleep(2)
        menu()


def pegar_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()

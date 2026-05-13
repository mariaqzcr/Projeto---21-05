from utils import titulo
from tarefas import (
    cadastrar_filme,
    listar_filmes,
    buscar_filme,
    registrar_aluguel,
    registrar_devolucao,
    mostrar_fila,
    mostrar_pilha,
    listar_por_genero
)

while True:

    titulo("LOCADORA DE FILMES")

    print("1 - Cadastrar filme")
    print("2 - Listar filmes")
    print("3 - Buscar filme")
    print("4 - Registrar aluguel")
    print("5 - Registrar devolução")
    print("6 - Mostrar fila de reservas")
    print("7 - Mostrar pilha de devoluções")
    print("8 - Listar filmes por gênero")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_filme()

    elif opcao == "2":
        listar_filmes()

    elif opcao == "3":
        buscar_filme()

    elif opcao == "4":
        registrar_aluguel()

    elif opcao == "5":
        registrar_devolucao()

    elif opcao == "6":
        mostrar_fila()

    elif opcao == "7":
        mostrar_pilha()

    elif opcao == "8":
        listar_por_genero()

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")

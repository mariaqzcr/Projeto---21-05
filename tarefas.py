from dados import filmes, fila_reservas, pilha_devolucoes
from dados import status_disponibilidade
from utils import linha


# Cadastrar filme
def cadastrar_filme():
    titulo = input("Título: ")
    genero = input("Gênero: ")
    ano = input("Ano: ")

    filme = {
        "titulo": titulo,
        "genero": genero,
        "ano": ano,
        "status": status_disponibilidade[0]
    }

    filmes.append(filme)

    print("Filme cadastrado com sucesso!")


# Listar filmes
def listar_filmes():
    if not filmes:
        print("Nenhum filme cadastrado.")
        return

    for i, filme in enumerate(filmes, start=1):
        linha()
        print(f"{i}. {filme['titulo']}")
        print(f"Gênero: {filme['genero']}")
        print(f"Ano: {filme['ano']}")
        print(f"Status: {filme['status']}")


# Buscar filme
def buscar_filme():
    nome = input("Digite o título: ").lower()

    encontrado = False

    for filme in filmes:
        if nome in filme["titulo"].lower():
            linha()
            print(f"Título: {filme['titulo']}")
            print(f"Gênero: {filme['genero']}")
            print(f"Ano: {filme['ano']}")
            print(f"Status: {filme['status']}")
            encontrado = True

    if not encontrado:
        print("Filme não encontrado.")


# Registrar aluguel
def registrar_aluguel():
    titulo_filme = input("Título do filme: ").lower()

    for filme in filmes:
        if filme["titulo"].lower() == titulo_filme:

            if filme["status"] == status_disponibilidade[1]:
                print("Filme indisponível.")
                return

            filme["status"] = status_disponibilidade[1]

            # FIFO
            fila_reservas.append(filme)

            print("Aluguel realizado com sucesso!")
            return

    print("Filme não encontrado.")


# Registrar devolução
def registrar_devolucao():
    titulo_filme = input("Título do filme: ").lower()

    for filme in filmes:
        if filme["titulo"].lower() == titulo_filme:

            if filme["status"] == status_disponibilidade[0]:
                print("Esse filme já está disponível.")
                return

            filme["status"] = status_disponibilidade[0]

            # LIFO
            pilha_devolucoes.append(filme)

            print("Devolução registrada com sucesso!")
            return

    print("Filme não encontrado.")


# Exibir fila FIFO
def mostrar_fila():
    if not fila_reservas:
        print("Fila vazia.")
        return

    print("\nFila de Reservas (FIFO)")
    linha()

    for filme in fila_reservas:
        print(filme["titulo"])


# Exibir pilha LIFO
def mostrar_pilha():
    if not pilha_devolucoes:
        print("Nenhuma devolução registrada.")
        return

    print("\nPilha de Devoluções (LIFO)")
    linha()

    for filme in reversed(pilha_devolucoes):
        print(filme["titulo"])


# Listar filmes disponíveis por gênero
def listar_por_genero():
    genero = input("Digite o gênero: ").lower()

    encontrou = False

    for filme in filmes:
        if (
            filme["genero"].lower() == genero
            and filme["status"] == "Disponível"
        ):
            print(filme["titulo"])
            encontrou = True

    if not encontrou:
        print("Nenhum filme disponível nesse gênero.")

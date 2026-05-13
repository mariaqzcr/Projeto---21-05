def titulo(texto):
    print("\n" + "=" * 40)
    print(texto.center(40))
    print("=" * 40)


def linha():
    print("-" * 40)


def validar_int(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print("Digite um número válido.")

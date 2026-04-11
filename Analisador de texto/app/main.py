import string


def limpar_texto(texto):
    texto = texto.lower()
    for pontuacao in string.punctuation:
        texto = texto.replace(pontuacao, "")
    return texto


def contar_caracteres(texto):
    contador = {}
    for char in texto:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1
    return contador


def contar_palavras(texto):
    palavras = texto.split()
    contador = {}

    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1

    return contador


def mostrar_top_palavras(contador, limite=5):
    ordenado = sorted(contador.items(), key=lambda x: x[1], reverse=True)
    return ordenado[:limite]


def estatisticas(texto):
    palavras = texto.split()
    print("\n📊 Estatísticas:")
    print(f"Total de palavras: {len(palavras)}")
    print(f"Total de caracteres: {len(texto)}")


def maior_palavra(texto):
    palavras = texto.split()
    if palavras:
        maior = max(palavras, key=len)
        print(f"\n🔎 Maior palavra: {maior}")


def menu():
    while True:
        print("\n" + "=" * 35)
        print("🧾 ANALISADOR DE TEXTO")
        print("=" * 35)
        print("Escolha as funções (separadas por espaço):")
        print("1 - Contar caracteres")
        print("2 - Contar palavras")
        print("3 - Palavras mais usadas (5)")
        print("4 - Estatísticas gerais (total de caracteres e palavras)")
        print("5 - Maior palavra")
        print("6 - Sair")

        escolhas = input("Digite os números: ").split()

        if "6" in escolhas:
            print("👋 Saindo...")
            break

        texto = input("\nDigite o texto:\n")

        # limpar texto uma vez só
        texto_limpo = limpar_texto(texto)

        palavras = None
        if any(op in escolhas for op in ["2", "3", "4", "6"]):
            palavras = contar_palavras(texto_limpo)

        if "1" in escolhas:
            caracteres = contar_caracteres(texto)
            print("\n🧾 Contagem de caracteres:")
            for char, count in caracteres.items():
                print(f"'{char}': {count}")

        if "2" in escolhas:
            print("\n🧠 Contagem de palavras:")
            for palavra, count in palavras.items():
                print(f"{palavra}: {count}")

        if "3" in escolhas:
            top = mostrar_top_palavras(palavras)
            print("\n🔥 Palavras mais usadas:")
            for palavra, count in top:
                print(f"{palavra}: {count}")

        if "4" in escolhas:
            estatisticas(texto_limpo)

        if "5" in escolhas:
            maior_palavra(texto_limpo)


if __name__ == "__main__":
    menu()

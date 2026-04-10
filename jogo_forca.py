import requests
import random

# -------------------------------------------------------
# Busca as palavras da API
# -------------------------------------------------------
url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'

try:
    resposta = requests.get(url, timeout=5)
    data = resposta.json()
except Exception:
    print("⚠️  Sem conexão com a API. Usando palavras locais.")
    data = [
        {"palavra": "python",     "dica": "Linguagem de programação famosa"},
        {"palavra": "javascript", "dica": "Linguagem da web"},
        {"palavra": "android",    "dica": "Sistema operacional mobile do Google"},
        {"palavra": "firebase",   "dica": "Banco de dados em nuvem do Google"},
        {"palavra": "github",     "dica": "Plataforma de versionamento de código"},
    ]

# -------------------------------------------------------
# Desenho da forca por estágio (0 = salvo, 6 = morto)
# -------------------------------------------------------
FORCA = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]

MAX_ERROS = 6

# -------------------------------------------------------
# Funções auxiliares
# -------------------------------------------------------

def mostrar_palavra(palavra_secreta, letras_corretas):
    """Mostra a palavra com _ para letras não descobertas"""
    exibicao = ""
    for letra in palavra_secreta:
        if letra in letras_corretas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    return exibicao.strip()


def palavra_completa(palavra_secreta, letras_corretas):
    """Verifica se todas as letras foram descobertas"""
    return all(letra in letras_corretas for letra in palavra_secreta)


def jogar():
    # Sorteia palavra e dica
    valor_secreto  = random.choice(data)
    palavra_secreta = valor_secreto['palavra'].lower()
    dica            = valor_secreto['dica']

    letras_corretas = set()
    letras_erradas  = set()
    pontuacao       = 0

    print("\n" + "=" * 45)
    print("       🎮  JOGO DA FORCA  🎮")
    print("=" * 45)
    print(f"📝 Dica: {dica}")
    print(f"🔤 A palavra tem {len(palavra_secreta)} letras\n")

    while len(letras_erradas) < MAX_ERROS:
        erros = len(letras_erradas)

        # Mostra forca
        print(FORCA[erros])

        # Mostra progresso da palavra
        print("Palavra: ", mostrar_palavra(palavra_secreta, letras_corretas))

        # Mostra letras já tentadas
        if letras_erradas:
            print(f"❌ Letras erradas ({erros}/{MAX_ERROS}): {' '.join(sorted(letras_erradas))}")
        if letras_corretas:
            print(f"✅ Letras corretas: {' '.join(sorted(letras_corretas))}")

        # Recebe chute
        print()
        chute = input("Digite uma letra (ou a palavra inteira): ").lower().strip()

        # Validação
        if not chute:
            print("⚠️  Digite algo!")
            continue

        # Tentou a palavra inteira
        if len(chute) > 1:
            if chute == palavra_secreta:
                pontuacao = (MAX_ERROS - erros) * 10
                print(FORCA[0])
                print(f"\n🎉 PARABÉNS! Você acertou a palavra: '{palavra_secreta}'!")
                print(f"⭐ Pontuação: {pontuacao} pontos")
                return
            else:
                print(f"❌ '{chute}' não é a palavra certa!")
                letras_erradas.add(f"[{chute}]")
                continue

        # Tentou uma letra
        if len(chute) != 1 or not chute.isalpha():
            print("⚠️  Digite apenas uma letra!")
            continue

        if chute in letras_corretas or chute in letras_erradas:
            print(f"⚠️  Você já tentou a letra '{chute}'!")
            continue

        if chute in palavra_secreta:
            letras_corretas.add(chute)
            print(f"✅ Boa! A letra '{chute}' está na palavra!")

            # Verificar vitória
            if palavra_completa(palavra_secreta, letras_corretas):
                pontuacao = (MAX_ERROS - len(letras_erradas)) * 10
                print(FORCA[0])
                print(f"\n🎉 PARABÉNS! Você completou a palavra: '{palavra_secreta}'!")
                print(f"⭐ Pontuação: {pontuacao} pontos")
                return
        else:
            letras_erradas.add(chute)
            print(f"❌ A letra '{chute}' não está na palavra!")

    # Perdeu
    print(FORCA[MAX_ERROS])
    print(f"\n💀 Você perdeu! A palavra secreta era: '{palavra_secreta}'")
    print("⭐ Pontuação: 0 pontos")


# -------------------------------------------------------
# Loop principal
# -------------------------------------------------------
def main():
    print("\n╔══════════════════════════════════════════╗")
    print("║         🎮  JOGO DA FORCA  🎮            ║")
    print("║     Adivinhe a palavra tecnológica!      ║")
    print("╚══════════════════════════════════════════╝")

    while True:
        jogar()
        print()
        jogar_novamente = input("🔄 Jogar novamente? (S/N): ").upper().strip()
        if jogar_novamente != "S":
            print("\n👋 Obrigado por jogar! Até a próxima!")
            break


if __name__ == "__main__":
    main()

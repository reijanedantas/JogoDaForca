# 🎮 Jogo da Forca

> Jogo da forca em Python com palavras tecnológicas obtidas de uma API

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Imersão IA](https://img.shields.io/badge/Imersão-IA%20Alura-purple)

---

## 📌 Sobre o Projeto

Jogo da forca desenvolvido em Python durante a **Imersão IA da Alura**. O jogador tenta adivinhar palavras tecnológicas obtidas de uma API externa, com dicas, múltiplas tentativas e desenho da forca no terminal.

---

## ✨ Funcionalidades

- 🌐 Palavras e dicas buscadas de uma API real
- 🔤 Tentativas letra por letra ou palavra inteira
- ❌ Desenho da forca atualizado a cada erro (6 estágios)
- 📋 Histórico de letras corretas e erradas
- ⭐ Sistema de pontuação
- 📴 Fallback com palavras locais se sem internet
- 🔄 Opção de jogar novamente

---

## 🎮 Como Jogar

```
╔══════════════════════════════════════════╗
║         🎮  JOGO DA FORCA  🎮            ║
║     Adivinhe a palavra tecnológica!      ║
╚══════════════════════════════════════════╝

📝 Dica: Linguagem de programação famosa
🔤 A palavra tem 6 letras

   -----
   |   |
       |
       |
       |
       |
=========

Palavra:  _ _ _ _ _ _
Digite uma letra (ou a palavra inteira): p
✅ Boa! A letra 'p' está na palavra!
```

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.x instalado
- Biblioteca `requests`

### Instalar dependências
```bash
pip install requests
```

### Executar
```bash
python jogo_forca.py
```

---

## 🏗️ Estrutura do Projeto

```
JogoDaForca/
└── jogo_forca.py   ← código principal
```

---

## ⚙️ Como Funciona

```
Busca palavras da API
        ↓
Sorteia palavra + dica aleatória
        ↓
Jogador tenta letras ou a palavra
        ↓
Acertou? → 🎉 Vitória + Pontuação
Errou 6x? → 💀 Derrota
        ↓
Jogar novamente?
```

### Sistema de Pontuação
A pontuação é calculada pelos erros que sobraram:
```
Pontuação = (6 - número de erros) × 10
```
Exemplo: acertou com 2 erros → `(6 - 2) × 10 = 40 pontos`

---

## 🌐 API Utilizada

```
https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json
```

Cada item da API contém:
```json
{
  "palavra": "python",
  "dica": "Linguagem de programação famosa"
}
```

---

## 👩‍💻 Autora

**Reijane Dantas**
Imersão IA — Alura

---

## 📄 Licença

Este projeto foi desenvolvido para fins de aprendizado.


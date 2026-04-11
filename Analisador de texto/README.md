# 🧾 Analisador de Texto CLI

## 📌 Descrição do problema

Muitos estudantes e usuários em geral têm dificuldade em analisar seus próprios textos, especialmente para identificar repetições excessivas, estrutura básica e padrões de escrita. Isso pode impactar negativamente na qualidade de redações, trabalhos acadêmicos e comunicação escrita.

## 💡 Proposta da solução

O **Analisador de Texto CLI** é uma aplicação simples em Python que permite ao usuário analisar textos diretamente pelo terminal. A ferramenta fornece informações úteis como contagem de palavras, caracteres, frequência de termos e identificação de repetições, auxiliando na melhoria da escrita.

## 👥 Público-alvo

* Estudantes do ensino médio e superior
* Pessoas que produzem textos com frequência
* Usuários que desejam uma ferramenta simples e rápida de análise textual

## ⚙️ Funcionalidades principais

* Contagem de caracteres
* Contagem de palavras
* Identificação das palavras mais usadas
* Estatísticas gerais do texto
* Identificação da maior palavra
* Interface interativa via CLI com seleção múltipla de funções

## 🛠️ Tecnologias utilizadas

* Python 3.x
* Biblioteca padrão (`string`)
* pytest (testes automatizados)
* flake8

## 📦 Instalação

```bash
git clone https://github.com/seu-usuario/analisador-texto-cli.git
cd analisador-texto-cli
pip install -r requirements.txt
```

## ▶️ Execução

```bash
python app/main.py
```

## 🧪 Executar testes

```bash
python -m pytest
```

## 🔢 Versão atual

v1.0.0

## 📁 Estrutura do projeto

```
analisador-texto-cli/
│
├── app/
│   └── main.py
│
├── tests/
│   └── test_app.py
│
├── README.md
└── requirements.txt 
```

## 🧠 Como usar

1. Execute o programa
2. Escolha as funcionalidades digitando os números (ex: `1 3 5`)
3. Insira o texto
4. Visualize os resultados no terminal

## 🎯 Exemplo de uso

```
===================================
🧾 ANALISADOR DE TEXTO
===================================
Escolha as funções (separadas por espaço):
1 - Contar caracteres
2 - Contar palavras
3 - Palavras mais usadas (5)
4 - Estatísticas gerais (total de caracteres e palavras)
5 - Maior palavra
6 - Sair
Digite os números:  1 3 5

Digite o texto:
Hello, World!

🧾 Contagem de caracteres:
'H': 1
'e': 1
'l': 3
'o': 2
',': 1
' ': 1
'W': 1
'r': 1
'd': 1
'!': 1

🔥 Palavras mais usadas:
hello: 1
world: 1

🔎 Maior palavra: hello
```

## 🧪 Testes automatizados

O projeto inclui testes automatizados utilizando `pytest` para validar as principais funções do sistema, garantindo confiabilidade e correto funcionamento.

## 👤 Autor

Guilherme Ribeiro
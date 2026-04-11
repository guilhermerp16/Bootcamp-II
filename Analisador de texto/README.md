# 🧾 Analisador de Texto CLI

## 📌 Descrição do problema

Muitas pessoas, como estudantes, escritores iniciantes e profissionais, têm dificuldade em analisar rapidamente a qualidade de um texto, como quantidade de palavras, frequência de termos e estrutura básica. Isso pode prejudicar estudos, produção de conteúdo e organização de informações.

## 💡 Proposta da solução

O Analisador de Texto é uma aplicação CLI simples que permite analisar textos de forma rápida e prática, fornecendo informações úteis como contagem de palavras, caracteres e outras métricas relevantes.

## 👥 Público-alvo

* Estudantes
* Escritores
* Qualquer pessoa que trabalhe com texto
  
## ⚙️ Funcionalidades
*  Contagem de palavras
*  Contagem de caracteres
*  Análise básica de texto
*  Interface via linha de comando (CLI) 

## 🛠️ Tecnologias utilizadas

* Python 3.13.12
* GitHub Actions (CI)
* pytest (testes automatizados)
* flake8 (linting)

## 📦 Instalação

```bash
git clone https://github.com/guilhermerp16/Bootcamp-II.git
cd Bootcamp-II/"Analisador de texto"
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

# 🖨️ Prints ZPL Fulfillment

Projeto para ajudar nas impressões de etiquetas de produtos Fulfillment (Mercado Livre). Ele gerencia a quantidade exata de etiquetas para cada remessa, salvando histórico de impressões e operações em geral.

## ❓ O que é ZPL?

ZPL (Zebra Programming Language) é uma linguagem de marcação usada para gerar etiquetas em impressoras Zebra. O sistema gera comandos ZPL com base nos dados dos produtos, permitindo impressões precisas e automatizadas.

---

## ⚙️ Funcionalidades

- Leitura automática de arquivos TXT exportados do Mercado Livre.
- Geração e impressão de etiquetas no formato ZPL (Zebra Programming Language).
- Interface gráfica para entrada de dados adicionais (EAN, validade, etc).
- Armazenamento de histórico em banco de dados (`ECOMM.etiqueta_full`).
- Gerenciamento de usuários via `.env`.

## 📁 Estrutura do Projeto

```bash
project_name/
│
├── app/                           # Camada de Interface com o Usuário
│   ├── __init__.py
│   ├── ui/                        # Componentes da interface (CustomTkinter)
│   │   ├── __init__.py
│   │   ├── login_screen.py        # Tela de login
│   │   ├── main_screen.py         # Tela principal após login
│   │   ├── input_data_screen.py   # Tela para entrada de dados (EAN, Data de validade, etc.)
│   │   └── ...                    # Outros componentes da UI
│   └── app.py                     # Função principal que inicializa o app e as telas
│
├── domain/                        # Camada de Entidades
│   ├── __init__.py
│   ├── label.py                   # Entidade que representa a etiqueta (ZPL)
│   └── product.py                 # Entidade que representa o produto (EAN, Data de validade, etc.)
│
├── use_cases/                     # Camada de Casos de Uso
│   ├── __init__.py
│   ├── label_processing.py        # Função que processa a lista de etiquetas ZPL
│   └── user_input_processing.py   # Função para tratar os dados inseridos pelo usuário (EAN, etc.)
│
├── interfaces/                    # Camada de Interfaces (Abstração)
│   ├── __init__.py
│   ├── label_repository.py        # Interface para persistir ou manipular dados de etiquetas
│   └── product_repository.py      # Interface para persistir ou manipular dados dos produtos
│
├── infrastructure/                # Camada de Infraestrutura
│   ├── __init__.py
│   ├── label_repository_in_memory.py   # Implementação em memória do repositório de etiquetas
│   └── product_repository_in_memory.py # Implementação em memória do repositório de produtos
│
├── config/                        # Configurações do projeto
│   ├── __init__.py
│   └── settings.py                # Arquivo com configurações gerais (ex: caminho de arquivos, variáveis de ambiente)
│
├── tests/                         # Testes unitários e de integração
│   ├── __init__.py
│   ├── test_label_processing.py   # Testes para a camada de processamento de etiquetas
│   ├── test_user_input_processing.py  # Testes para a camada de entrada de dados do usuário
│   └── test_app.py                # Testes para a camada de interface com o usuário (UI)
│
└── requirements.txt               # Dependências do projeto
```

## 📝 Exemplo de uso

1. Gerar arquivo no Mercado Livre
  - Acesse a sua conta no Mercado Livre.
  - Faça o procedimento de Fulfillment e exporte o arquivo de etiquetas.
  - O arquivo será salvo com um nome como:
    - Envio-42901219-Etiquetas-do-produtos.txt

2. Salve o arquivo no diretório correto
 - Coloque o arquivo em:

```bash
./update_etiquetas_db/data/Envio-XXXXXX-Etiquetas-do-produtos.txt
```

📄 Exemplo de conteúdo do arquivo TXT

```txt
^XA
^CI28
^LH0,0
^FO25,15^BY2,,0^BCN,55,N,N^FDYAXU24015^FS
^FT110,98^A0N,22,22^FH^FDYAXU24015^FS
^FT109,98^A0N,22,22^FH^FDYAXU24015^FS
^FO22,115^A0N,18,18^FB300,2,0,L^FH^FDSensor Nivel Gm Celta Prisma 2009 2012 2017 Flex Bosch^FS
^FO22,153^A0N,18,18^FB300,1,0,L^FH^FD^FS
^FO21,153^A0N,18,18^FB300,1,0,L^FH^FD^FS
^FO22,175^A0N,18,18^FH^FDSKU: 018223^FS
^FO22,175^A0N,18,18^FH^FD^FS
^PQ30,0,1,Y^XZ
^XA
```

## 🔐 Configuração de Usuários (`.env`)

```env
# Formato: CODIGO:Senha;CODIGO2:Senha2;...
USERS=2121:NaoXingueMinhaMae;2122:SenhaSegura
```

## 🖥️ Execução

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python .\src\prints_zpls_fulfillment\app\app.py
```

Inserir informacoes no Banco de Dados:

```bash
python .\src\update_etiquetas_db\main.py
```

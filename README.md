# """""

## Arquitetura

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

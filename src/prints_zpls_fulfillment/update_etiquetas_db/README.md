```bash
my_project/
│
├── src/
│   ├── __init__.py
│   ├── entities/
│   │   ├── __init__.py
│   │   └── etiqueta.py          # Contém a classe 'Etiqueta'
│   │
│   ├── use_cases/
│   │   ├── __init__.py
│   │   └── gerenciar_etiquetas.py # Contém o caso de uso 'GerenciarEtiquetas'
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── i_repositorio_etiquetas.py  # Interface do repositório
│   │   └── handler_postgres.py        # Implementação do repositório para o Postgres
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   └── queries.py               # Contém as queries SQL
│   │
│   └── main.py                    # Arquivo de entrada do projeto (onde o fluxo é orquestrado)
│
├── data/
│   └── Envio-42901219-Etiquetas-do-produtos.txt  # Arquivo de exemplo com as etiquetas
│
├── requirements.txt              # Dependências do projeto
├── README.md                     # Documentação do projeto
└── .gitignore                    # Arquivo de configuração do git (caso use controle de versão)
```

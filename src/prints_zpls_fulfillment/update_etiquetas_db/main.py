"""---"""
from prints_zpls_fulfillment.update_etiquetas_db.repositories.handler_postgres import HandlerPostgres
from prints_zpls_fulfillment.update_etiquetas_db.use_cases.gerenciar_etiquetas import GerenciarEtiquetas

def main():

    # Defina o caminho do arquivo
    path_etiqueta = 'src/prints_zpls_fulfillment/update_etiquetas_db/data/Envio-42901219-Etiquetas-do-produtos.txt'

    # Instancie o repositório (HandlerPostgres)
    repositorio_postgres = HandlerPostgres()

    # Crie o caso de uso
    gerenciar_etiquetas = GerenciarEtiquetas(repositorio_postgres)

    # Execute o processo
    gerenciar_etiquetas.executar(path_etiqueta)

if __name__ == '__main__':
    main()

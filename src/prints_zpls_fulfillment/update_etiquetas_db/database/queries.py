queries = {
    'get_rel': """
            SELECT
                *
            FROM "ECOMM".etiqueta_full
        """,
    'ml_info': """
            SELECT
                ml_info.item_id,
                ml_info.codpro,
                ml_info.sku as codref,
                ml_info.inventory_id as cod_ml
            FROM
                "ECOMM".ml_info
            WHERE
                ml_info.fulfillment
        """,
    'etiquetas': """
            SELECT
                *
            FROM
                "ECOMM".etiqueta_full
            WHERE
                NOT etq_impressa
            ORDER BY (id, etq_impressa, data_emissao, idx_etq)
        """,
    'prd_gtin_siac': """
            SELECT
                cd_produto as codpro,
                cd_barras as ean,
                qt_embala as embala,
                dt_cadast as data_cadastro
            FROM
                "D-1".prd_gtin
        """,
}

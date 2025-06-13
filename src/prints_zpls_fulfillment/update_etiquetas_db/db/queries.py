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
            ml_info.inventory_id as cod_ml,
            ml_info.ean
        FROM
            "ECOMM".ml_info
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
}

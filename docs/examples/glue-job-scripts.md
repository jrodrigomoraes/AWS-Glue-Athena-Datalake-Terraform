# Glue Job Script - Transformação e Integração de Dados

Este documento explica o funcionamento do script

## Objetivo do Script

- Realizar a **extração de dados normalizados** do Glue Data Catalog (alimentado por arquivos CSV no S3)
- Executar **joins entre tabelas** relacionadas a clientes, vendas, itens, produtos e vendedores
- Aplicar **mapeamento de colunas e transformação de schema**
- Avaliar a **qualidade dos dados** com regras básicas (ex: presença de colunas)
- Escrever o resultado no S3 como arquivos **Parquet particionados por `status`**
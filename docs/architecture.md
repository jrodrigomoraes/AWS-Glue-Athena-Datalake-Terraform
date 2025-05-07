# Arquitetura da Solução

A arquitetura segue o fluxo abaixo:

1. Dados CSV armazenados no S3.
2. Glue Crawler descobre o schema e cria metadados no Glue Catalog.
3. Glue Job transforma os dados e salva no formato Parquet particionado.
4. Um segundo Glue Crawler lê os dados Parquet e registra nova tabela no Catalog.
5. Athena consulta os dados particionados diretamente do Data Lake.

Segue esquema final transformado e executado pelo Job.

![Esquema Dados](imgs/EsquemaJob.jpg)

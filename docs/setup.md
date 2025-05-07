# Setup do Projeto

## Pré-requisitos

- Conta AWS
- AWS CLI configurado
- Terraform instalado

## Etapas

1. Clone o repositório.
2. Execute `terraform init && terraform apply` para criar os recursos.
3. Faça upload dos arquivos CSV no bucket `sourcedata/`.
4. Execute o primeiro Glue Crawler.
5. Rode o Glue Job via console ou trigger.
6. Execute o segundo Glue Crawler para os arquivos Parquet.
7. Acesse o Athena e execute as queries de análise.

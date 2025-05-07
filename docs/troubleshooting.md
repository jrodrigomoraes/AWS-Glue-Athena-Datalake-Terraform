# Troubleshooting

## Glue Job falha com `AccessDeniedException`

Verifique se a IAM Role atribuída ao Glue tem permissão para acessar os buckets S3.

## Athena retorna "table not found"

Confirme se:
- O segundo Crawler foi executado.
- O banco de dados foi selecionado corretamente.
- O nome da tabela está certo.
# Troubleshooting

## Glue Job falha com `AccessDeniedException`

Verifique se a IAM Role atribuída ao Glue tem permissão para acessar os buckets S3.

## Athena retorna "table not found"

Confirme se:
- O segundo Crawler foi executado.
- O banco de dados foi selecionado corretamente.
- O nome da tabela está certo.

## Additional Notes

- Always double-check the AWS region when creating Glue resources and running Athena queries.
- If your IAM Role does not have permissions for AWS Glue, consider attaching the `AWSGlueServiceRole` managed policy temporarily for testing.
- Make sure your S3 bucket and Glue/Athena services are in the **same region** to avoid query or job failures.

resource "aws_glue_catalog_database" "vendas" {
  name = var.glue_database_csv
}

resource "aws_glue_catalog_database" "vendas_datalake" {
  name = var.glue_database_parquet
}

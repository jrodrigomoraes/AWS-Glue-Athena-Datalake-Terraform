resource "aws_glue_crawler" "crawler_vendas" {
  name          = "crawler_vendas"
  database_name = var.glue_database_csv
  role          = aws_iam_role.glue_service_role.arn

  s3_target {
    path = "s3://${var.bucket_name}/sourcedata/"
  }

  schema_change_policy {
    update_behavior = "UPDATE_IN_DATABASE"
    delete_behavior = "DEPRECATE_IN_DATABASE"
  }
}

resource "aws_glue_crawler" "crawler_datalake" {
  name          = "crawler_datalake"
  database_name = var.glue_database_parquet
  role          = aws_iam_role.glue_service_role.arn

  s3_target {
    path = "s3://${var.bucket_name}/datalake/"
  }

  schema_change_policy {
    update_behavior = "UPDATE_IN_DATABASE"
    delete_behavior = "DEPRECATE_IN_DATABASE"
  }
}

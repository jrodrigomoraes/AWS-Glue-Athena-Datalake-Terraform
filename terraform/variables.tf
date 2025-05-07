variable "aws_region" {
  default = "us-east-1"
}

variable "bucket_name" {
  default = "datalakeengdadosjr"
}

variable "glue_role_name" {
  default = "glue_acesso"
}

variable "glue_database_csv" {
  default = "vendas"
}

variable "glue_database_parquet" {
  default = "vendas_datalake"
}

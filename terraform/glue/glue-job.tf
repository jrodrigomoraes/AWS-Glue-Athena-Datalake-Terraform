resource "aws_glue_job" "job_transform_vendas" {
  name     = "job-transform-vendas"
  role_arn = aws_iam_role.glue_service_role.arn

  command {
    name            = "glueetl"
    script_location = "s3://${var.bucket_name}/scripts/transform-script.py"
    python_version  = "3"
  }

  default_arguments = {
    "--TempDir" = "s3://${var.bucket_name}/temp/"
    "--job-language" = "python"
    "--enable-continuous-cloudwatch-log" = "true"
  }

  glue_version = "3.0"
  max_capacity = 2
  number_of_workers = 2
  worker_type = "G.1X"
}

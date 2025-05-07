output "bucket_name" {
  value = var.bucket_name
}

output "glue_role" {
  value = aws_iam_role.glue_service_role.name
}

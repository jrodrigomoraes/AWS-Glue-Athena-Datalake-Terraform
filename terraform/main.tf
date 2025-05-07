provider "aws" {
  region = var.aws_region
}

module "iam" {
  source = "./iam"
}

module "s3" {
  source = "./s3"
}

module "glue" {
  source = "./glue"
}

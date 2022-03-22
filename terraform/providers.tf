# providers.tf

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  profile = "skyboydev"
  region  = var.aws_region
}

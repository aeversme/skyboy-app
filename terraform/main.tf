# main.tf

resource "aws_vpc" "skyboy_vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "skyboy_vpc"
  }
}

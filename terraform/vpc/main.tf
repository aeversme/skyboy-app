# vpc/main.tf

locals {
  azs = data.aws_availability_zones.available.names
}

data "aws_availability_zones" "available" {}

resource "random_id" "random" {
  byte_length = 2
}

resource "aws_vpc" "skyboy_vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  lifecycle {
    create_before_destroy = true
  }

  tags = {
    Name = "skyboy_vpc_${random_id.random.dec}"
  }
}

resource "aws_internet_gateway" "skyboy_ig" {
  vpc_id = aws_vpc.skyboy_vpc.id

  tags = {
    Name = "skyboy_igw_${random_id.random.dec}"
  }
}

resource "aws_route_table" "skyboy_public_rt" {
  vpc_id = aws_vpc.skyboy_vpc.id

  tags = {
    Name = "skyboy_public_rt"
  }
}

resource "aws_route" "default_route" {
  route_table_id         = aws_route_table.skyboy_public_rt.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.skyboy_ig.id
}

resource "aws_default_route_table" "skyboy_vpc_default_rt" {
  default_route_table_id = aws_vpc.skyboy_vpc.default_route_table_id

  tags = {
    Name = "skyboy_default_rt"
  }
}

resource "aws_subnet" "skyboy_public_subnet" {
  count                   = length(local.azs)
  cidr_block              = cidrsubnet(var.vpc_cidr, 8, count.index + 1)
  vpc_id                  = aws_vpc.skyboy_vpc.id
  map_public_ip_on_launch = true
  availability_zone       = local.azs[count.index]

  tags = {
    Name = "skyboy_public_subnet_${count.index + 1}"
  }
}

resource "aws_route_table_association" "skyboy_public_assoc" {
  count          = length(local.azs)
  subnet_id      = aws_subnet.skyboy_public_subnet[count.index].id
  route_table_id = aws_route_table.skyboy_public_rt.id
}

resource "aws_security_group" "skyboy_service_sg" {
  name        = "skyboy_service_sg"
  description = "Security group for Skyboy ECS service"
  vpc_id      = aws_vpc.skyboy_vpc.id

  tags = {
    Name = "skyboy_service_sg"
  }
}

resource "aws_security_group_rule" "service_ingress" {
  type                     = "ingress"
  from_port                = 8501
  to_port                  = 8501
  protocol                 = "tcp"
  source_security_group_id = aws_security_group.skyboy_lb_sg.id
  security_group_id        = aws_security_group.skyboy_service_sg.id
}

resource "aws_security_group_rule" "service_egress" {
  type              = "egress"
  from_port         = 0
  to_port           = 65535
  protocol          = "-1"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.skyboy_service_sg.id
}

resource "aws_security_group" "skyboy_lb_sg" {
  name        = "skyboy_lb_sg"
  description = "Security group for Skyboy load balancer"
  vpc_id      = aws_vpc.skyboy_vpc.id

  tags = {
    Name = "skyboy_lb_sg"
  }
}

resource "aws_security_group_rule" "lb_http_ingress" {
  type              = "ingress"
  from_port         = 80
  to_port           = 80
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.skyboy_lb_sg.id
}

resource "aws_security_group_rule" "lb_https_ingress" {
  type              = "ingress"
  from_port         = 443
  to_port           = 443
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.skyboy_lb_sg.id
}

resource "aws_security_group_rule" "lb_egress" {
  type              = "egress"
  from_port         = 0
  to_port           = 65535
  protocol          = "-1"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.skyboy_lb_sg.id
}

# root/main.tf

module "vpc" {
  source   = "./vpc"
  vpc_cidr = "10.14.0.0/16"
}

module "loadbalancing" {
  source     = "./loadbalancing"
  lb_sg      = module.vpc.lb_sg
  lb_subnets = module.vpc.lb_subnets
}

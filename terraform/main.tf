# root/main.tf

module "vpc" {
  source   = "./vpc"
  vpc_cidr = "10.14.0.0/16"
}

module "loadbalancing" {
  source                 = "./loadbalancing"
  lb_sg                  = module.vpc.lb_sg
  lb_subnets             = module.vpc.lb_subnets
  tg_port                = 8501
  tg_protocol            = "HTTP"
  vpc_id                 = module.vpc.vpc_id
  lb_healthy_threshold   = 2
  lb_unhealthy_threshold = 2
  lb_timeout             = 3
  lb_interval            = 30
  fwd_listener_port      = 80
  fwd_listener_protocol  = "HTTP"
}

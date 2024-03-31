# root/main.tf

module "vpc" {
  source   = "./vpc"
  vpc_cidr = "10.14.0.0/16"
}

module "iam" {
  source = "./iam"
}

module "containers" {
  source              = "./containers"
  capacity_providers  = ["FARGATE", "FARGATE_SPOT"]
  service_subnets     = module.vpc.lb_subnets
  service_sg          = module.vpc.service_sg
  service_launch_type = "FARGATE"
  task_cpu            = 256
  task_memory         = 1024
  container_name      = "skyboy"
  container_port      = 8501
  task_role_arn       = module.iam.ecs_task_role_arn
}

module "autoscaling" {
  source             = "./autoscaling"
  cluster_name       = module.containers.cluster_name
  service_name       = module.containers.service_name
  scale_dimension    = "ecs:service:DesiredCount"
  namespace          = "ecs"
  max_capacity       = 2
  min_capacity       = 0
  scale_in_cooldown  = 60
  scale_out_cooldown = 60
  cpu_target         = 80
  mem_target         = 80
}

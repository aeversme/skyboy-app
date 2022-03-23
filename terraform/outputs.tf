# root/outputs.tf

output "load_balancer_endpoint" {
  value = module.loadbalancing.lb_endpoint
}

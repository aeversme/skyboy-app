# containers/outputs.tf

output "cluster_name" {
  value = aws_ecs_cluster.skyboy_cluster.name
}

output "service_name" {
  value = aws_ecs_service.skyboy_service.name
}

# vpc/outputs.tf

output "vpc_id" {
  value = aws_vpc.skyboy_vpc.id
}

output "lb_sg" {
  value = [aws_security_group.skyboy_lb_sg.id]
}

output "service_sg" {
  value = aws_security_group.skyboy_service_sg.id
}

output "lb_subnets" {
  value = [for subnet in aws_subnet.skyboy_public_subnet : subnet.id]
}

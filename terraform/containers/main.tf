# containers/main.tf

resource "aws_ecs_cluster" "skyboy_cluster" {
  name = "skyboycluster"

  tags = {
    Name = "skyboy_ecs_cluster"
  }
}

resource "aws_ecs_cluster_capacity_providers" "skyboy_cluster_providers" {
  cluster_name = aws_ecs_cluster.skyboy_cluster.name

  capacity_providers = var.capacity_providers
}

resource "aws_ecs_service" "skyboy_service" {
  name            = "skyboyservice"
  cluster         = aws_ecs_cluster.skyboy_cluster.id
  task_definition = aws_ecs_task_definition.skyboy_task.arn
  desired_count   = 1
  launch_type     = var.service_launch_type

  network_configuration {
    subnets          = var.service_subnets
    security_groups  = [var.service_sg]
    assign_public_ip = true
  }

  load_balancer {
    target_group_arn = var.target_group_arn
    container_name   = var.container_name
    container_port   = var.container_port
  }
}

resource "aws_ecs_task_definition" "skyboy_task" {
  family                   = "skyboytask"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = var.task_cpu
  memory                   = var.task_memory
  task_role_arn            = var.task_role_arn
  execution_role_arn       = var.task_role_arn

  container_definitions = file("${path.module}/task-definitions/skyboy.json")
}


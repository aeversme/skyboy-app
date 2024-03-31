# containers/main.tf

resource "aws_ecs_cluster" "skyboy_cluster" {
  name = "skyboy-cluster"

  tags = {
    Name = "skyboy_ecs_cluster"
  }
}

resource "aws_ecs_cluster_capacity_providers" "skyboy_cluster_providers" {
  cluster_name = aws_ecs_cluster.skyboy_cluster.name

  capacity_providers = var.capacity_providers
}

resource "aws_ecs_service" "skyboy_service" {
  name            = "skyboy-service"
  cluster         = aws_ecs_cluster.skyboy_cluster.id
  task_definition = aws_ecs_task_definition.skyboy_task.arn
  desired_count   = 1
  launch_type     = var.service_launch_type

  network_configuration {
    subnets          = var.service_subnets
    security_groups  = [var.service_sg]
    assign_public_ip = true
  }

  lifecycle {
    ignore_changes = [desired_count]
  }
}

resource "aws_ecs_task_definition" "skyboy_task" {
  family                   = "skyboy-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = var.task_cpu
  memory                   = var.task_memory
  task_role_arn            = var.task_role_arn
  execution_role_arn       = var.task_role_arn

  container_definitions = file("${path.module}/task-definitions/skyboy.json")
}


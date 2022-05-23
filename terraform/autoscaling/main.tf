# autoscaling/main.tf

resource "aws_appautoscaling_target" "skyboy_scaling_target" {
  max_capacity       = 4
  min_capacity       = 1
  resource_id        = "service/${var.cluster_name}/${var.service_name}"
  scalable_dimension = "ecs:service:DesiredCount"
  service_namespace  = "ecs"
}

resource "aws_appautoscaling_policy" "skyboy_cpu_policy" {
  name               = "cpu-autoscaling"
  policy_type        = "TargetTrackingScaling"
  resource_id        = aws_appautoscaling_target.skyboy_scaling_target.resource_id
  scalable_dimension = aws_appautoscaling_target.skyboy_scaling_target.scalable_dimension
  service_namespace  = aws_appautoscaling_target.skyboy_scaling_target.service_namespace

  target_tracking_scaling_policy_configuration {
    target_value       = 80
    scale_in_cooldown  = 60
    scale_out_cooldown = 60

    predefined_metric_specification {
      predefined_metric_type = "ECSServiceAverageCPUUtilization"
    }
  }
}

resource "aws_appautoscaling_policy" "skyboy_memory_policy" {
  name               = "memory-autoscaling"
  policy_type        = "TargetTrackingScaling"
  resource_id        = aws_appautoscaling_target.skyboy_scaling_target.resource_id
  scalable_dimension = aws_appautoscaling_target.skyboy_scaling_target.scalable_dimension
  service_namespace  = aws_appautoscaling_target.skyboy_scaling_target.service_namespace

  target_tracking_scaling_policy_configuration {
    target_value       = 80
    scale_in_cooldown  = 60
    scale_out_cooldown = 60

    predefined_metric_specification {
      predefined_metric_type = "ECSServiceAverageMemoryUtilization"
    }
  }
}

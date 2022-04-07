# iam/outputs.tf

output "ecs_task_role_arn" {
  value = aws_iam_role.ecs_task_role.arn
}

# containers/variables.tf

variable "capacity_providers" {
  type = list(string)
}

variable "service_subnets" {
  type = list(string)
}

variable "service_sg" {
  type = string
}

variable "service_launch_type" {
  type = string
}

variable "task_cpu" {
  type = number
}

variable "task_memory" {
  type = number
}

variable "task_role_arn" {
  type = string
}

variable "container_name" {
  type = string
}

variable "container_port" {
  type = number
}

variable "target_group_arn" {
  type = string
}

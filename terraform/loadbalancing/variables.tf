# loadbalancing/variables.tf

variable "lb_subnets" {
  type = list(string)
}

variable "lb_sg" {
  type = list(string)
}

variable "tg_port" {
  type = number
}

variable "tg_protocol" {
  type = string
}

variable "vpc_id" {
  type = string
}

variable "lb_healthy_threshold" {
  type = number
}

variable "lb_unhealthy_threshold" {
  type = number
}

variable "lb_timeout" {
  type = number
}

variable "lb_interval" {
  type = number
}

# loadbalancing/variables.tf

variable "lb_subnets" {
  type = list(string)
}

variable "lb_sg" {
  type = list(string)
}

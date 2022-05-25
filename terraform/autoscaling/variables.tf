# autoscaling/variables.tf

variable "cluster_name" {
  type = string
}

variable "service_name" {
  type = string
}

variable "scale_dimension" {
  type = string
}

variable "namespace" {
  type = string
}

variable "max_capacity" {
  type = number
}

variable "min_capacity" {
  type = number
}

variable "scale_in_cooldown" {
  type = number
}

variable "scale_out_cooldown" {
  type = number
}

variable "cpu_target" {
  type = number
}

variable "mem_target" {
  type = number
}

# variables.tf

variable "vpc_cidr" {
  type        = string
  description = "The CIDR range for the VPC."
  default     = "10.14.0.0/16"
}

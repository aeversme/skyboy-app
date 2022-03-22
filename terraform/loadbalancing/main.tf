# loadbalancing/main.tf

resource "aws_lb" "skyboy_lb" {
  name            = "skyboylb"
  subnets         = var.lb_subnets
  security_groups = var.lb_sg
  idle_timeout    = 400
}

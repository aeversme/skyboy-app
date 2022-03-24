# loadbalancing/main.tf

resource "aws_lb" "skyboy_lb" {
  name            = "skyboylb"
  subnets         = var.lb_subnets
  security_groups = var.lb_sg
  idle_timeout    = 400
}

resource "aws_lb_target_group" "skyboy_tg" {
  name        = "skyboytg"
  port        = var.tg_port
  protocol    = var.tg_protocol
  target_type = "ip"
  vpc_id      = var.vpc_id

  lifecycle {
    create_before_destroy = true
  }

  health_check {
    healthy_threshold   = var.lb_healthy_threshold
    unhealthy_threshold = var.lb_unhealthy_threshold
    timeout             = var.lb_timeout
    interval            = var.lb_interval
  }
}

# this will change to port 443 when a certificate is set up
# a redirect listener will also be required (80 -> 443)
resource "aws_lb_listener" "skyboy_forward_listener" {
  load_balancer_arn = aws_lb.skyboy_lb.arn
  port              = var.fwd_listener_port
  protocol          = var.fwd_listener_protocol
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.skyboy_tg.arn
  }
}

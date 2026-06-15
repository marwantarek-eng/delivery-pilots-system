resource "aws_ecr_repository" "pilot_svc" {
  name                 = "pilot-svc"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Name = "pilot-svc-repo"
  }
}

resource "aws_ecr_repository" "order_svc" {
  name                 = "order-svc"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Name = "order-svc-repo"
  }
}

# backends.tf

terraform {
  cloud {
    organization = "ae-cloud-dev"

    workspaces {
      name = "skyboy"
    }
  }
}

data "azuredevops_project" "project" {
  name = var.project_name
}

data "azuredevops_group" "reviewers" {
  project_id = data.azuredevops_project.project.id
  name       = var.reviewers_group_name
}

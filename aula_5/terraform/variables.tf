variable "project_name" {
  description = "The name of the Azure DevOps project"
  type        = string
}

variable "repository_name" {
  description = "The name of the Azure DevOps repository"
  type        = string
}

variable "default_branch" {
  description = "The default branch of the repository. ex: master"
  default     = "main"
  type        = string
}

variable "reviewers_group_name" {
  description = "The name of the Azure DevOps group that will be used as reviewers"
  type        = string
}

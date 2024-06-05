locals {
  full_default_branch_name = "refs/heads/${var.default_branch}"
}

resource "azuredevops_git_repository" "repository" {
  project_id = data.azuredevops_project.project.id
  name       = var.repository_name
  initialization {
    init_type = "Clean"
  }
}

resource "azuredevops_branch_policy_min_reviewers" "review_configuration" {
  project_id = data.azuredevops_project.project.id

  enabled  = true
  blocking = true

  settings {
    reviewer_count                         = 1
    submitter_can_vote                     = true
    last_pusher_cannot_approve             = false
    allow_completion_with_rejects_or_waits = false
    on_push_reset_approved_votes           = true

    scope {
      repository_id  = azuredevops_git_repository.repository.id
      repository_ref = local.full_default_branch_name
      match_type     = "Exact"
    }
  }
}

resource "azuredevops_branch_policy_comment_resolution" "configuration" {
  project_id = data.azuredevops_project.project.id

  enabled  = true
  blocking = true

  settings {
    scope {
      repository_id  = azuredevops_git_repository.repository.id
      repository_ref = local.full_default_branch_name
      match_type     = "Exact"
    }
  }
}

resource "azuredevops_branch_policy_auto_reviewers" "configuration" {
  project_id = data.azuredevops_project.project.id

  enabled  = true
  blocking = true

  settings {
    auto_reviewer_ids  = [data.azuredevops_group.reviewers.origin_id]
    submitter_can_vote = false
    message            = "It is required to have at least one DevOps team member to review the code."

    scope {
      repository_id  = azuredevops_git_repository.repository.id
      repository_ref = local.full_default_branch_name
      match_type     = "Exact"
    }
  }
}

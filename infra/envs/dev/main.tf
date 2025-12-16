provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_artifact_registry_repository" "repo" {
  location      = var.region
  repository_id = var.repo_name
  format        = "DOCKER"
}

resource "google_cloud_run_v2_service" "svc" {
  name     = var.service_name
  location = var.region

  template {
    containers {
      image = var.image
      ports { container_port = 8080 }
    }
  }
}

resource "google_cloud_run_v2_service_iam_member" "public" {
  location = google_cloud_run_v2_service.svc.location
  name     = google_cloud_run_v2_service.svc.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}

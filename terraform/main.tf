terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "quote_saver" {
  metadata {
    name = "quote-saver"
  }
}

resource "kubernetes_persistent_volume_claim" "postgres_pvc" {
  metadata {
    name      = "postgres-pvc"
    namespace = kubernetes_namespace.quote_saver.metadata[0].name
  }
  spec {
    access_modes = ["ReadWriteOnce"]
    resources {
      requests = {
        storage = "1Gi"
      }
    }
  }
}

resource "kubernetes_config_map" "quote_saver_config" {
  metadata {
    name      = "quote-saver-config"
    namespace = kubernetes_namespace.quote_saver.metadata[0].name
  }

  data = {
    REACT_APP_API_URL = "http://quote-api:5000"
    DATABASE_URL      = "postgresql://postgres:postgres@postgres-db:5432/quotes"
  }
}

resource "kubernetes_secret" "postgres_secret" {
  metadata {
    name      = "postgres-secret"
    namespace = kubernetes_namespace.quote_saver.metadata[0].name
  }

  data = {
    POSTGRES_USER     = base64encode("postgres")
    POSTGRES_PASSWORD = base64encode("postgres")
    POSTGRES_DB       = base64encode("quotes")
  }

  type = "Opaque"
} 
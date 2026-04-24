terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host = "npipe:////.//pipe//docker_engine"
}

resource "docker_image" "hello_world_api_service" {
  name         = "antonind5/py3.14-fastapi:latest"
  keep_locally = false
}

resource "docker_container" "hello_world_api_service" {
  image = docker_image.hello_world_api_service.image_id
  name  = "hello_world_api"
  ports {
    internal = 8000
    external = 8080
  }
}

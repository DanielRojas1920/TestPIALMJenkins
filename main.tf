terraform{
    required_providers{
        docker = {
            source  = "kreuzwerker/docker"
            version = "~> 3.0.1"
        }
    }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# Imagen y contenedor para la aplicación Django
resource "docker_image" "django_app" {
  name = "django"
  build {
    context    = "."
    dockerfile = "Dockerfile"
  }
}

resource "docker_container" "django_container" {
  image = "django_app"
  name  = "django_container"
  ports {
    internal = 8000
    external = 8000
  }

  command = ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
  depends_on = [docker_container.mysql_container]
}

# Imagen y contenedor para MySQL
resource "docker_container" "mysql_container" {
  name    = "mysql_database"
  image   = "mysql:5.7"  # Puedes usar una versión diferente si es necesario
  env = [
    "MYSQL_ROOT_PASSWORD=9WG\"\"u4:85M",
    "MYSQL_DATABASE=PIA_LMP",
    "MYSQL_USER=PIA_LMP",
    "MYSQL_PASSWORD=9WG\"\"u4:85M"
  ]
  ports {
    internal = 3306
    external = 3307
  }
}
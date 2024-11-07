# Usa la imagen base oficial de Python
FROM python:3.9

# Configura el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos para instalar dependencias
COPY requirements.txt /app/

RUN apt-get update && apt-get install -y \
    gcc \
    libmysqlclient-dev \
    python3-dev \

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el resto del código del proyecto
COPY . /app/

# Expone el puerto para el servidor Django
EXPOSE 8000
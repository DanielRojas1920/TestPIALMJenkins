# Usa la imagen base oficial de Python
FROM python:3

# Configura el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos para instalar dependencias
COPY requirements.txt /app/

# Instala las dependencias
RUN sudo pip install -r requirements.txt

# Copia el resto del código del proyecto
COPY . /app/

# Expone el puerto para el servidor Django
EXPOSE 8000
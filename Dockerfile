# Etapa 1: builder (instala dependencias Python)
FROM python:3.11-slim AS builder

WORKDIR /app

# Dependencias del sistema necesarias para compilar algunas libs (matplotlib / numpy)
RUN apt-get update && apt-get install -y \
    build-essential \
    libfreetype6-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar solo requerimientos para aprovechar la cache
COPY requirements.txt .

# Instalar dependencias en un prefix separado para luego copiarlo
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt

# Copiar el código de la app (por si quieres hacer tests en esta etapa)
COPY . .

# Etapa 2: imagen final de producción
FROM python:3.11-slim

WORKDIR /app

# Dependencias de runtime para matplotlib (sin toolchain de compilación)
RUN apt-get update && apt-get install -y \
    libfreetype6 \
    libpng16-16 \
    && rm -rf /var/lib/apt/lists/*

# Copiar las dependencias Python instaladas en /install desde el builder
COPY --from=builder /install /usr/local

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto que usará Uvicorn dentro del contenedor
EXPOSE 8004

# Opcional: evitar buffering de logs
ENV PYTHONUNBUFFERED=1

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8004"]

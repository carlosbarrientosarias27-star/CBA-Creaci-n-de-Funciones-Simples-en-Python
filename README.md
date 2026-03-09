# 🚀 Full-Stack Python: De Fundamentos a Sistemas Avanzados

Este repositorio contiene un ecosistema completo de aprendizaje y desarrollo en Python. El proyecto está diseñado de forma incremental, cubriendo desde la creación de funciones básicas hasta la implementación de un sistema de gestión de tareas con persistencia y seguridad.

# 📁 Estructura del Proyecto

El repositorio se divide en cuatro grandes módulos principales:

## 1. 📂 Creación de Funciones (CBA-CREACI-N-DE-FUNCIONES)

Fundamentos de lógica y validación.

Parte 1 & 2: Validaciones numéricas (es_positivo.py) y manipulación de strings (capitalizar(texto).py).

Parte 3 & 4: Lógica de usuario, incluyendo validación de emails y generación de resúmenes de perfil.

## 2. 📂 Refactorización y Patrones (ACTIVIDAD_INTERMEDIO_REFACTORIZACION)

Mejora de la calidad de código y diseño de software.

Bloque 1 & 2: Técnicas de simplificación de código, corrección de nomenclatura y aplicación del patrón Strategy.

Bloque 3 & 5: Evolución de sistemas de gestión de usuarios e inventarios desde código legacy a versiones refactorizadas.

## 3. 📂 Algoritmos de Generación Avanzada (ACTIVIDAD_AVANZADA_GENERACION)

Implementación de estructuras de datos y lógica compleja.

Bloque 1: Sistema de caché LRU (Least Recently Used) para gestión de memoria.

Bloque 2: Teoría de grafos dirigida (manual e implementada mediante IA).

Bloque 3 & 4: Algoritmos de Rate Limiting y ejercicios de Ingeniería Inversa.

## 4. 📂 Sistema de Gestión de Tareas (Bloque 5)

Una aplicación completa con arquitectura modular y persistencia.

auth/ & handlers/: Gestión de autenticación (JWT) y lógica de negocio para tareas.

middleware/: Capas de auditoría (audit_logger.py) y control de tráfico.

Persistencia: Base de datos relacional integrada en task_manager.db.

# 🛠️ Cómo Ejecutar cada Bloque

Para evitar errores de importación en los módulos internos, se recomienda ejecutar los scripts desde la raíz de cada carpeta principal utilizando el flag -m de Python.

## Ejecución de Lógica Básica

Bash
python -m "Parte 3.Validar_email"

## Ejecución de Refactorización

Bash
python -m "Bloque 2.2.2. patrón Strategy.Strategy_código"

## Ejecución de Sistemas Avanzados

Bash

## Para el sistema de tareas

python -m "Bloque 5 - Sistema de gestión de tareas.main"

## Para el sistema de caché

python -m "Bloque 1.1.2. Implantación Correcto.Sistema caché LRU(2)"

# ⚙️ Requisitos Técnicos

Python 3.12+: Requerido por la estructura de los archivos compilados .pyc.

SQLite: Utilizado para la persistencia del sistema de gestión de tareas.
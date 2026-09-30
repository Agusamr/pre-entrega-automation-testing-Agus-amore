# Propósito del proyecto

El objetivo de este proyecto es aplicar los conocimientos adquiridos hasta la Clase 8 del curso de Automatización de Testing, desarrollando pruebas automatizadas sobre una aplicación web utilizando Selenium WebDriver y Python.

El sitio utilizado para las pruebas es SauceDemo, una aplicación web demo diseñada para prácticas de testing.

El proyecto permite poner en práctica:

Automatización de flujos básicos de navegación web.
Interacción con elementos de una página web.
Localización de elementos mediante diferentes estrategias.
Validación de estados y resultados esperados.
Organización de pruebas utilizando Pytest.

## Tecnologías utilizadas
Python — Lenguaje de programación utilizado para desarrollar las pruebas.
Selenium WebDriver — Herramienta utilizada para automatizar la interacción con el navegador.
Pytest — Framework utilizado para estructurar y ejecutar las pruebas automatizadas.
Git — Sistema de control de versiones.
GitHub — Plataforma utilizada para almacenar y compartir el proyecto.


## Instalar las dependencias:

pip install selenium pytest

## Ejecutar las pruebas:

Para ejecutar un archivo de prueba específico:

pytest "ruta\al\archivo.py"

python -m pytest test_login.py
python -m pytest tests\test_presencia_productos.py -v -s para que muestre los print() en la terminal.

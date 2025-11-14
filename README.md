Proyecto de Automatización con Selenium
# Proyecto de Automatización con Selenium WebDriver  
**Autor:** Liam Antillón  
**Curso:** Calidad del de Software  
**Profesor:** Lorena Ramírez Corredor 
**Año:** 2025  

##  Descripción General  
Este proyecto implementa un conjunto de **seis automatizaciones web** utilizando **Selenium WebDriver en Python**, siguiendo el patrón **Page Object Model (POM)** para garantizar un código modular, escalable y mantenible.

Cada caso de prueba automatiza una interacción diferente en la plataforma  
 https://the-internet.herokuapp.com  
la cual se utiliza comúnmente para prácticas y pruebas de automatización.

---

#  **Tecnologías Utilizadas**
- **Python 3.14**
- **Selenium WebDriver 4**
- **Microsoft Edge WebDriver**
- **Page Object Model (POM)**
- **Git / GitHub para control de versiones**

---

#  **Estructura del Proyecto**

```bash
SeleniumProject/
│── drivers/               # WebDriver (msedgedriver.exe)
│── pages/                 # Clases POM
│   ├── base_page.py
│   ├── login_page.py
│   ├── download_page.py
│   ├── upload_page.py
│   ├── search_page.py
│   ├── dynamic_page.py
│   ├── table_page.py
│
│── tests/                 # Casos de prueba
│   ├── test_login.py
│   ├── test_download.py
│   ├── test_upload.py
│   ├── test_search.py
│   ├── test_dynamic.py
│   ├── test_table.py
│
│── config.py              # Configuración general del WebDriver
│── prueba.txt             # Archivo para pruebas de carga
│── table_data.csv         # Resultado exportado de tabla

 Automatizaciones Incluidas (6 Casos de Prueba)
1️⃣ Login Automático

Ingresa a la sección "Form Authentication"

Completa usuario y contraseña válidos

Verifica inicio de sesión correcto

Ejecutar:

py -m tests.test_login

2️⃣ Descarga de Archivo

Accede a "File Download"

Descarga un archivo disponible

Verifica que el archivo se haya guardado

Ejecutar:

py -m tests.test_download

3️⃣ Subida de Archivo

Ingresa a "File Upload"

Selecciona un archivo local

Envía el formulario y confirma el upload

Ejecutar:

py -m tests.test_upload

4️⃣ Búsqueda de Elementos

Entra a "Dynamic Controls"

Busca boton "Remove/Add"

Interactúa y valida cambios dinámicos

Ejecutar:

py -m tests.test_search

5️⃣ Contenido Dinámico

Navega a "Dynamic Content"

Refresca elementos dinámicos

Extrae y valida texto generado

Ejecutar:

py -m tests.test_dynamic

6️⃣ Lectura de Tabla y Exportación CSV

Accede a "Sortable Data Tables"

Lee datos de tabla HTML

Exporta datos a un archivo CSV

Ejecutar:

py -m tests.test_table

▶️ Cómo Ejecutar el Proyecto
1. Instalar dependencias
pip install selenium

2. Verificar WebDriver

Coloca el driver aquí:

C:\SeleniumDrivers\msedgedriver.exe

3. Ejecutar cualquier caso de prueba
py -m tests.nombre_del_test


Ejemplo:

py -m tests.test_login

 Metodología Aplicada

Automatizaciones basadas en el principio AAA (Arrange–Act–Assert)

Diseño estructurado usando POM (Page Object Model)

Separación entre:

lógica de negocio (pages/)

scripts de prueba (tests/)

configuración del navegador (config.py)

 Resultados

El sistema ejecuta correctamente las seis automatizaciones solicitadas.
Todos los casos fueron verificados y documentados en el informe entregado.

 Control de Versiones (Git)

Comandos utilizados:

git init
git add .
git commit -m "Primer commit - Proyecto Selenium automatizaciones"
git branch -M main
git remote add origin https://github.com/Wookix/SeleniumProject.git
git push -u origin main

📄 Licencia

Este proyecto es de uso académico y no está destinado para producción.

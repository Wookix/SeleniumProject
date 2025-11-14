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
-  **VS Code**

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

# 🧩 Casos de Prueba Automatizados (6)

A continuación, la lista oficial de pruebas automatizadas incluidas en este repositorio.

---

## ** Caso 1 — Login Automático**

✔ Ingresa a *Form Authentication*  
✔ Completa usuario y contraseña  
✔ Verifica el mensaje de inicio exitoso  

**Ejecutar:**

py -m tests.test_login

---

## ** Caso 2 — Navegación entre Módulos**

✔ Accede a distintos módulos del sitio  
✔ Cambia entre páginas  
✔ Valida que los títulos coincidan  

**Ejecutar:**

py -m tests.test_navigation

---

## ** Caso 3 — Inputs y Dropdown**

✔ Modifica valores de un campo  
✔ Selecciona opciones en un dropdown  
✔ Verifica los cambios  

**Ejecutar:**

py -m tests.test_form

---

## ** Caso 4 — Web Scraping de Tablas**

✔ Accede a *Sortable Data Tables*  
✔ Extrae datos de la tabla HTML  
✔ Exporta contenido a CSV  

**Ejecutar:**

py -m tests.test_table

---

## ** Caso 5 — Descarga de Archivos**

✔ Ingresa a *File Download*  
✔ Descarga un archivo disponible  
✔ Valida su existencia en el equipo  

**Ejecutar:**

py -m tests.test_download

---

## ** Caso 6 — Carga de Archivos**

✔ Usa el módulo *File Upload*  
✔ Selecciona archivo local  
✔ Confirma el upload exitoso  

**Ejecutar:**

py -m tests.test_upload

---

## 🚀 ¿Cómo Ejecutar Todo el Proyecto?

1. Instalar dependencias:

pip install selenium

2. Crear la carpeta SeleniumDrivers en C: y Verificar que `msedgedriver.exe` esté instalado en la carpeta

C:\SeleniumDrivers/msedgedriver.exe

3. Ejecutar cualquier caso de prueba:

py -m tests.nombre_del_test

Ejemplo:

py -m tests.test_login

---

## 📌 Versionamiento

El proyecto utiliza **Git** y está versionado públicamente en GitHub.

https://github.com/Wookix/SeleniumProject.git

---

## 📄 Licencia

Proyecto académico sin fines comerciales.  
Uso libre para aprendizaje y práctica.

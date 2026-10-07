# Pruebas automatizadas de SauceDemo

## Requisitos

- Python 3.10 o posterior
- Google Chrome instalado

## Instalación y ejecución

Desde la carpeta del proyecto, crea y activa un entorno virtual:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
```

En Windows, activa el entorno con `.venv\Scripts\activate` en lugar de `source .venv/bin/activate`.

Las pruebas usan Selenium para abrir SauceDemo en Chrome. `webdriver-manager` descarga el controlador de Chrome cuando hace falta. El reporte HTML se genera en `reports/reporte.html`.

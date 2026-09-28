# Virtual envirnment

### GENERAR Virtual ENVironment
```
python3 -m venv .venv
```

### activar venv
```
source .venv/bin/activate
```

### desactivar venv
```
deactivate
```

---



# TEST
```
pytest
```

### con mas detalles
```
pytest -v
```

```
python -m pytest
```

## Ejecutar solo tests con mark
* Solo ejecuta los test que tengan la marca "agregarProducto" en el archivo pytest.ini
```
pytest -m agregarProducto
```




# Hacer reportes HTML
* Instalar la librería
```
pip install pytest-html
```

 * generar el reporte 

```
pytest --html=reports/reporte01.html --self-contained-html
```

pytest --html=reports/reporte01.html **(genera el reporte en carpeta /reports)** --self-contained-html **(el ccs lo mete dentro del html, x defecto lo deja aparte)**


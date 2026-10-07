# Pre-entrega de proyecto: Automatización QA

## Objetivo

Aplicar los conocimientos adquiridos hasta la Clase 8 para automatizar flujos básicos de navegación web con Selenium WebDriver y Python. El proyecto debe practicar la interacción con elementos web, las estrategias de localización y la validación de estados.

**Sitio objetivo:** [saucedemo.com](https://www.saucedemo.com/)

## Fecha y formato de entrega

- **Fecha límite:** 7 días a partir de la Clase 8.
- **Formato:** código subido a GitHub.
- **Nombre del repositorio:** `pre-entrega-automation-testing-[nombre-apellido]`.
- **Visibilidad:** repositorio público.

## Tecnologías requeridas

- Python como lenguaje principal.
- Pytest para estructurar las pruebas.
- Selenium WebDriver para automatizar el navegador.
- Git y GitHub para el control de versiones.

## Organización del proyecto

- Separar el código en al menos dos archivos: pruebas y funciones auxiliares.
- Usar nombres significativos y comentarios descriptivos.
- Mantener el código legible, bien organizado y presentado de forma clara y profesional.
- Usar `README.md` para explicar el proyecto y facilitar su ejecución.

Estructura mínima sugerida:

```text
proyecto/
├── tests/
├── utils/       # Funciones auxiliares
├── datos/       # Opcional: CSV, JSON u otros datos externos
└── reports/     # Reportes y capturas
```

## Consignas obligatorias

### 1. Automatización del login

1. Navegar a la página de login de SauceDemo.
2. Ingresar credenciales válidas:
   - Usuario: `standard_user`
   - Contraseña: `secret_sauce`
3. Validar el login exitoso comprobando la redirección a la página de inventario.

**Criterios mínimos:** usar una espera explícita y validar `/inventory.html` y los textos `Products` y `Swag Labs`.

### 2. Navegación y verificación del catálogo

Crear un caso de prueba que:

- Verifique el título de la página de inventario.
- Compruebe que haya productos visibles, al menos uno.
- Valide que estén presentes elementos importantes de la interfaz, como el menú y los filtros.
- Liste o valide el nombre y el precio del primer producto.

**Criterios mínimos:** validar el título y la presencia de productos; obtener el nombre y el precio del primero.

### 3. Interacción con productos y carrito

Crear un caso de prueba que:

1. Añada el primer producto al carrito.
2. Verifique que el contador del carrito se incremente correctamente.
3. Navegue al carrito.
4. Compruebe que el producto añadido aparezca allí.

**Criterios mínimos:** agregar el primer producto y verificar que figure en el carrito.

## Funcionalidad esperada

- Los casos deben ejecutarse correctamente en SauceDemo.
- Las validaciones deben ser claras y específicas para cada paso.
- Los tests deben ser independientes: el fallo de uno no debe afectar a los demás.
- El código debe ser legible y estar organizado.

## README requerido

El `README.md` del proyecto debe explicar:

- El propósito del proyecto.
- Las tecnologías utilizadas.
- Cómo instalar las dependencias.
- Cómo ejecutar las pruebas.
- Cómo generar el reporte HTML.

Comando de reporte indicado en la consigna:

```sh
pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html
```

También se da como ejemplo:

```sh
pytest -v --html=reporte.html
```

## Repositorio y entregables

- Repositorio público en GitHub con todo el código.
- Commits frecuentes, con mensajes descriptivos que reflejen el progreso.
- `README.md` completo y claro.
- Reporte HTML generado por Pytest con los resultados de la ejecución.
- Evidencias adicionales: capturas automáticas en caso de fallos y logs de ejecución.
- Compartir el enlace al repositorio antes de la fecha límite.

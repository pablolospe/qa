import pytest # Importa la biblioteca pytest para la creación de pruebas unitarias y fixtures
from selenium import webdriver # Importa la biblioteca selenium para la automatización de navegadores
from selenium.webdriver.chrome.service import Service # Importa la clase Service para configurar el servicio del driver de Chrome
from webdriver_manager.chrome import ChromeDriverManager # Importa la clase ChromeDriverManager para gestionar automáticamente la instalación del driver de Chrome


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install()) # Configura el servicio del driver de Chrome
    options = webdriver.ChromeOptions()
    # options.add_argument("--start--maximized")  # Start Chrome maximized
    driver = webdriver.Chrome(service=service, options=options) # Crea una instancia del driver de Chrome con las opciones configuradas

    yield driver # Entrega la instancia del driver al test
    driver.quit() # Cierra el navegador después de que el test haya terminado



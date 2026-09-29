# import pytest # Importa la biblioteca pytest para la creación de pruebas unitarias y fixtures

from selenium import webdriver # Importa la biblioteca selenium para la automatización de navegadores
from selenium.webdriver.chrome.service import Service # Importa la clase Service para configurar el servicio del driver de Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # Importa la clase By para localizar elementos en la página web

import time

service = Service(ChromeDriverManager().install()) # Configura el servicio del driver de Chrome
driver = webdriver.Chrome(service=service) # Crea una instancia del driver de Chrome con las opciones configuradas

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Navega a la URL de inicio de sesión


time.sleep(4)

driver.find_element(By.NAME, "username").send_keys("Admin")  # Ingresa el nombre de usuario
driver.find_element(By.NAME, "password").send_keys("admin123")  # Ingresa la contraseña
driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Hace clic en el botón de inicio de sesión
# driver.find_element(By.XPATH, "//a[@href='https://www.youtube.com/c/OrangeHRMInc']").click()  # Hace clic en el botón de YouTube

time.sleep(8)

driver.quit()  # Cierra el navegador después de que la prueba haya terminado
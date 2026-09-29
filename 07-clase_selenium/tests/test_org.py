from utils.helpers import login_helper
from selenium.webdriver.common.by import By # Importa la clase By para localizar elementos en la página web

# import pytest # Importa la biblioteca pytest para la creación de pruebas unitarias y fixtures

def test_login( driver ):
    login_helper(driver)  # Llama a la función de inicio de sesión definida en helpers.py

    # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Navega a la URL de inicio de sesión
    
    # driver.find_element(By.NAME, "username").send_keys("Admin")  # Ingresa el nombre de usuario
    # driver.find_element(By.NAME, "password").send_keys("admin123")  # Ingresa la contraseña
    # driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Hace clic en el botón de inicio de sesión

    assert 'dashboard' in driver.current_url  # Verifica que la URL de la página contenga "dashboard" después del inicio de sesión   



def test_title_verification( driver ):
    login_helper(driver)  # Llama a la función de inicio de sesión definida en helpers.py

    assert "Dashboard" in driver.find_element(By.TAG_NAME, "h6").text  # Verifica que el título de la página contenga "Dashboard" después del inicio de sesión
    # assert 'Dashboard' in driver.  # Verifica que el título de la página contenga "Dashboard" después del inicio de sesión
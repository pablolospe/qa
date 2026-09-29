
import time

from conftest import driver


URL_LOGIN = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
URL_2 = "https://duckduckgo.com/"

def login_helper( driver ):

    driver.get(URL_LOGIN)  # Navega a la URL de inicio de sesión

    time.sleep(4)
    
    driver.find_element("name", "username").send_keys("Admin")  # Ingresa el nombre de usuario
    driver.find_element("name", "password").send_keys("admin123")  # Ingresa la contraseña
    driver.find_element("xpath", "//button[@type='submit']").click()  # Hace clic en el botón de inicio de sesión
    
    time.sleep(4)

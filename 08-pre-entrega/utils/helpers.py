
import time
from selenium.webdriver.common.by import By
from conftest import driver


URL_LOGIN = "https://www.saucedemo.com/"

def login_helper( driver ):

    driver.get(URL_LOGIN)  # Navega a la URL de inicio de sesión

    time.sleep(4)
    
    driver.find_element("name", "user-name").send_keys("standard_user")  # Ingresa el nombre de usuario
    driver.find_element("name", "password").send_keys("secret_sauce")  # Ingresa la contraseña
    driver.find_element(By.ID, "login-button").click()
    
    time.sleep(4)

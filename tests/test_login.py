from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

def test_login_exitoso():

    driver = webdriver.Chrome()


# Navegar a la página de login
    driver.get("https://www.saucedemo.com/")

    time.sleep(2) #pausa para que espere un ratito y no haga tan rápido

#primero localizo los elementos de la web para interactuar con ellos...
    usuario = driver.find_element(By.ID,"user-name")
    contrasena = driver.find_element(By.ID,"password")
    boton_login = driver.find_element(By.ID,"login-button")
    
#completar el form
    usuario.send_keys("standard_user")
    contrasena.send_keys("secret_sauce")
#hacer login
    boton_login .click()

    titulo = driver.find_element(By.CLASS_NAME,"app_logo")
    time.sleep(2)
    #validar la URL despues del login
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    assert titulo.text == "Swag Labs"
    driver.quit()

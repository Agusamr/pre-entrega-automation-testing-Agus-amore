from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

def test_presencia_productos():

    driver = webdriver.Chrome()  
    driver.get("https://www.saucedemo.com/")
        
    usuario = driver.find_element(By.ID,"user-name")
    password = driver.find_element(By.ID,"password")
    boton_login = driver.find_element(By.ID,"login-button")
    time.sleep(2)

    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")

    boton_login.click()

    productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
      
    #validar existencia de algun producto
    assert len(productos)>0

#validar existencia del primer producto
    primer_producto = productos[0]
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

#listar producto
    print(f"Primer producto: {nombre_producto}")
    print(f"Precio: {precio}")

#validar menu y filtro
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed()
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed()

    driver.quit()



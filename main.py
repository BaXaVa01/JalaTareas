from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tabulate
from creatingObsidian import createMd

# Crear un navegador Edge controlado por la libreria Selenium
driver = webdriver.Edge()

# Ir a la página de inicio de sesión
driver.get("https://uamvirtual.uam.edu.ni/grado/")

# Encontrar los campos de usuario y contraseña, y el submit

usuario = driver.find_element(By.NAME, "username")
contrasenia = driver.find_element(By.NAME, "password")
submit = driver.find_element(By.NAME, "logintoken")

# Ingresar credenciales
usuario.parent.execute_script("arguments[0].setAttribute('value', '########')", usuario)
contrasenia.parent.execute_script("arguments[0].setAttribute('value', '#######')", contrasenia)
submit.submit()


# Enviar el formulario

  # Esperar a que cargue la siguiente página
#En esta lista tenes que poner los links de las clases que queres que se revisen, y el nombre de la clase
clases = [["#####################################################", "finanzas"],
           ["#####################################################", "Base de datos"],
           ["#####################################################", "Investigacion de operaciones"],
           ["#####################################################", "Estadistica"],
           ["#####################################################", "Pob"],
           ["#####################################################]", "Algebra lineal"]]

asignaciones = []

for clase_url in clases:
    counterClases = 0
    driver.get(clase_url[0])
      # Espera a que cargue la página de la clase

    for section in range(1, 9):
        semana = clase_url[0] + "&section=" + str(section) + "#tabs-tree-start"
        driver.get(semana)
        # time.sleep(3)
        # Buscar todos los elementos con la clase 'accesshide'

        elementos = driver.find_elements(By.CLASS_NAME, "accesshide")

        # Recorrer los elementos encontrados
        for elemento in elementos:
            # Comprobar si el texto del elemento es "Tarea"
            if "Tarea" in elemento.text:
                
                print(f"Actividad encontrada en {clase_url[1]}: semana {section}")
                
                texto = elemento.find_element(By.XPATH, "..").text

                contenedor_principal = elemento.find_element(By.XPATH, "../..").get_attribute("href") 
                texto = texto.replace("Tarea", "",)
                print(texto)
                print(contenedor_principal, "\n")
                asignaciones.append([texto, contenedor_principal, section, clase_url[1]])

        counterClases += 1


createMd(asignaciones)
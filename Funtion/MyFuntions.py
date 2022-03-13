from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import io
import json


#Acciones
def Login(driver,User,Pass):
    # login
    driver.find_element(By.ID, "ar.com.unisolutions.unigis_deliveries_x:id/email").send_keys(User)
    # clave
    driver.find_element(By.ID, "ar.com.unisolutions.unigis_deliveries_x:id/password").send_keys(Pass)
    # seleccionar perfil
    driver.find_element(By.ID, "ar.com.unisolutions.unigis_deliveries_x:id/sp_endpoint").click()
    driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
    # conectar
    driver.find_element(By.ID, "ar.com.unisolutions.unigis_deliveries_x:id/sign_in_button").click()

def DocVencida(driver,wait):
    # notificacion de Documentacion vencida
    try:
        wait.until(EC.visibility_of_element_located((By.ID, "ar.com.unisolutions.unigis_deliveries_x:id/a_notificacion_documentos_button")))
        driver.find_element(By.ID,"ar.com.unisolutions.unigis_deliveries_x:id/a_notificacion_documentos_button").click()
    except TimeoutException:
        print('no se encontraron documentos vencidos')

def deslizar(driver,direccion):
    pantalla = driver.find_element(By.ID, 'android:id/content')
    if direccion == 'izquierda':
        TouchAction(driver).press(pantalla, 540, 1150).move_to(pantalla, 0, 1150).release().perform()
    elif direccion=='derecha':
        TouchAction(driver).press(pantalla, 0, 1150).move_to(pantalla, 5400, 1150).release().perform()
    elif direccion=='arriba':
        TouchAction(driver).press(pantalla, 540, 1700).move_to(pantalla, 540, 700).release().perform()
    elif direccion=='abajo':
        TouchAction(driver).press(pantalla, 540, 700).move_to(pantalla, 540, 1700).release().perform()

#Elementos
class Elemento():
    def __init__(self,driver,nombre,Estrategia,Localizador):
        self.driver=driver
        self.estrategia=Estrategia
        self.localizador=Localizador
        #almacenar el objeto en un json para su uso futuro
        with open('Elementos.JSON') as file:
            Elementos = json.load(file)
        Elementos[nombre] = [{'estrategia':self.estrategia,'localizador':self.localizador}]
        with open('Elementos.json', 'w') as file:
            json.dump(Elementos, file, indent=4)
        file.close()


    def click(self):
        driver = self.driver
        est = self.estrategia
        loc = self.localizador

        if est == 'id':
             driver.find_element(By.ID, loc).click()
        elif est == 'xpath':
             driver.find_element(By.XPATH, loc).click()
        elif est == 'name':
             driver.find_element(By.NAME, loc).click()
        elif est == 'css_selector':
             driver.find_element(By.CSS_SELECTOR, loc).click()
        elif est == 'tag_name':
             driver.find_element(By.TAG_NAME, loc).click()
        elif est == 'class_name':
             driver.find_element(By.CLASS_NAME, loc).click()
        elif est == 'link_text':
            driver.find_element(By.LINK_TEXT, loc).click()
        else:
            print('El Elemento no se logro encontrar')


def logout(driver,wait):
    i = 0
    while i == 0:
        try:
            driver.find_element(By.ID, "ar.com.unisolutions.unigis_deliveries_x:id/action_ver_qr_conductor")
        except:
            driver.press_keycode(4)  # Back
        else:
            driver.find_element(By.XPATH, "//android.widget.ImageView[@content-desc='Más opciones']").click()
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]")))
            salir = driver.find_element(By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]")
            salir.click()
            driver.quit()
            i = 1


Prueba='hola'










import HtmlTestRunner
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction


class Smoke_Mobile(unittest.TestCase):

    def setUp(self):
        self.mobil = {
            "appium:platformVersion": "11",
            "appium:automationName": "UiAutomator2",
            "appium:appPackage": "ar.com.unisolutions.unigis_deliveries_x",
            "appium:appActivity": ".views.user.activities.LoginActivity",
            "appium:platformName": "Android",
            "appium:noReset": 'true',
            "appium:UDID": "ZY22D2GP9X"
        }
        self.driver= webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.mobil)
        self.user="carlos"
        self.pas="1234"
        self.wait = WDW(self.driver, 100)
    #esto es una prueba
        #showLibraryContents

        #login
        self.driver.find_element(By.ID, "ar.com.unisolutions.unigis_deliveries_x:id/email").send_keys(self.user)
        #clave
        self.driver.find_element(By.ID, "ar.com.unisolutions.unigis_deliveries_x:id/password").send_keys(self.pas)
        #seleccionar perfil
        self.driver.find_element(By.ID, "ar.com.unisolutions.unigis_deliveries_x:id/sp_endpoint").click()
        self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]").click()
        #conectar
        self.driver.find_element(By.ID, "ar.com.unisolutions.unigis_deliveries_x:id/sign_in_button").click()
        #notificacion de Documentacion vencida
        self.wait.until(EC.visibility_of_element_located((By.ID, "ar.com.unisolutions.unigis_deliveries_x:id/a_notificacion_documentos_button")))
        self.driver.find_element(By.ID, "ar.com.unisolutions.unigis_deliveries_x:id/a_notificacion_documentos_button").click()

        #variables
        self.pod = self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout")
        self.touch=TouchAction(self.driver)

    def test_SK_106(self):
        driver=self.driver
        wdw=self.wait
        self.pod.click()
        wdw.until(EC.visibility_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout")))
        titulo=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView").text
        TEsperado = "Viajes Disponibles"
        self.assertTrue(titulo == TEsperado,"titulo diferente al esperado")
        try:
            driver.find_element(By.ID,"ar.com.unisolutions.unigis_deliveries_x:id/action_bar_refresh")
            driver.find_element(By.ID,"ar.com.unisolutions.unigis_deliveries_x:id/action_search_CB")
            driver.find_element(By.XPATH,"//android.widget.ImageView[@content-desc='Más opciones']")
            driver.find_element(By.ID,"ar.com.unisolutions.unigis_deliveries_x:id/viajes_grid_content_form")
            driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]")
            driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]")
            driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
            driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]")
            driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[2]")
            driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]")
            driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[4]")
            driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[5]")
            driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.ImageButton")
        except :
            valor = False
        else:
            valor = True
        finally:
            self.assertTrue(valor,"uno o mas elemento no fueron encontrados")

    def test_SK_107(self):
        wdw=self.wait
        driver = self.driver
        #entrar a POD
        self.pod.click()
        wdw.until(EC.visibility_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout")))
        #Seleccionar el detalle del primer viaje disponible
        driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]").click()
        wdw.until(EC.visibility_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup")))
        cond=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[7]").text
        #deslizar la pantalla hacia Recursos del viaje
        pantalla = driver.find_element(By.ID,'android:id/content')
        self.touch.press(pantalla,1030,1150).move_to(pantalla,0,1150).release().perform()
        #wdw.until((EC.visibility_of_element_located((By.ID,"ar.com.unisolutions.unigis_deliveries_x:id/content_detalle_page_info_titl"))))
        #clic en menu + menu expandible
        plus=driver.find_element(By.ID,"ar.com.unisolutions.unigis_deliveries_x:id/fab_expand_menu_button")
        plus.click()
        #wdw.until(EC.visibility_of_element_located((By.ID,"ar.com.unisolutions.unigis_deliveries_x:id/activity_detalle_viaje_bt_rendir_recurso")))
        ScanQR=driver.find_element(By.ID,"ar.com.unisolutions.unigis_deliveries_x:id/activity_detalle_viaje_bt_busqueda_escaner")
        ScanQR.click()
        wdw.until(EC.visibility_of_element_located((By.ID,"ar.com.unisolutions.unigis_deliveries_x:id/busquedayqr_bt_asignar_recurso")))
        driver.find_element(By.ID,"ar.com.unisolutions.unigis_deliveries_x:id/busquedayqr_bt_asignar_recurso").click()
        driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[1]").click()
        wdw.until(EC.visibility_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[7]")))
        condasig=driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView[7]").text
        valor = True
        if cond != condasig:
            valor = True
        else:
            valor = False
        self.assertTrue(valor, "no se ha asignado el conductor correctamente")




    def tearDown(self):
        i = 0
        while i == 0:
            try:
                self.qrconductor=self.driver.find_element(By.ID,"ar.com.unisolutions.unigis_deliveries_x:id/action_ver_qr_conductor")
            except:
                self.driver.press_keycode(4)
            else:
                self.driver.find_element(By.XPATH,"//android.widget.ImageView[@content-desc='Más opciones']").click()
                self.wait.until(EC.visibility_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]")))
                salir = self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]")
                salir.click()
                self.driver.quit()
                i = 1

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='resultado'))










from selenium import webdriver
from time import sleep
from secreto import entrar

nombre = "danielajg"
password = entrar


class InstaBot:
    def __init__(self, nombre, password):
        self.driver = webdriver.Chrome()
        self.driver.get("http://instagram.com")
        sleep(4)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/"
            "div[2]/div[1]/div/form/div[2]/div/label/input"
            ).send_keys(nombre)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/"
            "div[2]/div[1]/div/form/div[3]/div/label/input"
            ).send_keys(password)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/"
            "div[2]/div[1]/div/form/div[4]"
            ).click()
        sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/"
            "div/div/div/button"
            ).click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/"
            "div/div/div[3]/button[2]"
            ).click()
        sleep(30)


InstaBot('danieljag', entrar)

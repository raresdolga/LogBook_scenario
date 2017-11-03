from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time
import re
import xml.etree.ElementTree as ET



def pause():
        time.sleep(2)
  
#from pyvirtualdisplay import Display
def inputSignup(username, password): # searches for sign up input elements and inserts values
        inputUsername = driver.find_element_by_id("username")
        inputUsername.send_keys(username)
        pause()
        inputPassword = driver.find_element_by_id("password")
        inputPassword.send_keys(password)
        pause()
        signupButton = driver.find_element_by_id("signupBut")
        signupButton.click()
        pause()

def inputLogin(username, password):
    logInTabButton = driver.find_element_by_link_text("Log In")
    pause
    logInTabButton.click()
    pause()
    # inputUsername  = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, xpaths["//*[@id='username']"])))
    inputUsername = driver.find_element_by_id("username1")
    inputUsername.send_keys(username)
    pause()
    inputPassword = driver.find_element_by_id("password1")
    inputPassword.send_keys(password)
    pause()
    logInButton = driver.find_element_by_id("loginBut")
    logInButton.click()

def logOut():
    logOutButton = driver.find_element_by_id("logoutBut")
    pause()
    logOutButton.click()

def clearSignup(): # searches for sign up input elements and inserts values
        inputUsername = driver.find_element_by_id("username")
        inputUsername.clear()
        pause()
        inputPassword = driver.find_element_by_id("password")
        inputPassword.clear()
        pause()

def clearLogin():
    pause()
    # inputUsername  = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, xpaths["//*[@id='username']"])))
    inputUsername = driver.find_element_by_id("username1")
    inputUsername.clear()
    pause()
    inputPassword = driver.find_element_by_id("password1")
    inputPassword.clear()
    pause()

def changeViewToSignup():
    signUpTabButton = driver.find_element_by_link_text("Sign Up")
    pause
    signUpTabButton.click()
    pause()


driver = webdriver.Chrome("/usr/local/bin/chromedriver")
# driver.get("http://snifflog.uksouth.cloudapp.azure.com")
driver.get("http://127.0.0.1:8000")
# currentstate = "login"
# OriginalTitle = driver.title

inputLogin("bobby500", "")
clearLogin()
inputLogin("","asdasda")
clearLogin()
inputLogin("","")
clearLogin()

changeViewToSignup()

pause()
inputSignup("", "lamb500")
clearSignup()
inputSignup("bobbymate",""
clearSignup)
inputSignup("","")
clearSignup()


pause()
inputSignup("bobby128", "lamb128")
logOut()
inputLogin("bobby128", "lamb128")
logOut()


# inputSignup("bobby124","lamb124")
pause()
driver.quit()




import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from send_email import send_email
import pickle

def new_vaccin():
    #Path of the Driver which have been downloaded.
    driverPath = "/Users/henriterrasse/Documents/Code/ChromeDriver/chromedriver"

    #The headless argument permits to start ChromeDriver without opening the window.
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")

    #Initialisation of the selenium webdriver
    driver = webdriver.Chrome(driverPath)
    #driver = webdriver.Chrome(driverPath, options = chrome_options)
    
    #Go to the webpage we want to scrape
    driver.get("https://www.doctolib.fr/")

    #Collect the element with the following class.
    rdv_prochainement = driver.find_elements_by_xpath("//*[contains(text(), 'des RDV prochainement')]")
    rdv_prochainement_text = [rdv.text for rdv in rdv_prochainement]
    
    driver.close()
    
    #If there is no new RDV, return false.
    return 'Vaccination : des RDV prochainement' not in rdv_prochainement_text
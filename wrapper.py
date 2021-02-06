import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from send_email import send_email
from check_vaccin import new_vaccin
import pickle

if __name__ == "__main__":
        vaccin = new_vaccin()
        if vaccin:
                send_email()
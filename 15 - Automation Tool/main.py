from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Define driver options and service  
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
service = Service("chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options,service=service) 

#Load the webpage   
driver.get('https://demoqa.com/login')

#Locate username, password and login button
username_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,'userName')))
password_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,'password')))
login_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,'login')))

#Fill in username, password and click the button
username_field.send_keys('test001')
password_field.send_keys('Test1234!')
login_button.click()

#Locate the element dropdown
elements = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                            '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
elements.click()

text_box = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,'item-0')))
text_box.click()

#Locate the form fields and submit button
fullname_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,'userName')))
email_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,'userEmail')))
current_address_field =WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,'currentAddress')))
permanent_address_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,'permanentAddress')))
submit_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,'submit')))

#Fill in the for fields
fullname_field.send_keys('John Smith')
email_field.send_keys('john@gmail.com')
current_address_field.send_keys('calle inventada 123')
permanent_address_field.send_keys('calle inventada 123')
submit_button.click()

#Locate the download section and button
upload_download = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,'item-7')))
upload_download.click()
download_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID,'downloadButton')))
download_button.click()


input("press enter to close the browser")
driver.quit()


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By



firefox_path = "C://Users//srich//Downloads//geckodriver-v0.32.0-win32//geckodriver.exe"


option= webdriver.FirefoxOptions()
option.binary_location="C:\Program Files\Mozilla Firefox\\firefox.exe"


serv = Service(firefox_path)
driver= webdriver.Firefox(service=serv,options=option)


driver.get("https://www.python.org/")
search=driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[3]/p[2]/a')
print(search.text)
#


# driver.get("https://www.amazon.in/Earthy-Sapo-Reetha-Shampoo-Bar/dp/B06XHVZYLN/ref=pd_rhf_d_gw_s_pd_crcd_sccl_1_3/259-2975470-2874927?pd_rd_w=3bm92&content-id=amzn1.sym.dcf9b861-ea71-4cd9-870f-f1d20747f687&pf_rd_p=dcf9b861-ea71-4cd9-870f-f1d20747f687&pf_rd_r=ABPKF98PX4EK3JH3M5XR&pd_rd_wg=eggqZ&pd_rd_r=1a9927e5-4a18-46dc-b318-e1690a199ee8&pd_rd_i=B06XHVZYLN&th=1")
#
#
# price = driver.find_element(By.XPATH, "//*[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[1]/span[2]/span[2]")
# print(price.text)

driver.quit()
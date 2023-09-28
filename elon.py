import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()
a = ActionChains(driver)

driver.get('https://www.twitter.com')
time.sleep(9)
wait = WebDriverWait(driver, 10)
signin = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span")
signin.click()
email = wait.until(EC.presence_of_element_located((By.NAME, "text")))
email.send_keys("email or name")  
email.send_keys(Keys.ENTER)
password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys("password")
password.send_keys(Keys.ENTER)

driver.get('https://twitter.com/elonmusk')
time.sleep(5)  

page_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == page_height:
        break
    page_height = new_height


tweets = driver.find_elements(By.XPATH, '//div[@data-testid="tweet"]')


desktop_path = r'C:\Users\Hp Pavilion\Desktop\tweets1.txt'  
with open(desktop_path, 'w', encoding='utf-8') as file:
    for tweet in tweets:
        try:
            tweet_text = tweet.find_element(By.XPATH, './/div[@class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"]').text
            tweet_time = tweet.find_element(By.XPATH, './/time').get_attribute('datetime')
            file.write(f'{tweet_time} {tweet_text}\n')
        except:
            continue
driver.quit()
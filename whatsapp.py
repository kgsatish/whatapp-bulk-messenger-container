from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from flask import Flask
from flask import request
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import urllib.parse
import os

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def scrape():
    print("Execution Started")
    phone = request.args.get('phone')
    text = request.args.get('text')

    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--user-data-dir=/home/seluser/.config/google-chrome/whatsapp")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)

    #maximize the window size
    driver.maximize_window()
    print(vars(driver))
    driver.caps['networkConnectionEnabled'] = True
    time.sleep(5)
    qry = {'phone': phone, 'text': text}
    url = "https://web.whatsapp.com/send/?{}".format(urllib.parse.urlencode(qry))
    driver.get(url)
    driver_wait = WebDriverWait(driver, 120)
    driver_wait.until(lambda driver:  driver.find_element(By.XPATH,
        '//span[@class="selectable-text copyable-text" and @data-lexical-text="true"]'))
    time.sleep(30)
    print(driver.title)
    print(vars(driver))

    message_box = driver_wait.until(lambda driver: driver.find_element(
        By.XPATH, '//div[@title="Type a message" and @role="textbox"]'))
    action = ActionChains(driver)
    action.move_to_element(message_box).click()
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(10)
    driver.close()
    driver.quit()
    print("Execution Successfully Completed!")
    return '<html><head><link rel="icon" href="data:,"></head><body><p>Done sucessfully to phone ' + phone + '</p></body></html>'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

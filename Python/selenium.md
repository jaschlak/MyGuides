# Selenium

    Getting started with selenium
    
    Note: The example below uses the chrome driver you have installed.
          There are other examples that will be different if you explicitly point to your driver
    
    Here are more examples/reading:
    https://selenium-python.readthedocs.io/getting-started.html
    https://www.geeksforgeeks.org/find_elements_by_partial_link_text-driver-method-selenium-python/?ref=ml_lbp
    
## Code

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.get('https://www.google.com');
    
    # find element
    driver.find_element(By.ID, '<insert id value>')
    driver.find_element(By.CLASS_NAME, '<insert class name>')
    driver.find_element(By.CSS_SELECTOR, '<insert css selector>')
    driver.find_element(By.LINK_TEXT, '<insert text from element>')
    driver.find_element(By.PARTIAL_LINK_TEXT, '<insert some text from element>')
    driver.find_element(By.TAG_NAME, '<insert tag name>')
    driver.find_element(By.XPATH, '<insert custom xpath>')
    
    # assign an element to variable
    element = driver.find_element(By.ID, '<insert id value>')
    
## actions

    element.click()
    element.send_keys('text to input')
    driver.back()
    
## waits, after an action wait for something to happen before continuing (condition instead of time)

    #documentation at: https://selenium-python.readthedocs.io/waits.html#explicit-waits


    from selenium.webdriver.support import expected_conditions as EC
    
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
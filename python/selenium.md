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
    
    
    
## Here is some code that will use Firefox and use manual options allowing port specification (cycles every 5 minutes)

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.proxy import Proxy, ProxyType

    from datetime import datetime
    import time

    prox_ip = '<loopback_ip>'
    prox_port = '<port>'

    frequency_s = <run frequency seconds>

    site_username = '<username>'
    site_password = '<password>'

    url = '<site_url>'

    poll_timeout_s = <failure timeout seconds>
    poll_frequency_s = <check for faulure every, seconds>


    # Create a new Firefox options object
    options = webdriver.FirefoxOptions()

    # Set proxy settings in the options
    proxy_address = "{}:{}".format(prox_ip,prox_port)  # Change this to your proxy address
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = proxy_address
    proxy.ssl_proxy = proxy_address
    options.proxy = proxy

    # set to run immediately
    last_time = time.time() - frequency_s

    while True:

        if time.time() - last_time >= frequency_s:
            print(datetime.now())
        
            driver = webdriver.Firefox(options=options)
            wait = WebDriverWait(driver, timeout=poll_timeout_s, poll_frequency=poll_frequency_s, ignored_exceptions=[TimeoutException])
            driver.get(url)
            
            # %%
            
            find_username = driver.find_element(By.CSS_SELECTOR, 'input[class="<all classes>')
            find_username.send_keys(site_username)
            
            find_password = driver.find_element(By.CSS_SELECTOR, 'input[class="<all classes>')
            find_password.send_keys(site_password)

            driver.find_element(By.CSS_SELECTOR, 'div[class="<class>').click()
            
            element = wait.until(EC.visibility_of_element_located((By.ID, "<ID loockup>")))
            driver.close()
            
            last_time = time.time()
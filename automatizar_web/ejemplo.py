from selenium.webdriver.opera.options import Options 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException 
from selenium import webdriver 
from time import sleep 
  
  
if __name__ == '__main__': 
      
    
    
    edgeBrowser = webdriver.Edge(r"msedgedriver.exe") 
      
    
    edgeBrowser.maximize_window() 
      
    
    edgeBrowser.get('https://www.lambdatest.com') 
    try: 
      
        sampleElement = WebDriverWait(browser, 10).until( 
            EC.presence_of_element_located((By.ID, 'useremail'))) 
        
      
        sampleElement.send_keys("gfg@lambdatest.com") 
        
        sampleElement.click() 
        
      
        sampleElement2 = WebDriverWait(browser, 10).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR,  
                                        "#testing_form > div"))) 
        
        sampleElement2.click() 
        
      sleep(20)
    except TimeoutException: 
        print("Trying to find the given element but unfortunately no element is found") 
    sleep(20)
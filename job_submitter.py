import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def submit_application(portal, credentials, job_url, cv_path, job_title, company):
    """Submit job application to the specified portal."""
    
    # Set up Selenium WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Different submission logic based on portal
        if portal.lower() == 'linkedin':
            return submit_to_linkedin(driver, credentials, job_url, cv_path)
        elif portal.lower() == 'indeed':
            return submit_to_indeed(driver, credentials, job_url, cv_path)
        elif portal.lower() == 'glassdoor':
            return submit_to_glassdoor(driver, credentials, job_url, cv_path)
        else:
            return f"Submission to {portal} is not yet implemented"
            
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        driver.quit()

def submit_to_linkedin(driver, credentials, job_url, cv_path):
    """Submit application to LinkedIn."""
    try:
        # Login
        driver.get("https://www.linkedin.com/login")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        
        driver.find_element(By.ID, "username").send_keys(credentials['username'])
        driver.find_element(By.ID, "password").send_keys(credentials['password'])
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Wait for login to complete
        WebDriverWait(driver, 10).until(EC.url_contains("linkedin.com/feed"))
        
        # Navigate to job posting
        driver.get(job_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".jobs-apply-button")))
        
        # Click apply button
        driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button").click()
        
        # Wait for application form
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
        
        # Upload resume
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(cv_path)
        
        # This is a simplified example - actual LinkedIn application process might require more steps
        # Complete the rest of the form...
        
        # Submit application
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']")
        submit_button.click()
        
        # Wait for confirmation
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".artdeco-inline-feedback--success")))
        
        return "Successfully submitted to LinkedIn"
        
    except TimeoutException:
        return "Timeout on LinkedIn submission"
    except Exception as e:
        return f"LinkedIn submission error: {str(e)}"

def submit_to_indeed(driver, credentials, job_url, cv_path):
    """Submit application to Indeed."""
    try:
        # Login
        driver.get("https://www.indeed.com/account/login")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ifl-InputFormField-3")))
        
        driver.find_element(By.ID, "ifl-InputFormField-3").send_keys(credentials['username'])
        driver.find_element(By.ID, "ifl-InputFormField-7").send_keys(credentials['password'])
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Wait for login to complete
        WebDriverWait(driver, 10).until(EC.url_contains("indeed.com/"))
        
        # Navigate to job posting
        driver.get(job_url)
        
        # Click apply button
        apply_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobsearch-IndeedApplyButton-newDesign"))
        )
        apply_button.click()
        
        # Handle application process (simplified)
        # The exact steps will depend on the specific job posting
        
        # Upload resume if prompted
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
            file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
            file_input.send_keys(cv_path)
        except TimeoutException:
            # Resume upload might not be required if already on file
            pass
        
        return "Indeed submission process started (may require manual completion)"
        
    except TimeoutException:
        return "Timeout on Indeed submission"
    except Exception as e:
        return f"Indeed submission error: {str(e)}"

def submit_to_glassdoor(driver, credentials, job_url, cv_path):
    """Submit application to Glassdoor."""
    try:
        # Login
        driver.get("https://www.glassdoor.com/profile/login_input.htm")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "modalUserEmail")))
        
        # Enter email
        driver.find_element(By.ID, "modalUserEmail").send_keys(credentials['username'])
        driver.find_element(By.ID, "modalUserPassword").send_keys(credentials['password'])
        driver.find_element(By.CSS_SELECTOR, "button[name='submit']").click()
        
        # Wait for login to complete
        WebDriverWait(driver, 10).until(EC.url_contains("glassdoor.com"))
        
        # Navigate to job posting
        driver.get(job_url)
        
        # Click apply button
        apply_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".applyButton"))
        )
        apply_button.click()
        
        # Handle application process (simplified)
        # The exact steps will depend on the specific job posting
        
        return "Glassdoor submission process started (may require manual completion)"
        
    except TimeoutException:
        return "Timeout on Glassdoor submission"
    except Exception as e:
        return f"Glassdoor submission error: {str(e)}"
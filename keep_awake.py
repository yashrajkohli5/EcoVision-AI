import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def wake_up_streamlit(url):
    # Set up Chrome options for headless mode (no UI window)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        print(f"Visiting {url} to keep it awake...")
        driver.get(url)
        
        # Give the Streamlit "Spinners" time to load the app
        time.sleep(10) 
        
        print("Page loaded successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    # Replace with your actual Streamlit URL
    STREAMLIT_URL = "https://ecovision-ai.streamlit.app/"
    
    # Run this in a loop or schedule it via Cron/Task Scheduler
    wake_up_streamlit(STREAMLIT_URL)

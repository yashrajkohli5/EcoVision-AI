import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def wake_up_apps(urls):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Adding a User-Agent helps avoid being blocked as a basic bot
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Wrap in list if only a single string is passed
        if isinstance(urls, str):
            urls = [urls]

        for url in urls:
            print(f"Visiting {url}...")
            driver.get(url)
            time.sleep(15) # Give it extra time to load the "Wake up" state

            # Logic to find and click the 'Wake up' button
            try:
                # Streamlit's 'Wake up' button usually contains this text
                wake_up_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Wake up')]")
                if wake_up_button:
                    wake_up_button.click()
                    print(f"Clicked 'Wake up' for {url}. Waiting for app to load...")
                    time.sleep(20) # Wait for the actual app to boot up
            except Exception:
                print(f"No 'Wake up' button found for {url}. App might already be awake.")

            print(f"Successfully processed {url}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    # You can add your Analytica URL here too!
    my_apps = ["https://ecovision-ai.streamlit.app/"] 
    wake_up_apps(my_apps)

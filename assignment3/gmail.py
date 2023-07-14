from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the YouTube homepage
driver.get("https://www.youtube.com")
time.sleep(3)

# Finding the search bar and entering text
search_bar = driver.find_element("name", "search_query")
search_bar.send_keys("Python tutorial")
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Selecting the first video from the search results
video_link = driver.find_element("xpath", "//ytd-video-renderer[1]//a[@id='thumbnail']")
video_link.click()

# Waiting for the video to load
time.sleep(5)

# Playing the video
play_button = driver.find_element("xpath", "//button[@aria-label='Play']")
play_button.click()

# Waiting for the video to play for 5 seconds
time.sleep(5)

# Closing the webdriver
driver.close()

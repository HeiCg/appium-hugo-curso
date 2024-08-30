from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from utils.data import get_window_size


def swipe(driver, start_x, start_y, end_x, end_y, duration=800):
    driver.swipe(start_x, start_y, end_x, end_y, duration)
    driver.implicitly_wait(time_to_wait=3)


def scroll_and_find_element(driver, xpath, max_scroll_attempts=5):
    width, height = get_window_size(driver)

    start_x = width / 2
    start_y = height * 0.8
    end_x = width / 2
    end_y = height * 0.2

    scroll_attempts = 0
    while scroll_attempts < max_scroll_attempts:
        try:
            element = driver.find_element(
                by=AppiumBy.XPATH,
                value=xpath
            )
            return element
        except NoSuchElementException:
            print("[ActionLog] Scrolling")
            swipe(driver, start_x, start_y, end_x, end_y)
            driver.implicitly_wait(time_to_wait=2)
            scroll_attempts += 1
    raise NoSuchElementException(f"Element not found {xpath}")

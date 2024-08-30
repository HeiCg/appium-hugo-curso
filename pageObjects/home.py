from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver import WebElement as MobileWebElement


class HomeScreen():
    option_search = dict(
        value="//android.widget.Button[@content-desc='Buscas']"
    )

    def __init__(self, driver) -> None:
        self.driver: webdriver = driver

    def tap_on_search(self) -> MobileWebElement:
        try:
            el = self.driver.find_element(
                by=AppiumBy.XPATH,
                value=self.option_search['value']
            )
            el.click()
        except NoSuchElementException:
            raise Exception(
                f"Element {self.option_search} was not found"
            ) from None
        self.driver.implicitly_wait(time_to_wait=2)
        return el

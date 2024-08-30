import unittest
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver import WebElement as MobileWebElement
# from selenium.common.exceptions import NoSuchElementException
from pageObjects.home import HomeScreen
from utils.actions import scroll_and_find_element


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='ZF524RZBHD',
    noReset=True
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    xpath_search = dict(
        value="""
        //android.widget.AutoCompleteTextView[
            @resource-id='android:id/search_src_text'
        ]"""
    )

    xpath_field_focused = dict(
        value="//*[@focused='true']"
    )

    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            appium_server_url,
            options=UiAutomator2Options().load_capabilities(capabilities)
        )
        self.driver.find_element

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_verify_listed_season_from_tv_shows(self) -> None:
        tv_shows = [
            "house",
            "the last kingdom",
            "hunter x hunter"
        ]

        # Step 1: Click on search
        HomeScreen(self.driver).tap_on_search()

        for tv_show in tv_shows:
            # Step 2: Typing
            el: MobileWebElement
            if self.driver.is_keyboard_shown():
                el = self.driver.find_element(
                            by=AppiumBy.XPATH,
                            value=self.xpath_field_focused['value']
                )
            else:
                el = self.driver.find_element(
                    by=AppiumBy.XPATH,
                    value=self.xpath_search['value']
                )
            el.send_keys(tv_show)
            self.driver.hide_keyboard()
            # Step 3: Tap on first suggestion displayed
            xpath_first_suggestions = dict(
                value="""//
                android.widget.GridView[
                    android.widget.LinearLayout[
                        android.widget.TextView[@text='Principais sugestões']
                    ]
                ]/androidx.recyclerview.widget.RecyclerView/android.widget.ImageView[1]
                """
            )

            self.driver.find_element(
                by=AppiumBy.XPATH,
                value=xpath_first_suggestions['value']
            ).click()

            # Step 4: Tap on seasons information
            xpath_season_info = dict(
                value="""
                    //android.widget.Button[
                        starts-with(@content-desc, "Temporada")
                    ]
                """
            )
            scroll_and_find_element(
                self.driver, xpath_season_info['value']
            ).click()
            # Step 5: Verify is all seasons availables appears
            Seasons = self.driver.find_elements(
                by=AppiumBy.XPATH,
                value="""
                    //androidx.recyclerview.widget.RecyclerView
                    //android.widget.Button
                """
            )
            print(f"{tv_show} - {[_.get_attribute('text') for _ in Seasons]}")
            [self.driver.back() for _ in range(3)]


if __name__ == '__main__':
    unittest.main()

def get_window_size(driver):
    size = driver.get_window_size()
    return size['width'], size['height']

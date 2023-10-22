from selenium.webdriver.common.by import By


class LoginPage:
    username_by_name_locator = "Email"
    password_by_name_locator = "Password"
    login_by_css_selector_locator = "button[type='submit']"
    logout_by_xpath_locator = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(by=By.NAME, value=self.username_by_name_locator).clear()
        self.driver.find_element(by=By.NAME, value=self.username_by_name_locator).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(by=By.NAME, value=self.password_by_name_locator).clear()
        self.driver.find_element(by=By.NAME, value=self.password_by_name_locator).send_keys(password)

    def login(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.login_by_css_selector_locator).click()

    def logout(self):
        self.driver.find_element(by=By.XPATH, value=self.logout_by_xpath_locator).click()


# if __name__ == '__main__':
#     url1 = 'https://admin-demo.nopcommerce.com/login'
#     driver_ = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     driver_.maximize_window()
#     driver_.implicitly_wait(10)
#     driver_.get(url=url1)
#
#     lp = LoginPage(driver=driver_)
#     lp.set_username(username='admin@yourstore.com')
#     time.sleep(2)
#     lp.set_password(password='admin')
#     time.sleep(2)
#     lp.login()
#     time.sleep(3)
#     lp.logout()
#     time.sleep(3)
#     driver_.quit()

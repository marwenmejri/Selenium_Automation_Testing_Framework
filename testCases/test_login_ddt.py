import time

from pagesObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import Logger
from utilities.data_utils import get_json_data, get_excel_data


class Test002DDTLogin:
    baseURL = ReadConfig.get_base_url()
    logger = Logger.sample_logger()
    # filename = 'TestData/LoginData.json'
    filename = 'TestData/LoginData.xlsx'

    def test_login_ddt(self, setup):
        self.logger.info("************** Test002DDTLogin Test started !! *************")
        self.logger.info("************** Login Test DDT started !! *************")
        driver = setup
        driver.get(url=self.baseURL)
        lp = LoginPage(driver=driver)
        status = []
        # output = get_json_data(filename=self.filename)
        output = get_excel_data(filename=self.filename)
        idx = 0
        for username, password, exp in output:
            idx += 1
            self.logger.info(f"*********** Iteration N° {idx} ************")
            lp.set_username(username=username)
            lp.set_password(password=password)
            lp.login()
            if driver.title == "Dashboard / nopCommerce administration":
                if exp == 'Pass':
                    status.append(True)
                    self.logger.info("************** Passed *************")
                else:
                    status.append(False)
                    self.logger.error("************** Failed *************")
                time.sleep(4)
                lp.logout()
            else:
                if exp == 'Pass':
                    status.append(False)
                    self.logger.error("************** Failed *************")
                else:
                    status.append(True)
                    self.logger.info("************** Passed *************")
        if all(status):
            self.logger.info("************** Test Login DDT Passed *************")
            driver.quit()
            assert True
        else:
            self.logger.info("************** Test Login DDT Failed !!! *************")
            driver.quit()
            assert False

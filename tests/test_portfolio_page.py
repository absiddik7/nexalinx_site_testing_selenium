import unittest
from selenium import webdriver
import utils.config as config
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PortfolioPageTest(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = webdriver.Chrome(config.CHROME_DRIVER_PATH)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.scroll_to_element = "arguments[0].scrollIntoView();"
         

    def test_portfolio_page(self):
        self.driver.get(config.BASE_URL)
        sleep(5)

        # verfiy clicking on the nav item Portfolio open correct page
        portfolio_navbar = self.driver.find_element(By.LINK_TEXT, "Portfolio")
        portfolio_navbar.click()
        self.assertEqual(self.driver.current_url, config.PORTFOLIO_PAGE_URL)
        sleep(5)

        # verify Some Of Our Finest Works text is present
        some_of_our_finest_works = self.driver.find_element(By.XPATH, "//strong[contains(text(),'Some Of Our Finest Works')]")
        self.assertTrue(some_of_our_finest_works.is_displayed())

        # verify Get Started Now button is present
        get_started_now_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Get Started Now!')]")
        self.assertTrue(get_started_now_button.is_displayed())

        #verify Web App and Mobile App button is present
        web_app_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Web App')]")
        self.assertTrue(web_app_button.is_displayed())
        mobile_app_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Mobile App')]")
        self.assertTrue(mobile_app_button.is_displayed())
        
        self.driver.quit()
        

    def test_get_started_now_button(self):
        self.driver.get(config.BASE_URL)
        sleep(5)
        # verfiy clicking on the nav item Portfolio open correct page
        portfolio_navbar = self.driver.find_element(By.LINK_TEXT, "Portfolio")
        portfolio_navbar.click()

        sleep(5)

        # verify Get Started Now button is present and open correct page
        get_started_now_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Get Started Now!')]")
        self.assertTrue(get_started_now_button.is_displayed())
        get_started_now_button.click()
        modal_window = self.driver.find_element(By.XPATH, "//div[@class='modal-dialog']")
        self.assertTrue(modal_window.is_displayed(), "Modal window is not displayed")
        sleep(3)
        close_btn = self.driver.find_element(By.XPATH, "//button[@class='btn-close']")
        close_btn.click()
        sleep(3)

        self.driver.quit()




    def test_get_started_now_form(self):
        self.driver.get(config.BASE_URL)
        sleep(5)
        # verfiy clicking on the nav item Portfolio open correct page
        portfolio_navbar = self.driver.find_element(By.LINK_TEXT, "Portfolio")
        portfolio_navbar.click()

        sleep(5)

        # verify Get Started Now button is present and open correct page
        get_started_now_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Get Started Now!')]")
        self.assertTrue(get_started_now_button.is_displayed())
        get_started_now_button.click()
        modal_window = self.driver.find_element(By.XPATH, "//div[@class='modal-dialog']")
        self.assertTrue(modal_window.is_displayed(), "Modal window is not displayed")
        sleep(3)

        # insert name in the form
        name_field = self.driver.find_element(By.XPATH, "//html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/input[1]")
        name_field.send_keys("Test Name")

        # insert email in the form
        email_field = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/input[1]")
        email_field.send_keys("test@gmail.com")

        # insert contact number in the form
        contact_number_field = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/input[1]")
        contact_number_field.send_keys("1234567890")

        # insert comment in the form
        comment_field = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/form[1]/div[5]/textarea[1]")
        comment_field.send_keys("Test Comment")

        # click on submit button
        submit_button = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/form[1]/div[6]/button[1]")
        submit_button.click()

        
        sleep(3)



    

    def tearDown(self):
        self.driver.close


    if __name__ == "__main__":
        unittest.main()
    

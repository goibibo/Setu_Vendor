import unittest
import urllib2
import json
import time
import logging
from selenium import webdriver
#import HTMLTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException

class sanity(unittest.TestCase):
      def setUp(self):
          self.ApiUrl = "http://www.goibibo.com"
          # define browser Instance chrome
          self.driver = webdriver.Chrome("/opt/google/chrome/chromedriver")
          # Maximum browser window
          self.driver.maximize_window()
          print "cursor test: " + self._testMethodName

      def vendorthree(self):
          driver = self.driver

          driver.get(self.ApiUrl)
          time.sleep(10)
          driver.get("http://www.goibibo.com")
          time.sleep(2)
          element = driver.find_element_by_link_text('Sign In')
          element.click()
          time.sleep(2)

          driver.switch_to_frame(driver.find_element_by_id("authiframe"))
          login = driver.find_element_by_link_text('Log In')
          login.click()
          username = driver.find_element_by_id("authUsername").send_keys("mishrarishav@outlook.com")
          password = driver.find_element_by_id("authPassword").send_keys("rishumishra")
          signin_button = driver.find_element_by_id("authExistingUserSignInBtn")
          signin_button.click()
          time.sleep(5)
          print "User : Rishav"
          print "Password: **********"



          LOG_FILENAME = "a.log"
          logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
          logging.info("Chrome Instance started")


          Navigation = driver.find_element(By.LINK_TEXT, 'Flight + Hotels')
          Navigation.click()
          LOG_FILENAME = "a.log"
          logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
          logging.info("\n")
          print "FPH Clicked"
          time.sleep(5)

          source = driver.find_element_by_id("fph-from-input")
          source.send_keys("del")
          time.sleep(1.5)
          source.send_keys(Keys.DOWN)
          source.send_keys(Keys.ENTER)
          src_val = source.get_attribute('value')
          print src_val

          destinaton = driver.find_element_by_id("fph-to-input")
          destinaton.send_keys("kolk")
          time.sleep(1.5)
          destinaton.send_keys(Keys.DOWN)
          destinaton.send_keys(Keys.ENTER)
          dest_val = destinaton.get_attribute('value')
          print dest_val


          start_date = driver.find_element_by_id("start-date")
          start_date.click()
          date =driver.find_element_by_id("jrdp_start-calen_6_21_2017")
          date.click()
          start_date1 = driver.find_element_by_id("start-date")
          print "Starting date is :" , start_date1.get_attribute('value')

          traveller = driver.find_element_by_id("fph-pax")
          traveller.click()

          adult_1 = driver.find_element_by_id("fph-pax-adult")
          print "No of Pax :" , adult_1.get_attribute('value')

          close_for_pax = driver.find_element_by_id("fph-pax-close")
          close_for_pax.click()

          Search = driver.find_element_by_id("fph_search_btn")
          Search.click()
          print "Search Clicked"

          print "Welcome to SRP Page"
          print "Validation for V3 Hotels"

          time.sleep(7)
          see_all_hotel = driver.find_element_by_xpath("//a[contains(text(),'See All Hotels')]")
          see_all_hotel.click()

          print "See All Hotel Clicked"

          time.sleep(4)
          driver.execute_script("document.getElementsByName('hotelNameTextBox')[0].click();")

          time.sleep(2)

          hotel_name = driver.find_element_by_xpath("//div[@class='ht_shName']//input[@class='htr_iptx ui-autocomplete-input']")
          hotel_name.click()

          time.sleep(4)
          hotel_name.send_keys("Park Plaza Kolkata Ballygunge")
          time.sleep(4)
          hotel_name.send_keys(Keys.DOWN)
          hotel_name.send_keys(Keys.ENTER)
          hotel_name.click()
          ht_val = hotel_name.get_attribute('value')
          print ht_val


          combo_price = driver.find_element_by_xpath("//span[@class='ht_button fr']")
          combo_price.click()

          time.sleep(6)
          book_deal = driver.find_element_by_xpath("//button[contains(text(),'Book Combo Deal')]")
          book_deal.click()


          print "BOOK COMBO"

          print "------------------------------------------"
          print "Traveller Detail Page"

          try:
              time.sleep(3)
              farepopup = driver.find_elements_by_xpath("//h4[contains(text(),'Oh! There has been a change in the fare.')]")
              close = driver.find_element_by_xpath("//a[contains(@class,'popClose')]")
              time.sleep(2)
              close.click()

          except Exception as e:
              print e.message
              print "No Fare Raise Or dip"

          time.sleep(8)

          driver.execute_script("window.scrollTo(0, 400)")

          title = driver.find_element_by_id("pax_adult_title_0")
          title.send_keys(Keys.DOWN)
          title.send_keys(Keys.DOWN)
          title.click()

          first_name = driver.find_element_by_id("pax_adult_firstname_0")
          first_name.send_keys("Test")
          fir_val = first_name.get_attribute('value')
          print fir_val

          last_name = driver.find_element_by_id("pax_adult_lastname_0")
          last_name.send_keys("Automation")
          las_val = last_name.get_attribute('value')
          print las_val

          email = driver.find_element_by_id("email")
          email.clear()
          email.send_keys("rishav.mishra@go-mmt.com")
          em_val = email.get_attribute('value')
          print em_val

          mobile = driver.find_element_by_id("mobile")
          mobile.send_keys("9999999999")
          mob_val = mobile.get_attribute('value')
          print  mob_val

          pay = driver.find_element_by_id("makePayment")
          print pay.text
          pay.click()

          print "----------------------------------------------"
          print "PAYMENT PAGE"

          time.sleep(7)

          driver.execute_script("window.scrollTo(0, 400)")
          #wait = WebDriverWait(driver, 10)
          try:
              ui.WebDriverWait(driver,timeout = 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class = 'bkOfferTag fl']")))
              return True
          except TimeoutException:
              print ':::session expire text did not come::::'
              return False


          #element = wait.until(EC.element_to_be_presence((By.XPATH, "//div[@class = 'bkOfferTag fl']")))
          print " Session Expire "


      def tearDown(self):
          self.driver.close()
      
if __name__ == "__main__":
     unittest.main()
   #suite = unittest.TestSuite()
   #suite.addTest(sanity("vendorthree"))
    

   #runner = HTMLTestRunner.HTMLTestRunner()
   #runner.run(suite)

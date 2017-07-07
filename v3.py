import unittest
import urllib2
import json
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import HTMLTestRunner
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SetuRegressionSuite(unittest.TestCase):
        def setUp(self):
            self.ApiUrl = "https://sanityprodpp.goibibo.com/go/f/"
            # define browser Instance chrome
            self.driver = webdriver.Chrome("/opt/google/chrome/chromedriver")
            # Maximum browser window
            self.driver.maximize_window()
            print "cursor test: " + self._testMethodName

            LOG_FILENAME = "a.log"
            logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
            logging.info("Chrome Instance started")

        def test_to_login(self):
            driver = self.driver
            # Navigate to UI
            driver.get(self.ApiUrl)
            time.sleep(10)
            driver.get("https://sanityprodpp.goibibo.com/go/f/")
            time.sleep(2)
            element = driver.find_element_by_link_text('Sign In')
            element.click()

            #sigin = driver.find_element_by_id("get_sign_in")
            time.sleep(2)
            signin_frame = driver.find_element_by_id("authiframe")
            driver.switch_to_frame(driver.find_element_by_id("authiframe"))
            login = driver.find_element_by_link_text('Log In')
            login.click()
        
            username = driver.find_element_by_id("authUsername").send_keys("shilpanaik.bs1@gmail.com")
            password = driver.find_element_by_id("authPassword").send_keys("shiven71011")
            signin_button = driver.find_element_by_id("authExistingUserSignInBtn")
            signin_button.click()
            time.sleep(5)

        def GDS_LCC(self):
            driver = self.driver
            driver.get(self.ApiUrl)
            time.sleep(10)
            driver.get("https://sanityprodpp.goibibo.com/go/f/")
            time.sleep(5)

            source = driver.find_element_by_id("fph-from-input")
            source.send_keys("Bangalore")
            time.sleep(10)
            source.send_keys(Keys.DOWN)
            source.send_keys(Keys.ENTER)
            dest = driver.find_element_by_id("fph-to-input")
            dest.send_keys("Chennai")
            time.sleep(10)
            dest.send_keys(Keys.DOWN)
            dest.send_keys(Keys.ENTER)
            time.sleep(2)
            date = driver.find_element_by_id("start-date")
            date.click()
            pickdate = driver.find_element(By.XPATH, ".//*[@id='jrdp_start-calen_6_28_2017']")
            pickdate.click()
            time.sleep(2)
            day = driver.find_element(By.XPATH, "//*[@id='start-date']")
            date = driver.find_element_by_id("start-date")
            print "2. date is:", date.get_attribute('value')
            print date.get_attribute('value')
            time.sleep(2)
            self.assertEqual(date.get_attribute('value'), '28 Jul 2017')

            date1 = driver.find_element_by_id("end-date")
            date1.click()
            pickdate1 = driver.find_element(By.XPATH, ".//*[@id='jrdp_end-calen_6_30_2017']")
            pickdate1.click()
            time.sleep(1.5)
            day1 = driver.find_element(By.XPATH, "//*[@id='end-date']")
            date1 = driver.find_element_by_id("end-date")
            print "3. date is:", date1.get_attribute('value')
            print date1.get_attribute('value')
            time.sleep(1.5)
            self.assertEqual(date1.get_attribute('value'), '30 Jul 2017')

            classtype = driver.find_element_by_id("fph-class")
            classtype.click()
            select3 = Select(classtype)
            select3.select_by_value("E")
            classtype = driver.find_element_by_id("fph-class")
            classtype.get_attribute('value')
            print classtype.get_attribute('value')
            if classtype.get_attribute('value') == "E":
                print "4. It is Economy class"

            else:
                print "5. It is not Economy Class"

            fph_button = driver.find_element_by_id("fph_search_btn")
            fph_button.click()
            time.sleep(1.5)

            # Source and Destination validation

            # place = driver.find_element_by_xpath(".//*[@id='fph-srp-breadcrum']/span[1]")
            # print "Place is:", place.text

            # if place.text == place.text:
            # print 'Place validation is correct', place.text
            # else:
            # print "Its place bug"

            time.sleep(10)

            srprice = driver.find_element_by_xpath("//div[2]/span[2]/span")
            print "6. Price in the srps:", srprice.text

            saveprice = driver.find_element_by_xpath(
                './/*[@id="fph-srp-itinerary-holder"]/section[1]/div[2]/div[2]/span[1]')
            print "7. Save Rs. is:", str(saveprice.text)

            # Selecting Hotels and Room Type
            try:
                block = driver.find_element(By.CSS_SELECTOR, "div.moreHtlBlk")
                time.sleep(5)
                # frame = driver.find_element_by_xpath(".//*[@id='fph-srp-itinerary-holder']/section[1]/div[3]/div/div[2]/div/div/div/div[3]/div/div[1]/div/div[1]/label")
                # frame.click()
                frame = driver.find_element_by_xpath(
                    "//section[@id='fph-srp-itinerary-holder']/section/div[3]/div/div[2]/div/div/div/div[3]")
                frame1 = driver.find_element_by_css_selector("label..firepath-matching-node")
                frame1.click()
                selection = driver.find_element_by_xpath(
                    "//section[@id='fph-srp-itinerary-holder']/section/div[3]/div/div[2]/div/div/div/div[3]/div/div/div/div[3]/span")
                print "8. Room Select is:", selection.text
                r = selection.text
                time.sleep(1)
            except NoSuchElementException:
                print "9. No Found....continuing script"

            show_room = driver.find_element_by_name("fph-srp-detail-hotel")
            show_room.click()
            time.sleep(15)
            roomtype = driver.find_element(By.CSS_SELECTOR, "#change-hotel-room > div.popContent > #changehotelscontainer")
            time.sleep(5)
            v = driver.find_element(By.ID, "changehotelscontainer")
            time.sleep(10)
            va = driver.find_element_by_xpath("//ul[@id='dp_roomListing']/li[1]")
            time.sleep(2)
            ovalue = va.find_element(By.XPATH, "//ul[@id='dp_roomListing']/li[1]/span/a")
            print "10. New Room type is:", ovalue.text
            # dvalue = va.find_element(By.XPATH, "//ul[@id='dp_roomListing']/li[3]/p/span/small")
            # print "New Room type description is:", dvalue.text
            pvalue = va.find_element_by_xpath("//ul[@id='dp_roomListing']/li[1]/p[3]/em")
            print "11. New price value is:", pvalue.text
            selecttype = va.find_element_by_xpath("//ul[@id='dp_roomListing']/li[1]/span/a")
            selecttype.click()
            time.sleep(1)
            onselection = driver.find_element_by_xpath("//div[3]/div/div/div/div[3]/span[3]")
            print '12. Room type on selection from showroom is:', onselection.text
            if not onselection.text == ovalue.text:
                print " 13. Room selection validation is success"
            else:
                print "14. There is roomtype selection bug"

            srprice = driver.find_element_by_xpath("//div[2]/span[2]/span")
            print "15. Price in the srps:", srprice.text

            saveprice = driver.find_element_by_xpath(
                './/*[@id="fph-srp-itinerary-holder"]/section[1]/div[2]/div[2]/span[1]')
            print "16. Save Rs. is:", str(saveprice.text)

            # Change Flight

            changeflight = driver.find_element(By.XPATH,
                                               './/*[@id="fph-srp-itinerary-holder"]/section[1]/div[1]/div[1]/div[2]/span/a')
            changeflight.click()

            changeflightprice = driver.find_element_by_class_name("ourPrice")
            print "17. Price in Change flight form is:", changeflightprice.text

            changeflightsaveprice = driver.find_element_by_xpath(
                ".//*[@id='fph-popup-window-flight-change']/div/div[1]/div/div[2]/span")
            print "18. Save Rs. is:", str(changeflightsaveprice.text)

            if srprice.text == changeflightprice.text:
                print "19. price match is correct"
            else:
                print "20. Value price is incorrect and its bug"

            if changeflightsaveprice.text == saveprice.text:
                print "21. save value match is correct"
            else:
                print "22. save value is incorrect and its bug"

            wait1 = driver.find_element_by_xpath("//div[@id='fph-popup-window-flight-change']/div/div[2]/div[3]")
            time.sleep(15)
            # stops = driver.find_element_by_id("fltst")
            # onestop = driver.find_element_by_xpath("(//input[@name='fSt'])[2]")
            # onestop.click()
            airlinefilter = driver.find_element_by_id("fltcrr-div")
            time.sleep(5)

            # stops = driver.find_element_by_xpath("/div[@id='fltst-div']/label[2]/input")
            # stops.click()
            gds1 = driver.find_element_by_xpath("//ul[@id='fl']/li/div/dfn/label/input")
            gds1.click()
            gds2 = driver.find_element_by_xpath("//ul[@id='ol']/li/div/dfn/label/input")
            gds2.click()
            onwardflight = driver.find_element_by_xpath("//ul[@id='fl']/li/div/dfn")
            onwardflightno = driver.find_element_by_xpath("//ul[@id='fl']/li/div/samp/span/i")
            print "23. Onward flight is:", onwardflightno.text
            returnflight = driver.find_element_by_xpath("//ul[@id='ol']/li[30]/div/samp/span")
            returnflightno = driver.find_element_by_xpath("//ul[@id='ol']/li[30]/div/samp/span/i")
            print "24. Return flight is:", returnflightno.text
            newairline = driver.find_element_by_xpath(
                ".//*[@id='fph-popup-window-flight-change']/div/div[1]/ul/li[1]/div/div[1]/div[2]")
            time.sleep(5)
            j1 = driver.find_element_by_xpath(
                "//div[@id='fph-popup-window-flight-change']/div/div/ul/li/div/div/div[2]/span")
            print "25. Onward Journey is:", j1.text
            t1 = driver.find_element_by_xpath(
                "//div[@id='fph-popup-window-flight-change']/div/div/ul/li/div/div/div[2]/span[3]")
            print "26. Time is:", t1.text
            s1 = driver.find_element_by_xpath(
                "//div[@id='fph-popup-window-flight-change']/div/div/ul/li/div/div/div[2]/span[4]")
            print "27. Stop is:", s1.text
            j2 = driver.find_element_by_xpath(
                "//div[@id='fph-popup-window-flight-change']/div/div/ul/li/div/div[2]/div[2]/span")
            print "28. Return Journey is:", j2.text
            t2 = driver.find_element_by_xpath(
                "//div[@id='fph-popup-window-flight-change']/div/div/ul/li/div/div[2]/div[2]/span[3]")
            print "29. Time is:", t2.text
            s2 = driver.find_element_by_xpath(
                "//div[@id='fph-popup-window-flight-change']/div/div/ul/li/div/div[2]/div[2]/span[4]")
            print "30. Stop is:", s2.text
            originalvalue = driver.find_element_by_xpath("//div[@id='fph-popup-window-flight-change']/div/div/div/div/span")
            print "31. Original value was:", originalvalue.text
            Discountvalue = driver.find_element_by_xpath("//div/div/div/div/span[2]")
            t = Discountvalue.text
            print "32. Dicounted Value is:", t
            save = driver.find_element_by_xpath("//div[@id='fph-popup-window-flight-change']/div/div/div/div[2]/span")
            print "33. Your saving:", save.text
            bookcombo = driver.find_element_by_xpath(
                ".//*[@id='fph-popup-window-flight-change']/div/div[1]/div/div[2]/div/button")
            bookcombo.click()
            time.sleep(5)

            try:
                time.sleep(2)
                farepopup = driver.find_elements_by_xpath("//div[@id='go_gi_fare_failiure']/div/div")
                elem = driver.find_element_by_xpath("//div[@id='go_gi_fare_failiure']/div/h4")
                if elem.is_displayed():
                    newfare = driver.find_element_by_xpath("//div[@id='go_gi_fare_failiure']/div/div/div/div/p/span")
                    # oldfare
                    oldfare = driver.find_element_by_xpath("//div[@id='go_gi_fare_failiure']/div/div/div/div/p[2]/span")
                    newfarevalue = driver.find_element_by_xpath(
                        "//div[@id='go_gi_fare_failiure']/div/div/div/div/p/span[2]")
                    print "34. New fare value is:", newfarevalue.text
                    oldfarevalue = driver.find_element_by_xpath(
                        "//div[@id='go_gi_fare_failiure']/div/div/div/div/p[2]/span[2]")
                    print "35. Old fare value is:", oldfarevalue.text
                    Increasesymbol = driver.find_element_by_xpath("//div[@id='go_gi_fare_failiure']/div/div/div/div[2]/i")
                    print "36. Symbol is:", Increasesymbol.text
                    Increasedto = driver.find_element_by_xpath(
                        "//div[@id='go_gi_fare_failiure']/div/div/div/div[2]/span/span")
                    print "37. Price increased to:", Increasedto.text
                    okbutton = driver.find_element_by_xpath("//div[@id='go_gi_fare_failiure']/div/div/div[2]/button")
                    okbutton.click()
            except NoSuchElementException:
                print "38. Fare dip or Rise was not found....continuing script"

            # Booking page validation

            grandtotal = driver.find_element_by_xpath("//div[11]/div[2]/div/div[2]/div")
            r = grandtotal.text
            print "39. Grand total after reprice is:", r

            if t == r:
                print "40. Total after remains same:Awesome"
            else:
                print "41. Ohh there is either dip or rise or not same without pop up"

            # Booking Page Validation
            Pleasenote = driver.find_element_by_xpath("//div[@id='trip_step']/div[2]/div/span")
            # farerules = driver.find_element_by_xpath("(//a[contains(@href, 'javascript:void(0);')])[3]")
            # time.sleep(5)
            # dest = driver.find_element_by_xpath("//div[@id='fareRulespopUp']/div[2]/div/h5")
            # print "Destination Place is", dest.text
            # if dest.text == "BLR-DEL:":
            # print "Its correct place destination"
            # else:
            # print  "Its wrong place destination"

            # closebutton = driver.find_element_by_xpath("//a[@onclick='gi.trip.closePopup();']")
            # closebutton.click()
            Roomtypp = driver.find_element_by_xpath("//div[@id='hotelDetail']/div[2]/div/h1")
            print "42. Room Type on Booking page is:", Roomtypp.text
            s = Roomtypp.text
            time.sleep(10)
            # "Validation for Room type is correct"

            ## print  "Validation of Room Type is Wrong"

            # offersgocash = driver.find_element_by_xpath("//div[@id='promo_cont_box']/label/input")
            # offersgocash.click()
            # time.sleep(3)
            # offerpopup = driver.find_element_by_xpath("//div[@id='go_gi_fare_dialog']/div/div")
            # offersgocash.text
            # offersgocashclose = driver.find_element_by_xpath("(//a[contains(@href, 'javascript:void(0)')])[12]")
            # offersgocashclose.click()

            # Travellers Details

            titelselect = driver.find_element_by_xpath("//div[@id='adult_cont_1']/div[2]/div/div/select")
            titelselect.click()
            select4 = Select(titelselect)
            select4.select_by_value('1')
            titelselect = driver.find_element_by_xpath("//div[@id='adult_cont_1']/div[2]/div/div/select")
            titelselect.get_attribute('value')
            print titelselect.get_attribute('value')
            Firstname = driver.find_element_by_id("pax_adult_firstname_0")
            Firstname.send_keys("Shilpa")
            Middlename = driver.find_element_by_id("pax_adult_middlename_0")
            Middlename.send_keys("Naik")
            Lastname = driver.find_element_by_id("pax_adult_lastname_0")
            Lastname.send_keys("Venkatesh")
            EmailId = driver.find_element_by_id("email")
            EmailId.clear()
            EmailId.send_keys("shilpa.naik@goibibo.com")
            MobileNo = driver.find_element_by_id("mobile")
            MobileNo.clear()
            MobileNo.send_keys(9900150217)
            MakePayment = driver.find_element_by_id("makePayment")
            MakePayment.click()
            time.sleep(2)


        def Oneway(self):
            driver = self.driver
            #driver.get(self.ApiUrl)
            #time.sleep(5)
            driver.get("https://sanityprodpp.goibibo.com/go/fph/search/air-6771549831164675055-2820046943342890302-20170807-20170808-1-0-0-E-111/hotels-2820046943342890302-20170807-20170808-1/917/")

            time.sleep(10)


            srprice = driver.find_element_by_xpath("//div[2]/span[2]/span")
            print "5. Price in the srps:", srprice.text

            saveprice = driver.find_element_by_xpath(
                './/*[@id="fph-srp-itinerary-holder"]/section[1]/div[2]/div[2]/span[1]')
            print "6. Save Rs. is:", str(saveprice.text)

            # Selecting Hotels and Room Type
            try:
                block = driver.find_element(By.CSS_SELECTOR, "div.moreHtlBlk")
                time.sleep(5)
                # frame = driver.find_element_by_xpath(".//*[@id='fph-srp-itinerary-holder']/section[1]/div[3]/div/div[2]/div/div/div/div[3]/div/div[1]/div/div[1]/label")
                # frame.click()
                frame = driver.find_element_by_xpath(
                    "//section[@id='fph-srp-itinerary-holder']/section/div[3]/div/div[2]/div/div/div/div[3]")
                frame1 = driver.find_element_by_css_selector("label..firepath-matching-node")
                frame1.click()
                selection = driver.find_element_by_xpath(
                    "//section[@id='fph-srp-itinerary-holder']/section/div[3]/div/div[2]/div/div/div/div[3]/div/div/div/div[3]/span")
                print "7. Room Select is:", selection.text
                r = selection.text
                time.sleep(1)
            except NoSuchElementException:
                print "8. No Found....continuing script"

            show_room = driver.find_element_by_name("fph-srp-detail-hotel")
            show_room.click()
            time.sleep(10)
            roomtype = driver.find_element(By.CSS_SELECTOR,
                                           "#change-hotel-room > div.popContent > #changehotelscontainer")
            time.sleep(10)
            v = driver.find_element(By.ID, "changehotelscontainer")
            time.sleep(5)
            va = driver.find_element_by_xpath("//ul[@id='dp_roomListing']/li[1]")
            time.sleep(2)
            ovalue = va.find_element(By.XPATH, "//ul[@id='dp_roomListing']/li[1]/span/a")
            print "9. New Room type is:", ovalue.text
            # dvalue = va.find_element(By.XPATH, "//ul[@id='dp_roomListing']/li[3]/p/span/small")
            # print "New Room type description is:", dvalue.text
            # pvalue = va.find_element_by_xpath("//ul[@id='dp_roomListing']/li[3]/p[3]/em")
            # print "New price value is:", pvalue.text
            selecttype = va.find_element_by_xpath("//ul[@id='dp_roomListing']/li[1]/span/a")
            selecttype.click()
            time.sleep(1)
            onselection = driver.find_element_by_xpath("//div[3]/div/div/div/div[3]/span[3]")
            print '10. Room type on selection from showroom is:', onselection.text
            if not onselection.text == ovalue.text:
                print "11. Room selection validation is success"
            else:
                print "12. There is roomtype selection bug"

            srprice = driver.find_element_by_xpath("//div[2]/span[2]/span")
            print "13. Price in the srps:", srprice.text

            saveprice = driver.find_element_by_xpath(
                './/*[@id="fph-srp-itinerary-holder"]/section[1]/div[2]/div[2]/span[1]')
            print "14. Save Rs. is:", str(saveprice.text)

            # Click on Book button
            button = driver.find_element_by_xpath(".//*[@id='fph-srp-itinerary-holder']/section[1]/div[2]/div[3]/button")
            button.click()
            time.sleep(10)

            try:
                time.sleep(2)
                farepopup = driver.find_elements_by_xpath("//div[@id='go_gi_fare_failiure']/div/div")
                elem = driver.find_element_by_xpath("//div[@id='go_gi_fare_failiure']/div/h4")
                if elem.is_displayed():
                    newfare = driver.find_element_by_xpath("//div[@id='go_gi_fare_failiure']/div/div/div/div/p/span")
                    # oldfare
                    oldfare = driver.find_element_by_xpath("//div[@id='go_gi_fare_failiure']/div/div/div/div/p[2]/span")
                    newfarevalue = driver.find_element_by_xpath(
                        "//div[@id='go_gi_fare_failiure']/div/div/div/div/p/span[2]")
                    print "15. New fare value is:", newfarevalue.text
                    oldfarevalue = driver.find_element_by_xpath(
                        "//div[@id='go_gi_fare_failiure']/div/div/div/div/p[2]/span[2]")
                    print "16. Old fare value is:", oldfarevalue.text
                    Increasesymbol = driver.find_element_by_xpath("//div[@id='go_gi_fare_failiure']/div/div/div/div[2]/i")
                    print "17. Symbol is:", Increasesymbol.text
                    Increasedto = driver.find_element_by_xpath(
                        "//div[@id='go_gi_fare_failiure']/div/div/div/div[2]/span/span")
                    print "18. Price increased to:", Increasedto.text
                    okbutton = driver.find_element_by_xpath("//div[@id='go_gi_fare_failiure']/div/div/div[2]/button")
                    okbutton.click()
            except NoSuchElementException:
                print "19. Fare dip or Rise was not found....continuing script"

            grandtotal = driver.find_element_by_xpath("//div[@id='fr_tot_amnt_box']/div[2]/div")
            r = grandtotal.text
            print "20. Grand total after reprice is:", r

            # if t == r:
            # print "Total after remains same:Awesome"
            # else:
            # print "Ohh there is either dip or rise or not same without pop up"

            # Booking Page Validation
            Pleasenote = driver.find_element_by_xpath("//div[@id='trip_step']/div[2]/div/span")
            # farerules = driver.find_element_by_xpath("(//a[contains(@href, 'javascript:void(0);')])[3]")
            # time.sleep(5)
            # dest = driver.find_element_by_xpath("//div[@id='fareRulespopUp']/div[2]/div/h5")
            # print "Destination Place is", dest.text
            # if dest.text == "BLR-DEL:":
            # print "Its correct place destination"
            # else:
            # print  "Its wrong place destination"

            # closebutton = driver.find_element_by_xpath("//a[@onclick='gi.trip.closePopup();']")
            # closebutton.click()
            Roomtypp = driver.find_element_by_xpath("//div[@id='hotelDetail']/div[2]/div/h1")
            print "21. Room Type on Booking page is:", Roomtypp.text
            s = Roomtypp.text
            time.sleep(10)
            # "Validation for Room type is correct"

            ## print  "Validation of Room Type is Wrong"

            # offersgocash = driver.find_element_by_xpath("//div[@id='promo_cont_box']/label/input")
            # offersgocash.click()
            # time.sleep(3)
            # offerpopup = driver.find_element_by_xpath("//div[@id='go_gi_fare_dialog']/div/div")
            # offersgocash.text
            # offersgocashclose = driver.find_element_by_xpath("(//a[contains(@href, 'javascript:void(0)')])[12]")
            # offersgocashclose.click()

            # Travellers Details

            titelselect = driver.find_element_by_xpath("//div[@id='adult_cont_1']/div[2]/div/div/select")
            titelselect.click()
            select4 = Select(titelselect)
            select4.select_by_value('1')
            titelselect = driver.find_element_by_xpath("//div[@id='adult_cont_1']/div[2]/div/div/select")
            titelselect.get_attribute('value')
            print titelselect.get_attribute('value')
            Firstname = driver.find_element_by_id("pax_adult_firstname_0")
            Firstname.send_keys("Shilpabs")
            Middlename = driver.find_element_by_id("pax_adult_middlename_0")
            Middlename.send_keys("Naikbs")
            Lastname = driver.find_element_by_id("pax_adult_lastname_0")
            Lastname.send_keys("Venkateshkumar")
            EmailId = driver.find_element_by_id("email")
            EmailId.clear()
            EmailId.send_keys("shilpa.naik@goibibo.com")
            MobileNo = driver.find_element_by_id("mobile")
            MobileNo.clear()
            MobileNo.send_keys(9900150217)
            MakePayment = driver.find_element_by_id("makePayment")
            MakePayment.click()
            time.sleep(2)
        
        
        

        def tearDown(self):
            self.driver.close()
            print "test is over"


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(SetuRegressionSuite("test_to_login"))
    suite.addTest(SetuRegressionSuite("GDS_LCC"))
    #suite.addTest(SetuRegressionSuite("LCC"))
    suite.addTest(SetuRegressionSuite("Oneway"))
    #suite.addTest(SetuRegressionSuite("SetuInt"))
    #suite.addTest(SetuRegressionSuite("Dom_Oneway_Upsell"))
    #suite.addTest(SetuRegressionSuite("International_oneway_Upsell"))

    runner = HTMLTestRunner.HTMLTestRunner()
    runner.run(suite)

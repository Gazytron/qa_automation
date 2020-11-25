from selenium import webdriver
import requests
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
import pytest
# import HtmlTestRunner


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # Methods in UnitTest should start from "test" keyword
    def test_search(self):

        driver = self.driver
        driver.get("https://qasvus.wixsite.com/ca-marketing")
        self.assertIn("Home | California Marketing", driver.title)
        print("Page has", driver.title + " as Page title")
        time.sleep(2)


        body = driver.find_element_by_css_selector('body')
        #body.click()



        i1 = driver.find_element(By.XPATH,("//p[@id='comp-kcu4j5tk1label']"))
        if i1:
            print("Blog is found")
            i1.click()
        else:
            print("Blog is not found")
        time.sleep(3)

        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        body.send_keys(Keys.PAGE_UP)
        time.sleep(1)
        all_posts = driver.find_element(By.XPATH, "//a[contains(text(),'All Posts')]")
        print(all_posts.location)
        if all_posts:
            print("All posts found")
        try:
            #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
            wait = WebDriverWait(driver, 5)
            wait.until(EC.element_to_be_clickable(By.XPATH, "//a[contains(text(),'All Posts')]"))
            wait.until(EC.invisibility_of_element_located(By.XPATH, "//a[contains(text(),'All Posts')]"))
            all_posts.click()
        except:
            body.send_keys(Keys.PAGE_UP)
            all_posts.click()





        time.sleep(2)
        ss2 = driver.find_element(By.XPATH, "//p[@id='comp-kcu4j5tk2label']")
        if ss2:
            print("Shop is found")
            try:
                ss2.click()
            except:
                body.send_keys(Keys.PAGE_DOWN)
                ss2.click()
        else:
            print("Shop not found")
        time.sleep(2)
        items = driver.find_elements(By.XPATH,"//ul[@class='_3Xnzg _3g8J4']")
        if len(items)<1:
            print("Products weren't populated")
        else:
            print("Products were populated")
        time.sleep(2)

        login = driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]")
        login.click()
        print("First login clicked")
        time.sleep(2)

        w2 = driver.find_element(By.XPATH,"//div[@role='dialog']")
        w2.click()
        lin = driver.find_element(By.XPATH, "//button[contains(text(),'Log In')]")

        lin.click()
        print("Second login clicked")
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Log in with Email')]")))
        w_email = driver.find_element(By.XPATH,"//span[contains(text(),'Log in with Email')]")
        w_email.click()
        print("login with email clicked")

        time.sleep(3)
        emaile = driver.find_element(By.XPATH,"(//input)[2]")
        #emaile.clear()
        emaile.send_keys("best@best.best")
        pswd = driver.find_element(By.XPATH, "//input[@type='password']")
        #pswd.clear()
        pswd.send_keys("best123")
        pswd.send_keys(Keys.RETURN)
        #print(emaile.is_displayed()," and ",emaile.is_enabled(), " ", emaile.location)
        #print(pswd.is_displayed()," and ",pswd.is_enabled(), " ", pswd.location)
        time.sleep(3)
        aa1 = driver.find_element(By.XPATH,"//div[@aria-label='Members bar']")
        assert "Hello best" in aa1.text
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 0)")
        time.sleep(2)

        logout = driver.find_element(By.XPATH, "//button[@aria-label='best account menu']")
        logout.click()
        time.sleep(2)
        logout2 = driver.find_elements_by_tag_name("nav")
        logout2[2].click()
        #logout2.click()

        time.sleep(2)
        print("End of test")

        #self.assertTrue(i1)
        #driver.find_element(By.XPATH, "//a[contains(text(),'Log In')]").click()
        #time.sleep(3)
        #driver.find_element(By.XPATH, "//span[contains(text(),'Log in with Email')]").click()
        #time.sleep(3)
        #driver.find_element(By.ID, "input_input_emailInput_SM_ROOT_COMP10").send_keys("best@best.best")
        #driver.find_element(By.ID, "input_input_passwordInput_SM_ROOT_COMP10").send_keys("best123")
        #driver.find_element(By.XPATH,
         #                   "//body/div[@id='SITE_CONTAINER']/div[@id='main_MF']/div[6]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/button[1]/span[1]").click()
        #time.sleep(2)

    def tearDown(self):
        self.driver.quit()

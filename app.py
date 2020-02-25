import time
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import scipy.interpolate as si


def menu():
    email = 'YOUR EMAIL OR USERNAME'
    pw = 'YOUR PASSWORD'
    membean(email, pw)


def membean(email, pw):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("start-maximized")
    options.add_argument('disable-infobars')
    options.set_capability("browser.cache.disk.enable", False)
    options.set_capability("browser.cache.memory.enable", False)
    options.set_capability("browser.cache.offline.enable", False)
    options.set_capability("network.http.use-cache", False)
    driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
    driver.delete_all_cookies()
    driver.get('https://membean.com')

    driver.find_element_by_xpath('//a[@class = "nav-login"]').click()
    driver.find_element_by_xpath('//input[@id = "user_username"]').send_keys(email)
    driver.find_element_by_xpath('//input[@id = "user_password"]').send_keys(pw)
    driver.find_element_by_xpath('//div[@class = "form-group"]//button[@type = "submit"]').submit()
    time.sleep(3)
    driver.find_element_by_xpath('//a[@id = "startTrainingBtn"]').click()

    done = False

    while done == False:
        action = ActionChains(driver)
        edit_link = driver.find_elements_by_xpath('//head//link[@rel = "stylesheet"]')
        edit_link = edit_link[1]
        driver.execute_script("arguments[0].href = ''", edit_link)
        try:
            driver.find_element_by_xpath('//input[@id = "15_min_"]').click()
        except:
            pass
        random_num = random.randint(1, 4)
        if random_num != 4:
            try:
                points = [[0, 0], [0, 2], [2, 3], [4, 0], [6, 3], [8, 2], [8, 0]]
                points = np.array(points)

                x = points[:, 0]
                y = points[:, 1]

                t = range(len(points))
                ipl_t = np.linspace(0.0, len(points) - 1, 100)

                x_tup = si.splrep(t, x, k=3)
                y_tup = si.splrep(t, y, k=3)

                x_list = list(x_tup)
                xl = x.tolist()
                x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

                y_list = list(y_tup)
                yl = y.tolist()
                y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

                x_i = si.splev(ipl_t, x_list)  # x interpolate values
                y_i = si.splev(ipl_t, y_list)  # y interpolate values
                pass_q = driver.find_element_by_xpath('//input[@id = "pass"]').click()

                for mouse_x, mouse_y in zip(x_i, y_i):
                    action.move_by_offset(mouse_x, mouse_y)
                    action.move_to_element(pass_q)
                    action.perform()
                    print(mouse_x, mouse_y)
                action.move_to_element(pass_q)
                action.perform()
            except:
                pass
            try:
                driver.find_element_by_xpath('//input[@id = "next-btn"]').click()
            except:
                pass
            try:
                driver.find_element_by_xpath('//input[@id = "Click_me_to_stop"]').click()
                done = True
            except:
                pass
            time.sleep(15)
        else:
            try:
                points = [[0, 0], [0, 2], [2, 3], [4, 0], [6, 3], [8, 2], [8, 0]]
                points = np.array(points)

                x = points[:, 0]
                y = points[:, 1]

                t = range(len(points))
                ipl_t = np.linspace(0.0, len(points) - 1, 100)

                x_tup = si.splrep(t, x, k=3)
                y_tup = si.splrep(t, y, k=3)

                x_list = list(x_tup)
                xl = x.tolist()
                x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

                y_list = list(y_tup)
                yl = y.tolist()
                y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

                x_i = si.splev(ipl_t, x_list)  # x interpolate values
                y_i = si.splev(ipl_t, y_list)  # y interpolate values
                fail_q = driver.find_element_by_xpath('//input[@id = "fail"]').click()
                action.move_to_element(fail_q)
                action.perform()
                for mouse_x, mouse_y in zip(x_i, y_i):
                    action.move_by_offset(mouse_x, mouse_y)
                    action.perform()
                    print(mouse_x, mouse_y)
            except:
                pass
            try:
                driver.find_element_by_xpath('//div[@id = "ext-gen335"]').click()
                actions = ActionChains(driver)
                actions.send_keys('a')
                actions.send_keys('b')
                actions.send_keys('c')
            except:
                pass
            try:
                driver.find_element_by_xpath('//input[@id = "next-btn"]').click()

            except:
                pass
            try:
                driver.find_element_by_xpath('//input[@id = "Click_me_to_stop"]').click()
                done = True
            except:
                pass
            time.sleep(3)


menu()

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
from time import sleep

if __name__ == '__main__':

    url = 'https://www.google.co.jp/'
#    url = 'http://abehiroshi.la.coocan.jp/'

    outputdir = '/home/firefox/output/'
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    profile = webdriver.FirefoxProfile()
#    USERAGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
#    profile.set_preference("general.useragent.override", USERAGENT)
#    profile.set_preference("permissions.default.image", 2)
#    profile.set_preference('permissions.default.stylesheet', 2)
    profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    profile.set_preference("network.proxy.ftp", "localhost")
    profile.set_preference("network.proxy.ftp_port", 8080)
    profile.set_preference("network.proxy.http", "localhost")
    profile.set_preference("network.proxy.http_port", 8080)
    profile.set_preference("network.proxy.socks", "localhost")
    profile.set_preference("network.proxy.socks_port", 8080)
    profile.set_preference("network.proxy.ssl", "localhost")
    profile.set_preference("network.proxy.ssl_port", 8080)
    profile.set_preference("network.proxy.type", 1)

    options = Options()
    options.set_headless(headless=True)
    driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver', options=options, firefox_profile=profile)

    try:
        driver.get(url)
        sleep(3)
        print('title:', driver.title)
        driver.save_screenshot(outputdir + 'screenshot-' + timestamp + '.png')
    finally:
       driver.quit()

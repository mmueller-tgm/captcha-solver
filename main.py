from selenium import webdriver
from tesserwrap import Tesseract
from PIL import Image
from io import BytesIO
from solver import TesserSolver
import base64

class main:
    def __init__(self, url=input("Please Specify the URL:\n")):
        # initialize tesseract
        self.solver = TesserSolver()
        # set driver
        self.driver = webdriver.Firefox()

        self.url = url

        self.run()

    def run(self):
        string, confidency = self.solver.solve(self.request())
        if len(string) != 5 or confidency < 75:
            self.run()
        else:
            self.set_out(string)

    def request(self):
        # get the webpage
        self.driver.get(self.url)
        # find the captcha dif
        self.el = self.driver.find_element_by_class_name('cdscaptchaimage')
        # extract the screenshot
        return Image.open(BytesIO(self.el.screenshot_as_png))

    def set_out(self, string):
        out = self.driver.find_element_by_class_name('cdscaptchaimage_textfeld')

        out.send_keys(string)

if __name__ == '__main__':
    main()
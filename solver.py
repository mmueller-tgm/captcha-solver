from tesserwrap import Tesseract
import re

class TesserSolver:
    def __init__(self):
        # initialize tesseract
        self.tr = Tesseract()

    def solve(self, img):
        # load the screenshot
        self.tr.ocr_image(img)
        # set segmentation mode
        self.tr.set_page_seg_mode(7)

        # print(tr.get_symbols())
        print(self.tr.get_mean_confidence())

        # get the text of the captcha
        string = re.sub(r'[^a-zA-Z0-9]', '', self.tr.get_utf8_text())

        return [string, self.tr.get_mean_confidence()]
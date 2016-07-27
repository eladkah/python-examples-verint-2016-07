'''
Contains ImageFile class that raises InvalidImageExt exception if it receives a file name with invalid image extension
Tests with unit tests
'''

import unittest
import os


class InvalidImageExt(Exception):
    def __init__(self, message):
        super(InvalidImageExt, self).__init__(message)


class ImageFile(object):
    def __init__(self, file_name):
        self.check_ext(file_name)

    def check_ext(self, file_name):
        _, exten = os.path.splitext(file_name)
        if exten not in ('.png', '.jpg', '.jpeg', '.bmp'):
            raise InvalidImageExt('%s is not a valid extension' % exten)


class TestImageFile(unittest.TestCase):
    def test_good_ext(self):
        try:
            img = ImageFile("file.png")
        except InvalidImageExt:
            self.fail("png should be a valid file extension")

    def test_bad_ext(self):
        with self.assertRaises(InvalidImageExt):
            img = ImageFile("file.mp3")

unittest.main()

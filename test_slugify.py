import unittest
from Slugify import slugify

class TestSlugify(unittest.TestCase):
    def test_HelloWorld(self):
        self.assertEqual(slugify("Hello World"), "hello-world")
    def test_Punctuation(self):
        self.assertEqual(slugify("Ball State University!"), "ball-state-university")
    def test_MultipleSpaces(self):
        self.assertEqual(slugify("   This   is    a    test"), "this-is-a-test")
    def test_Empty(self):
        self.assertEqual(slugify(""), "")
    def test_SpecialCharacters(self):
        self.assertEqual(slugify("@#%^"), "")
if __name__ == '__main__':
    unittest.main()
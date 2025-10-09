import unittest
def IsPalindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertFalse(IsPalindrome("Hello"))
        self.assertTrue(IsPalindrome("Racecar"))
        self.assertTrue(IsPalindrome(""))
        self.assertTrue(IsPalindrome("Able was I ere I saw Elba"))
if __name__ == '__main__':
    unittest.main()
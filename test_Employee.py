import unittest
from employee import Employee
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("John", "Doe", 50000)
    def test_GiveRaise(self):
        self.employee.GiveRaise(5000)
        self.assertEqual(self.employee.salary, 55000)
if __name__ == '__main__':
    unittest.main()
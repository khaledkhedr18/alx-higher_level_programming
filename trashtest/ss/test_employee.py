import unittest
from unittest import patch
from employee import Employee
import requests

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('khaled', 'khedr', 10000)
        self.emp_2 = Employee('hanin', 'nahrawy', 8000)

    
    def tearDown(self):
         pass

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'khaled.khedr@email.com')
        self.assertEqual(self.emp_2.email, 'hanin.nahrawy@email.com')
		
        self.emp_1.first = 'hassan'
        self.emp_2.first = 'eman'

        self.assertEqual(self.emp_1.email, 'hassan.khedr@email.com')
        self.assertEqual(self.emp_2.email, 'eman.nahrawy@email.com')
    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname, 'khaled khedr')
        self.assertEqual(self.emp_2.fullname, 'hanin nahrawy')
		
        self.emp_1.first = 'hassan'
        self.emp_2.first = 'eman'

        self.assertEqual(self.emp_1.fullname, 'hassan khedr')
        self.assertEqual(self.emp_2.fullname, 'eman nahrawy')

    def monthly_schedule(self, month):
         response = requests.get(f'http://company.com/{self.last}/{month}')
         if response.ok:
              return response.text
         else:
              return 'Bad response!'
if __name__ == '__main__':
	unittest.main()
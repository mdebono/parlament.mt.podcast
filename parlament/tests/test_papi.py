import unittest

from parlament import papi

class TestParlamentApi(unittest.TestCase):

    def test_get_title(self):
        sitting = {'Title': 'This is a title'}
        title = papi.get_sitting_title(sitting)
        self.assertEqual(title, 'This is a title')

if __name__ == '__main__':
    unittest.main()
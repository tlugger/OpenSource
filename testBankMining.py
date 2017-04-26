import unittest
from BankMining import rowCount

class TestFileSize(unittest.TestCase):
    def test_size(self):
	filesize = 614
	self.assertEqual(filesize, rowCount())

if __name__ == '__main__':
    unittest.main()

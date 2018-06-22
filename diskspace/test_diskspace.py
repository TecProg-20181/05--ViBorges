import unittest
import diskspace

class TestDiskspace(unittest.TestCase):

    def test_bytes_to_readble(self):
        blocks = 1024
        amount = diskspace.bytes_to_readable(blocks)
        self.assertEqual('512.00Kb', amount)

    def test_bytes_to_readble_zero(self):
        blocks = 0
        amount = diskspace.bytes_to_readable(blocks)
        self.assertEqual('0.00B', amount)

if __name__ == '__main__':
    unittest.main()

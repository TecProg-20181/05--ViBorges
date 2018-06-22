import unittest
import diskspace
import subprocess

class TestDiskspace(unittest.TestCase):

    def test_bytes_to_readble(self):
        blocks = 1024
        amount = diskspace.bytes_to_readable(blocks)
        self.assertEqual('512.00Kb', amount)

    def test_bytes_to_readble_zero(self):
        blocks = 0
        amount = diskspace.bytes_to_readable(blocks)
        self.assertEqual('0.00B', amount)

    def test_subprocess_check_output(self):
        cmd = 'ls'
        result_sub = subprocess.check_output(cmd)
        result_fuc = diskspace.subprocess_check_output(cmd)
        self.assertEqual(result_sub, result_fuc)


if __name__ == '__main__':
    unittest.main()

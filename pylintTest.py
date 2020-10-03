import unittest
import doctestTest
from subprocess import PIPE, Popen
class ProductTestCase(unittest.TestCase):
    def test_withPyLint(self):
			cmd = 'pylint', '-rn', 'doctestTest'
			pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
			print(pylint.stdout.read())
			

if __name__ == '__main__':
    unittest.main()

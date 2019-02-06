#Modifying the test_integration example to test Hello, World!
#Uses subprocesses to run program and capture output

import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
import subprocess


class TestOutput(unittest.TestCase):
    def setUp(self):
        pass

    #Add in tests that comment at top of file?
    @weight(1)
    @tags("intro comments")
    def test_output(self):
        """Program begins with introductory comment """
	pr = open('studentProg.py', 'r')
        output = pr.readline()
        self.assertEqual(output[0], "#")


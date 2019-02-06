#Modifying the test_integration example to test Hello, World!
#Uses subprocesses to run program and capture output

import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
import subprocess


class TestOutput(unittest.TestCase):
    def setUp(self):
        pass

    @weight(4)
    @tags("output")
    def test_output(self):
        """Drawing octagon. """
        studentProg = subprocess.Popen(['python3','studentProg.py'],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	#Is the -u option necessary?
        output = studentProg.stdout.readlines()
        print('Program ended with position: ')
	print(output[-1])
        print('Expected position:  heading: 0 turns: 8')
        self.assertEqual(output[-1], "heading: 0 turns: 8\n")
        studentProg.terminate()

    #Add in tests that comment at top of file?
    #For future programs, can test functions individually...

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
        """Drawing spiral that grows. """
        studentProg = subprocess.Popen(['python3','studentProg.py'],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	#Is the -u option necessary?
        output = studentProg.stdout.read()
        print("Your program had the following color assignments:")
        print(output)
        print ("Expected colors:  bgcolor: purple\n color: white\n")
        correct = False
        if output.find('purple') > -1 and output.find('white') > -1:
             correct = True
        self.assertEqual(correct, True)
        studentProg.terminate()

    #Add in tests that comment at top of file?
    #For future programs, can test functions individually...

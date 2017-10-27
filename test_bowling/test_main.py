import tempfile
import unittest

import os

from bowling.__main__ import main


class MainTest(unittest.TestCase):
    def test_main(self):
        dir = tempfile.mkdtemp('bowling')
        input = os.path.join(dir, 'input')
        output = os.path.join(dir, 'output')
        os.chdir(dir)
        with open(input, 'w') as f:
            f.write("1\n2\n3\n4\n")
        main()
        with open(output) as f:
            score = f.readline()
            try:
                score = int(score.strip())
                self.assertEqual(score, 10)
            except ValueError:
                self.fail('expected "' + score + '" to be an integer value')

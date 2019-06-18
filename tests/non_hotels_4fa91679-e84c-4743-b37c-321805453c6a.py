

from unittest import *
import unittest
from ..src.rename import RandomRename

class RenameTest(TestCase):
    # instance 

    def test_files_by_extension(self): 
        r = RandomRename()
        files = r.find_by_extension(['eer.py' 'ererwe.py', 'werw.jpg', 'werwr.jp', 'waa.jpeg', 'werwef.qwe', 'qweew.p', 'ewq.w'], ['.py', 'p'])
        self.assertEquals(files, ['eer.py', 'ererwe.py', 'qweew.p'], "Incorrect")
    

unittest.main()
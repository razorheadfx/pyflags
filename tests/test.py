import unittest
from dateutil import parser
import datetime

from .. import pyflags




class TestPyflags(unittest.TestCase):
    
    def setUp(self):
        f = pyflags.Flags()
        self.f = f
        f.simple("-int", func = lambda args:  int(args[0]) )
        f.flag("-datetime", argcount = 2, func = lambda args: parser.parse("%s %s" %(args[0],args[1])))
        f.boolean("-b")
        f.flag("--notthere", argcount = 2, func = lambda args: "%s %s should not be seen" %(args[0], args[1]))
        f.boolean("-false")
        f.boolean("-s")
        f.flag("-collectme", argcount = 2, func = None)
        
    
    def testBooleans(self):
        f = self.f
        a = "add -s -b"
        args = a.split(" ")
        
        leftovers = ["add"]
        notleftovers = ["-s", "-b"]
            
        vals = f.parse_all(args)
            
        left = f.leftover_args
            
            
        
        for l in leftovers:
            self.assertIn(l, left, "Should be leftover")
        
        for n in notleftovers:
            self.assertNotIn(n, left, "Should not be leftover")
        
        self.assertTrue(vals["-b"] == True)
        self.assertTrue(vals["-false"] == False)
        self.assertTrue(vals["-s"] == True)
        
    def testMultiArg(self):
        f = self.f
        a = "add -datetime 2017.07.11 10:35 -collectme a b"
        args = a.split(" ")
        
        leftovers = ["add"]
        notleftovers = ["-datetime", "2017.07.11","10:35","-collectme", "a","b"]
            
        vals = f.parse_all(args)
            
        left = f.leftover_args
            
            
        
        for l in leftovers:
            self.assertIn(l, left, "Should be leftover")
        
        for n in notleftovers:
            self.assertNotIn(n, left, "Should not be leftover")
        
        self.assertTrue(vals["-datetime"] == datetime.datetime(2017, month = 7, day = 11, hour = 10, minute = 35))
        self.assertTrue(vals["-collectme"] == ["a","b"])
        
    def testCustomFunc(self):
        f = self.f
        a = "add -int 4 -datetime 2017.07.11 10:35"
        args = a.split(" ")
        
        leftovers = ["add"]
        notleftovers = ["-int" ,"4","-datetime", "2017.07.11","10:35"]
        
        vals = f.parse_all(args)
            
        left = f.leftover_args
        
        for l in leftovers:
            self.assertIn(l, left, "Should be leftover")
        
        for n in notleftovers:
            self.assertNotIn(n, left, "Should not be leftover")
        
        self.assertTrue(vals["-datetime"] == datetime.datetime(2017, month = 7, day = 11, hour = 10, minute = 35))
        self.assertTrue(vals["-int"] == 4)
        
    
if __name__ == "__main__":
    unittest.main()
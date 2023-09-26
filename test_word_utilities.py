"""Word Utilites.

Actually Slices the word.
Author: Frankie Benedetto
Version: 12/12/22
Honor Code: TA's
"""
import unittest
from word_utilities import WordUtilities

class TestWordUtilities(unittest.TestCase):
    
    def test1(self):
        x = WordUtilities()
        x.slicer("Ability")
        self.assertEqual(["ABI", "LI", "TY"], x.el_list)
    
    def test2(self):
        x = WordUtilities()
        x.slicer("Absolute")
        self.assertEqual(["AB", "SO", "LU", "TE"], x.el_list)
        
    def test3(self):
        x = WordUtilities()
        x.slicer("Abhorrent")
        self.assertEqual(["ABH", "ORR", "ENT"], x.el_list)
        
if __name__ == "__main__":
    unittest.main()
    
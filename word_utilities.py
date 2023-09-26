"""Word Utilites.

Actually Slices the word.
Author: Frankie Benedetto
Version: 12/12/22
Honor Code: TA's
"""
from word_slice import WordSlice


class WordUtilities:
    """This the class."""

    def slicer(self, word):
        """Slices a word.

        Args:
            word(str): Its a word.

        Returns:
            el_list(list): List of slices.
        """
        word = word.upper()
        self.el_list = []
        length = len(word)
        if length % 3 == 0:
            for x in range(0, length, 3):
                self.el_list.append(word[x:x+3])
        elif length % 2 == 0:
            for x in range(0, length, 2):
                self.el_list.append(word[x:x+2])
        else:
            self.el_list.append(word[0:3])
            for x in range(3, length, 2):
                self.el_list.append(word[x:x+2])
                
        el_list2 = []
        for x in self.el_list:
            y = WordSlice(x)
            el_list2.append(y)

        return el_list2
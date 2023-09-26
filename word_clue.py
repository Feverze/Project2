"""Word Clue.

Actually Slices the word.
Author: Frankie Benedetto
Version: 12/12/22
Honor Code: TA's
"""
from word_utilities import WordUtilities


class WordClue:
    """This is the class for WordClue."""
     
    def __init__(self, word='', clue=''):
        """Its the intializer.
            
        Args:
            word(str): its a word.
            clue(str): clue for word.
        """
        self.word = word
        self.clue = clue
        MIN_WORD_LENGTH = 4
        MAX_CLUE_LENGTH = 40
        self.el_list = []
        word_util = WordUtilities()
        self.cortadora = word_util.slicer(self.word)
        if word is None or len(word) < MIN_WORD_LENGTH:
            self.word = 'DEFAULT'
        else:
            self.word = word
            
        if clue is None or len(clue) > MAX_CLUE_LENGTH or len(clue) == 0:
            self.clue = 'DEFAULT CLUE'
        else:
            self.clue = clue
            
        for x in self.cortadora:
            y = str(x)
            self.el_list.append(y)
            
    def __eq__(self, other):
        """Its the __eq__.
        
        Args:
            other: other value
            
        Returns:
            bool: True or False.
        """
        if isinstance(other, WordClue):
            return self.word.upper() == other.word.upper()
        
    def get_clue(self):
        """Gets the clue.
            
        Returns:
            clue(str): clue for word.
        """
        return self.clue
        
    def get_first_letter_hint(self):
        """Gets a letter.
            
        Returns:
            self.word(str): Gets a letter.
        """
        return self.word[0].upper()
        
    def get_first_slice_hint(self):
        """Gets first slice.
            
        Returns:
            self.el_list(list): list of slices.
        """
        return self.el_list[0]
        
    def get_whole_word_hint(self):
        """Gives the whole word.
            
        Returns:
            self.word.upper(str): its a word.
        """
        return self.word.upper()
        
    def get_slices(self):
        """Gets a slice.
            
        Returns:
            self.el_list(list): lists of slices.
        """
        return self.el_list
        
    def get_word(self):
        """This gets a word.
            
        Returns:
            self.word(str): its a word.
        """
        return self.word
        
    def __str__(self):
        """Returns the string.
            
        Returns:
            string(str): string of words.
        """
        return f"{self.word}-{self.clue}\n{' '.join(self.el_list)}\n"
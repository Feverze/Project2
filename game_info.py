"""Game info.

The games information.
Author: Frankie Benedetto
Version: 12/12/22
Honor Code: TA's
"""
from word_clue import WordClue
from file_utilities import FileUtilities
from word_utilities import WordUtilities


class GameInfo:
    """This is the class for GameInfo."""

    NUMBER_OF_WORDS = 7
    
    def __init__(self, el_name):
        """Its the intializer.
            
        Args:
            el_name(list): empty list.
        """
        self.el_name = el_name
        teacher_sent = FileUtilities.read_lines_from_file(el_name, GameInfo.NUMBER_OF_WORDS)
        slicing = WordUtilities()
        self.word_slices = []
        self.cluelist = []
        self.clues_to_words = []

        word_num = 0
        for x in teacher_sent:
            y = x.split('-')
            self.cluelist.append(WordClue(y[0], y[1]))
            word_num += 1

        if word_num == GameInfo.NUMBER_OF_WORDS:
            self.complete = True
        else:
            self.complete = False

        for x in range(len(self.cluelist)):
            y = slicing.slicer(self.cluelist[x].word)
            for a in y:
                self.word_slices.append(a)
            
    def get_slices(self):
        """Gets some slices.
            
        Returns:
            self.word_slices(list): Gets slices.
        """
        return self.word_slices
    
    def get_word_clues(self):
        """List of clues.
            
        Returns:
            self.clues_to_words(list): clues.
        """
        return self.clues_to_words
        
    def __str__(self):
        """Returns a string.
            
        Returns:
            z(str): its a string.
            a(str): its a string
        """
        z = 'Cluelist'
        x = 0
        while x < len(self.cluelist):
            z += self.cluelist[x].word + '-' + self.cluelist[x].clue
            x += 1
        a = '\nSlices\n'
        for y in range(len(self.word_slices)):
            a += f"{self.word_slices[y]}"
        return z + a
            
    def is_complete(self):
        """Tells if words of slices have been used.
            
        Returns:
            bool: True or False.
        """
        return self.complete
        
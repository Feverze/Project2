"""Word Slice.

Tells if been sliced or not.
Author: Frankie Benedetto
Version: 12/12/22
Honor Code: TA's
"""


class WordSlice:
    """This the class."""

    def __init__(self, text):
        """Its the intializer.
            
        Args:
            text(str): its a word.
        """
        self.text = text
        self.used = False
        
    def is_used(self):
        """Word used or not.

        Returns:
            bool: T or F
        """
        return self.used
   
    def reset(self):
        """Resets the used value."""
        self.used = False
         
    def __str__(self):
        """Returns blank line if being used.

        Returns:
            str: blank line
        """
        if self.used is False:
            return self.text
        else:
            return ''
        
    def use(self):
        """Makes it true if needed."""
        self.used = True
         

       
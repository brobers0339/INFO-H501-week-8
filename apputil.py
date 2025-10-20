from collections import defaultdict


class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None  # you'll need to build this

    def get_term_dict(self):
        '''
        Build a term dictionary mapping each word in the corpus to a list of words 
        that immediately follow it.

        This function splits the corpus text into individual words, then iterates 
        through them to create a mapping where each key is a word and its value 
        is a list of words that occur directly after that word in the corpus.

        Returns
        -------
        dict
            A dictionary where keys are words (str) and values are lists of 
            subsequent words (list of str).
        '''

        self.corpus = self.corpus.split()

        self.term_dict = defaultdict(list)

        index = 1


        for word in self.corpus:
            if index < len(self.corpus) - 1:
                self.term_dict[word].append(self.corpus[index])
                index += 1
            else:
                return self.term_dict


    def generate(self, seed_term=None, term_count=15):

        # your code here ...

        return None